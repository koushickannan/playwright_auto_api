import os
import shutil
import subprocess

# Directory where Allure reports are stored
ALLURE_REPORT_DIR = "ExecutionReports"

# Remove the existing Allure report directory if it exists
if os.path.exists(ALLURE_REPORT_DIR):
    shutil.rmtree(ALLURE_REPORT_DIR)
    print("Old Allure reports deleted.")

# Run pytest to execute tests and generate new Allure reports
subprocess.run(["pytest", "--alluredir", ALLURE_REPORT_DIR])
