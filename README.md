<div style="display: flex;">
    <a href="https://playwright.dev/">
        <img alt="Playwright" src="https://www.lambdatest.com/resources/images/header/Playwright_logo.svg" width="250" style="margin-right: 100px;"/>
    </a>
    <a href="https://www.python.org/">
        <img alt="Python" src="https://www.python.org/static/img/python-logo.png" width="200"/>
    </a>
</div>

### **API Automation Framework**

### Initial Setup:
- Install and configure [Python3](https://www.python.org/downloads/)
- Setup your IDE (Preferably [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows))
- Import cloned repository as project
- Install allure plugin for reporting

    - For Windows:
      - Run this command in powershell
          ```sh
            iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
          ```
      - After installing scoop run this command
          ```sh
            scoop install allure
          ```

    - For Mac:
      - Run this command on terminal to install homebrew
          ```sh
            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
          ```
      - After installing homebrew run this command
          ```sh
            brew install allure
          ```

    - For Linux:
      - Run following commands to install the allure on linux
          ```sh
            sudo apt-add-repository ppa:qameta/allure
            sudo apt-get update
            sudo apt-get install allure
          ```

- Install all required packages using this command
    ```sh
    pip install -r requirements.txt
    ```

### Example:
- Open pycharm terminal (Alt+F12) and run following command to run the tests
    ```sh
    python run_tests.py --env DEV 
    ```
  In the above command specify the environment to run tests against (e.g., QA, DEV, STAGE). By default, it will run on QA.

- Trigger Allure Reports
    ```sh
    allure serve ExecutionReports/{report_folder}
    ```