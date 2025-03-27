from dotenv import load_dotenv
from jira import JIRA
import os
import datetime

load_dotenv(override=True)

JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API = os.getenv("JIRA_API")

jira = JIRA(
    server = JIRA_SERVER,
    basic_auth=(JIRA_USERNAME, JIRA_API)
                )
print(jira.projects())
# print(jira.myself)
for i  in jira.issue_types():
    if i.name.lower()in ["bug","баг","ошибка"]:
        bug_type = i 

jira_issue = jira.create_issue(
    {
        "project":{"key":"GOIDA"},
        "summary": "задача теста",
        "description": f"ошибка название ошибки\n\nДата: {datetime.datetime.now()}",
        "issuetype": {"id":bug_type.id}
    }
)

jira.add_attachment(jira_issue.key,"29e890cb-00a9-4475-a9e0-d83a8047fc37.jfif")