import os
import subprocess
import argparse
from datetime import datetime

# Argument parser to accept environment input
parser = argparse.ArgumentParser(description="Run pytest with Allure report generation.")
parser.add_argument(
    "--env",
    type=str,
    required=True,
    help="Specify the environment to run tests against (e.g., QA, DEV, STAGE)"
)
parser.add_argument(
    "--tests",
    type=str,
    nargs='*',  # Accept zero or more test files
    help="Specify the test files or test cases to run (e.g., test_file.py or test_file.py::test_case)"
)

# Parse arguments
args = parser.parse_args()
env = args.env
tests = args.tests

# Directory where Allure reports are stored
base_report_dir = "ExecutionReports"

# Create a unique directory for this run based on the current timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
allure_report_dir = os.path.join(base_report_dir, f"report_{timestamp}")

# Ensure the directories exist
os.makedirs(allure_report_dir, exist_ok=True)

# Run pytest to execute tests and generate new Allure reports
pytest_args = ["pytest", "--env", env, "--alluredir", allure_report_dir]
if tests:
    pytest_args.extend(tests)
subprocess.run(pytest_args)
