"""
Integration Test Class for LLM-Generated Functions
This module integrates three functions to demonstrate complex interactions and edge cases.
"""

import math
from typing import List, Union, Tuple, Any

class DataProcessor:
    """
    Integrated class that combines three functions:
    1. mean_absolute_deviation - calculates statistical measures
    2. find_closest_elements - finds relationships in data
    3. select_words - filters and processes text data
    
    This class demonstrates how these functions can work together in a data processing pipeline.
    """
    
    def __init__(self):
        self.processed_data = []
        self.statistics = {}
        self.filtered_results = []
    
    def mean_absolute_deviation(self, numbers: List[float]) -> float:
        """Calculate the Mean Absolute Deviation of a list of numbers."""
        if not numbers:
            return 0.0
        
        # Type validation - critical edge case from analysis
        validated_numbers = []
        for num in numbers:
            if isinstance(num, bool):
                raise TypeError("Boolean inputs not allowed")
            if not isinstance(num, (int, float)):
                raise TypeError(f"Non-numerical input: {num}")
            validated_numbers.append(float(num))
        
        mean = sum(validated_numbers) / len(validated_numbers)
        return sum(abs(x - mean) for x in validated_numbers) / len(validated_numbers)
    
    def find_closest_elements(self, numbers: List[float]) -> Tuple[float, float]:
        """Find the two closest elements in a list."""
        if len(numbers) < 2:
            raise ValueError("Need at least 2 elements")
        
        # Type validation
        validated_numbers = []
        for num in numbers:
            if isinstance(num, bool):
                raise TypeError("Boolean inputs not allowed")
            if not isinstance(num, (int, float)):
                raise TypeError(f"Non-numerical input: {num}")
            validated_numbers.append(float(num))
        
        min_distance = float('inf')
        closest_pair = (validated_numbers[0], validated_numbers[1])
        
        for i in range(len(validated_numbers)):
            for j in range(i + 1, len(validated_numbers)):
                distance = abs(validated_numbers[i] - validated_numbers[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (validated_numbers[i], validated_numbers[j])
        
        return closest_pair
    
    def select_words(self, s: str, n: int) -> List[str]:
        """Select words that have exactly n consonants."""
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n < 0:
            raise ValueError("n cannot be negative")
        
        vowels = set('aeiouAEIOU')
        words = s.split()
        result = []
        
        for word in words:
            consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
            if consonant_count == n:
                result.append(word)
        
        return result
    
    def process_numerical_data(self, data: List[float]) -> dict:
        """
        Integration method 1: Process numerical data and return comprehensive statistics.
        Uses mean_absolute_deviation and find_closest_elements together.
        """
        if not data:
            return {"error": "Empty dataset"}
        
        try:
            # Calculate statistical measures
            mad = self.mean_absolute_deviation(data)
            closest_pair = self.find_closest_elements(data)
            
            # Store results
            result = {
                "mean_absolute_deviation": mad,
                "closest_elements": closest_pair,
                "closest_distance": abs(closest_pair[0] - closest_pair[1]),
                "data_count": len(data),
                "data_range": max(data) - min(data) if data else 0
            }
            
            self.statistics = result
            return result
            
        except (TypeError, ValueError) as e:
            return {"error": str(e)}
    
    def analyze_text_with_numbers(self, text: str, target_consonants: int, 
                                  numerical_context: List[float] = None) -> dict:
        """
        Integration method 2: Analyze text and provide numerical context.
        Uses select_words with numerical processing functions.
        """
        try:
            # Process text
            selected_words = self.select_words(text, target_consonants)
            
            # Create numerical context if not provided
            if numerical_context is None:
                # Generate numbers based on word lengths
                numerical_context = [len(word) for word in selected_words]
            
            # Process numerical data if available
            numerical_stats = {}
            if len(numerical_context) >= 2:
                numerical_stats = self.process_numerical_data(numerical_context)
            elif len(numerical_context) == 1:
                numerical_stats = {
                    "mean_absolute_deviation": 0.0,
                    "closest_elements": None,
                    "data_count": 1,
                    "single_value": numerical_context[0]
                }
            
            result = {
                "selected_words": selected_words,
                "word_count": len(selected_words),
                "target_consonants": target_consonants,
                "numerical_analysis": numerical_stats,
                "integration_successful": True
            }
            
            self.filtered_results = result
            return result
            
        except Exception as e:
            return {
                "error": str(e),
                "integration_successful": False
            }
    
    def comprehensive_data_pipeline(self, text_data: str, numerical_data: List[float], 
                                   consonant_filter: int) -> dict:
        """
        Integration method 3: Complete data processing pipeline.
        Combines all three functions in a complex workflow.
        """
        pipeline_results = {
            "text_analysis": {},
            "numerical_analysis": {},
            "cross_analysis": {},
            "pipeline_status": "starting"
        }
        
        try:
            # Step 1: Text processing
            pipeline_results["pipeline_status"] = "processing_text"
            text_result = self.analyze_text_with_numbers(text_data, consonant_filter)
            pipeline_results["text_analysis"] = text_result
            
            # Step 2: Numerical processing
            pipeline_results["pipeline_status"] = "processing_numbers"
            numerical_result = self.process_numerical_data(numerical_data)
            pipeline_results["numerical_analysis"] = numerical_result
            
            # Step 3: Cross-analysis
            pipeline_results["pipeline_status"] = "cross_analysis"
            if (text_result.get("integration_successful") and 
                "error" not in numerical_result):
                
                word_lengths = [len(word) for word in text_result["selected_words"]]
                
                # Find correlation between word lengths and numerical data
                if len(word_lengths) >= 2 and len(numerical_data) >= 2:
                    # Compare MAD of word lengths vs numerical data
                    text_mad = self.mean_absolute_deviation(word_lengths)
                    num_mad = numerical_result["mean_absolute_deviation"]
                    
                    cross_analysis = {
                        "text_data_mad": text_mad,
                        "numerical_data_mad": num_mad,
                        "mad_ratio": text_mad / num_mad if num_mad != 0 else float('inf'),
                        "correlation_strength": "high" if abs(text_mad - num_mad) < 1.0 else "low"
                    }
                    
                    pipeline_results["cross_analysis"] = cross_analysis
                
                pipeline_results["pipeline_status"] = "completed_successfully"
            else:
                pipeline_results["pipeline_status"] = "completed_with_errors"
            
            return pipeline_results
            
        except Exception as e:
            pipeline_results["pipeline_status"] = "failed"
            pipeline_results["error"] = str(e)
            return pipeline_results
    
    def get_processing_summary(self) -> dict:
        """Get summary of all processing done by this instance."""
        return {
            "statistics": self.statistics,
            "filtered_results": self.filtered_results,
            "processed_data_count": len(self.processed_data)
        }
