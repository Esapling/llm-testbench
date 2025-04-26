import os
import sys
import subprocess
import re # Import the regular expression module

dir = os.path.dirname(__file__)
sys.path.append(dir)

dirs = os.listdir(dir)
dirs = [d for d in dirs if os.path.isdir(os.path.join(dir, d)) and not d.startswith('__')]

total_failed_tests = 0 # Rename to reflect counting tests
total_directories_tested = 0
directories_with_failures = 0 # Keep track of directories with any failure

with open("result.txt", "w") as result_file:
    for d in dirs:
        print(f"Running tests in {d}...")
        command = [
            "python", "-m", "unittest", "discover",
            "-s", os.path.join(dir, d),
            "-p", "*.py"
        ]

        process_result = subprocess.run(command, capture_output=True, text=True)
        result_file.write(f"--- Results for directory: {d} ---\n")
        result_file.write(process_result.stdout)
        result_file.write(process_result.stderr)
        result_file.write("\n\n")

        total_directories_tested += 1

        # Parse stderr to find the number of failures
        failures_in_dir = 0
        if process_result.returncode != 0:
            directories_with_failures += 1
            # Search for the "FAILED (failures=N)" pattern in stderr
            match = re.search(r"FAILED \(failures=(\d+)\)", process_result.stderr)
            if match:
                try:
                    failures_in_dir = int(match.group(1))
                    total_failed_tests += failures_in_dir
                except ValueError:
                    print(f"Warning: Could not parse failure count for directory {d}")
            else:
                 # Handle cases where stderr might indicate failure differently (e.g., errors)
                 # For simplicity, we can check if 'FAIL' or 'ERROR' is present if the pattern isn't found
                 if "FAIL:" in process_result.stderr or "ERROR:" in process_result.stderr:
                     # We know there were failures, but couldn't parse the exact count
                     # This part might need refinement based on actual unittest error output formats
                     print(f"Warning: Detected failures but couldn't parse exact count for directory {d}")
                     # Optionally, increment by 1 if specific count isn't found but errors exist
                     # total_failed_tests += 1 # Or handle as appropriate

with open("log.txt", "w") as log_file:
    log_file.write(f"Total directories tested: {total_directories_tested}\n")
    log_file.write(f"Directories with failures: {directories_with_failures}\n")
    log_file.write(f"Total test filed test cases: {total_failed_tests}\n") # Write the total failed test count
print(f"Finished running tests.")
print(f"Total directories tested: {total_directories_tested}")
print(f"Directories with failures: {directories_with_failures}")
print(f"Total failed tests: {total_failed_tests}") # Print the total failed test count