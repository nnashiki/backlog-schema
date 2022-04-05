from backlog_schema import __version__, AddTaskRequest, Project, CreatedUser, Content

def test_version():
    assert __version__ == '0.1.0'

def test_parse_add_task_request_raw():
    add_task_request_raw = """
{
  "id": 0,
  "project": {
    "id": 0,
    "projectKey": "project.projectKey",
    "name": "project.name",
    "chartEnabled": true,
    "subtaskingEnabled": false,
    "projectLeaderCanEditProjectLeader": false,
    "useWikiTreeView": true,
    "textFormattingRule": "markdown",
    "archived": false
  },
  "type": 1,
  "content": {
    "id": 100,
    "key_id": 100,
    "summary": "test issue",
    "description": "test description",
    "issueType": {
      "id": 100,
      "projectId": 100,
      "name": "test",
      "color": "#e30000",
      "displayOrder": -1
    },
    "resolution": null,
    "priority": {
      "id": 3,
      "name": "中"
    },
    "status": {
      "id": 1,
      "name": "未対応"
    },
    "assignee": null,
    "category": [],
    "versions": [],
    "milestone": [],
    "startDate": null,
    "dueDate": null,
    "estimatedHours": null,
    "actualHours": null,
    "parentIssueId": null,
    "customFields": [],
    "attachments": []
  },
  "notifications": [],
  "createdUser": {
    "id": 0,
    "userId": null,
    "name": "createdUser.name",
    "roleType": 2,
    "lang": "ja",
    "mailAddress": null,
    "nulabAccount": {
      "nulabId": "nulabAccount.nulabId",
      "name": "nulabAccount.name",
      "uniqueId": "nulabAccount.uniqueId"
    }
  },
  "created": "2022-04-01T09:00:00Z"
}
    """

    add_task_request = AddTaskRequest.parse_raw(add_task_request_raw)
    assert add_task_request.id == 0
    assert add_task_request.type == 1
    assert len(add_task_request.notifications) == 0
    assert add_task_request.created == "2022-04-01T09:00:00Z"
    assert isinstance(add_task_request.project, Project)
    assert isinstance(add_task_request.content, Content)
    assert isinstance(add_task_request.createdUser, CreatedUser)
