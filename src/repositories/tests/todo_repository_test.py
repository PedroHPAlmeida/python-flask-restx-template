import pytest
from .. import TodoRepository


def test_get():
    todo_dao = TodoRepository()
    todo_1 = todo_dao.create({'task_1': 'Build an API 1'})
    todo_2 = todo_dao.create({'task_2': 'Build an API 2'})
    todo_3 = todo_dao.create({'task_3': 'Build an API 3'})

    assert todo_dao.get(1) == todo_1
    assert todo_dao.get(2) == todo_2
    assert todo_dao.get(3) == todo_3


def test_get_todo_doesnt_exist():
    todo_dao = TodoRepository()
    todo_dao.create({'task_1': 'Build an API 1'})
    todo_dao.create({'task_2': 'Build an API 2'})

    with pytest.raises(Exception):
        todo_dao.get(3)


def test_create():
    todo_dao = TodoRepository()
    todo = todo_dao.create({'task': 'Build an API'})

    assert todo_dao.get(1) == todo


def test_update():
    todo_dao = TodoRepository()
    todo_dao.create({'task': 'Build an API'})

    todo_updated = todo_dao.update(1, {'task': 'Build an API updated'})

    assert todo_updated == todo_dao.get(1)


def test_delete():
    todo_dao = TodoRepository()
    todo_dao.create({'task': 'Build an API'})
    todo_dao.delete(1)

    with pytest.raises(Exception):
        todo_dao.get(1)
