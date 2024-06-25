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

# Parse arguments
args = parser.parse_args()
env = args.env

# Directory where Allure reports are stored
base_report_dir = "ExecutionReports"

# Create a unique directory for this run based on the current timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
allure_report_dir = os.path.join(base_report_dir, f"report_{timestamp}")
# html_report_dir = os.path.join(base_report_dir, f"html_report_{timestamp}")

# Ensure the directories exist
os.makedirs(allure_report_dir, exist_ok=True)
# os.makedirs(html_report_dir, exist_ok=True)

# Run pytest to execute tests and generate new Allure reports
subprocess.run(["pytest", f"--env={env}", "--alluredir", allure_report_dir])

# # Generate the HTML report
# subprocess.run(["allure", "generate", allure_report_dir, "-o", html_report_dir])
#
# print(f"Allure HTML report generated at: {html_report_dir}")
#
# # Optionally serve the report
# subprocess.run(["allure", "serve", html_report_dir])