import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../app")))
from tasks import add_task, get_tasks
def test_add_task():
    add_task("learn docker")
    assert "learn docker" in get_tasks()
def test_multiple_tasks():
    add_task("learn ci")
    add_task("learn devops")
    tasks=get_tasks()
    assert "learn ci" in tasks
    assert "learn devops" in tasks