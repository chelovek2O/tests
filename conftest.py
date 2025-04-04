import pytest
import os
from selenium import webdriver
from jira import JIRA
from dotenv import load_dotenv
from datetime import datetime
from selenium.webdriver.chrome.options import Options


JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API = os.getenv("JIRA_API")
def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="Выберите браузер: chrome или firefox")
    parser.addoption("--jira", action="store_true", help="Включить интеграцию с Jira")
    
@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\n start Chrome")
        options = Options()
        options.page_load_strategy = 'eager'
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1920, 1080)
    elif browser_name == "firefox":
        print("\n start Firefox")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
        
  
    
    yield browser
    
    print("\n quit browser")
    browser.quit()


@pytest.fixture(scope="session")
def jira_client(request):
    if request.config.getoption("jira"):
        jira = JIRA(
            server=JIRA_SERVER,
            basic_auth=(JIRA_USERNAME, JIRA_API)
        )
        return jira

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and hasattr(report, "wasxfail") and report.outcome == "passed":
        print("все кайф")

    if report.when == "call" and report.outcome == "failed":
        if "browser" in item.funcargs:
            browser = item.funcargs["browser"]
            browser.save_screenshot("Скриншот_ошибки.png")

        if "jira_client" in item.funcargs:
            jira = item.funcargs["jira_client"]
            if jira:
                issue_type = jira.issue_types()
                bug_type = issue_type[4]

                issue_dict = {
                    "project": {"key": "GOIDA"},
                    "summary": f"{item.name}",
                    "description": f"Ошибка: {report.longreprtext}\n\nДата: {datetime.now()}",
                    "issuetype": {"id": bug_type.id}
                }

                new_issue = jira.create_issue(fields=issue_dict)
                jira.add_attachment(new_issue.key, "Скриншот_ошибки.png")
# try:
#     assert 1 == 0
# except AssertionError as e:
#     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAшибкаа")