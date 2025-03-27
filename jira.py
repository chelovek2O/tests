from dotenv import load_dotenv
from jira import JIRA
import os

load_dotenv

JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API = os.getenv("JIRA_API")
jira = JIRA(
    server = JIRA_SERVER,
    basic_auth=(JIRA_USERNAME, JIRA_API)
                )
print(jira.projects())