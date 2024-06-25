import os
import shutil
import subprocess
import argparse

# Argument parser to accept environment input
parser = argparse.ArgumentParser(description="Run pytest with Allure report generation.")
parser.add_argument(
    "--env",
    type=str,
    required=True,
    help="Specify the environment to run tests against (e.g., QA, DEV, STAGE)"
)

# Parse arguments
args = parser.parse_args()
env = args.env

# Directory where Allure reports are stored
ALLURE_REPORT_DIR = "ExecutionReports"

# Remove the existing Allure report directory if it exists
if os.path.exists(ALLURE_REPORT_DIR):
    shutil.rmtree(ALLURE_REPORT_DIR)
    print("Old Allure reports deleted.")

# Run pytest to execute tests and generate new Allure reports
subprocess.run(["pytest", "--env", env, "--alluredir", ALLURE_REPORT_DIR])
