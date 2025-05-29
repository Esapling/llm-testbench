"""
Comprehensive Integration Tests for DataProcessor Class
Tests the interaction between mean_absolute_deviation, find_closest_elements, and select_words
"""

import unittest
import math
from integration_test_class import DataProcessor

class TestDataProcessorIntegration(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.processor = DataProcessor()
    
    def test_individual_functions_basic(self):
        """Test that individual functions work correctly in isolation."""
        # Test mean_absolute_deviation
        result = self.processor.mean_absolute_deviation([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 1.2, places=1)
        
        # Test find_closest_elements
        closest = self.processor.find_closest_elements([1.0, 3.0, 2.0, 5.0])
        self.assertEqual(closest, (1.0, 2.0))
        
        # Test select_words
        words = self.processor.select_words("hello world test", 3)
        self.assertEqual(words, ["hello", "world"])
    
    def test_edge_cases_from_analysis(self):
        """Test critical edge cases identified in the LLM analysis."""
        
        # Test boolean input rejection (universal failure in LLM analysis)
        with self.assertRaises(TypeError):
            self.processor.mean_absolute_deviation([1, 2, True, 4])
        
        with self.assertRaises(TypeError):
            self.processor.find_closest_elements([1.0, False, 3.0])
        
        # Test empty inputs
        self.assertEqual(self.processor.mean_absolute_deviation([]), 0.0)
        
        with self.assertRaises(ValueError):
            self.processor.find_closest_elements([])
        
        # Test non-numerical inputs
        with self.assertRaises(TypeError):
            self.processor.mean_absolute_deviation([1, "string", 3])
        
        # Test negative consonant count
        with self.assertRaises(ValueError):
            self.processor.select_words("test", -1)
    
    def test_process_numerical_data_integration(self):
        """Test integration of mean_absolute_deviation and find_closest_elements."""
        
        # Normal case
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = self.processor.process_numerical_data(data)
        
        self.assertIn("mean_absolute_deviation", result)
        self.assertIn("closest_elements", result)
        self.assertIn("closest_distance", result)
        self.assertEqual(result["data_count"], 5)
        self.assertEqual(result["data_range"], 4.0)
        
        # Edge case: minimum valid input
        data_min = [1.0, 2.0]
        result_min = self.processor.process_numerical_data(data_min)
        self.assertEqual(result_min["closest_distance"], 1.0)
        
        # Edge case: empty data
        result_empty = self.processor.process_numerical_data([])
        self.assertIn("error", result_empty)
        
        # Edge case: invalid data types
        result_invalid = self.processor.process_numerical_data([1, "invalid", 3])
        self.assertIn("error", result_invalid)
    
    def test_analyze_text_with_numbers_integration(self):
        """Test integration of select_words with numerical processing."""
        
        # Normal case with provided numerical context
        text = "hello world python programming test"
        numerical_context = [5.0, 3.0, 8.0, 2.0]
        result = self.processor.analyze_text_with_numbers(text, 3, numerical_context)
        
        self.assertTrue(result["integration_successful"])
        self.assertIn("selected_words", result)
        self.assertIn("numerical_analysis", result)
        
        # Case with auto-generated numerical context (word lengths)
        result_auto = self.processor.analyze_text_with_numbers(text, 3)
        self.assertTrue(result_auto["integration_successful"])
        
        # Edge case: no matching words
        result_no_match = self.processor.analyze_text_with_numbers("a i o u", 5)
        self.assertEqual(result_no_match["word_count"], 0)
        
        # Edge case: single word
        result_single = self.processor.analyze_text_with_numbers("hello", 3)
        self.assertTrue(result_single["integration_successful"])
        
        # Edge case: invalid input types
        with self.assertRaises(TypeError):
            self.processor.analyze_text_with_numbers(123, 3)
    
    def test_comprehensive_data_pipeline(self):
        """Test the complete integration of all three functions."""
        
        # Normal case: successful pipeline
        text_data = "hello world python programming"
        numerical_data = [1.5, 2.0, 3.5, 2.2, 4.0]
        consonant_filter = 3
        
        result = self.processor.comprehensive_data_pipeline(
            text_data, numerical_data, consonant_filter
        )
        
        self.assertEqual(result["pipeline_status"], "completed_successfully")
        self.assertIn("text_analysis", result)
        self.assertIn("numerical_analysis", result)
        self.assertIn("cross_analysis", result)
        
        # Verify cross-analysis was performed
        if result["cross_analysis"]:
            self.assertIn("text_data_mad", result["cross_analysis"])
            self.assertIn("numerical_data_mad", result["cross_analysis"])
    
    def test_pipeline_error_handling(self):
        """Test pipeline behavior with various error conditions."""
        
        # Empty numerical data
        result_empty_num = self.processor.comprehensive_data_pipeline(
            "hello world", [], 3
        )
        self.assertEqual(result_empty_num["pipeline_status"], "completed_with_errors")
        
        # Invalid numerical data
        result_invalid_num = self.processor.comprehensive_data_pipeline(
            "hello world", [1, "invalid", 3], 3
        )
        self.assertEqual(result_invalid_num["pipeline_status"], "completed_with_errors")
        
        # Negative consonant filter
        with self.assertRaises(ValueError):
            self.processor.comprehensive_data_pipeline(
                "hello world", [1.0, 2.0], -1
            )
    
    def test_complex_integration_scenarios(self):
        """Test complex scenarios that combine multiple edge cases."""
        
        # Scenario 1: Large dataset with statistical significance
        large_data = list(range(1, 101))  # 1 to 100
        large_data_float = [float(x) for x in large_data]
        
        result_large = self.processor.process_numerical_data(large_data_float)
        self.assertGreater(result_large["mean_absolute_deviation"], 0)
        self.assertEqual(result_large["closest_distance"], 1.0)
        
        # Scenario 2: Text with varied word lengths and consonant counts
        complex_text = "a hello beautiful programming language with various word lengths"
        result_complex = self.processor.analyze_text_with_numbers(complex_text, 5)
        
        # Should find words with exactly 5 consonants
        expected_words = []
        for word in complex_text.split():
            consonants = sum(1 for c in word if c.isalpha() and c.lower() not in 'aeiou')
            if consonants == 5:
                expected_words.append(word)
        
        self.assertEqual(result_complex["selected_words"], expected_words)
        
        # Scenario 3: Pipeline with edge case combinations
        edge_text = "hi a programming"  # Mixed word lengths
        edge_numbers = [1.0, 1.1]  # Very close numbers
        
        result_edge = self.processor.comprehensive_data_pipeline(
            edge_text, edge_numbers, 2
        )
        
        self.assertIn("pipeline_status", result_edge)
    
    def test_state_management(self):
        """Test that the processor correctly manages internal state."""
        
        # Process some data
        self.processor.process_numerical_data([1.0, 2.0, 3.0])
        self.processor.analyze_text_with_numbers("hello world", 3)
        
        # Check state was stored
        summary = self.processor.get_processing_summary()
        self.assertIn("statistics", summary)
        self.assertIn("filtered_results", summary)
        
        # Verify statistics were stored
        self.assertNotEqual(self.processor.statistics, {})
        self.assertNotEqual(self.processor.filtered_results, {})
    
    def test_type_validation_consistency(self):
        """Test that type validation is consistent across all integrated functions."""
        
        # All functions should reject boolean inputs
        boolean_tests = [
            lambda: self.processor.mean_absolute_deviation([True, False]),
            lambda: self.processor.find_closest_elements([True, 1.0]),
            lambda: self.processor.process_numerical_data([False, 2.0])
        ]
        
        for test_func in boolean_tests:
            with self.assertRaises(TypeError):
                test_func()
        
        # String input validation
        with self.assertRaises(TypeError):
            self.processor.select_words(123, 3)
        
        with self.assertRaises(TypeError):
            self.processor.select_words("hello", "invalid")

if __name__ == "__main__":
    # Run the integration tests
    unittest.main(verbosity=2)
