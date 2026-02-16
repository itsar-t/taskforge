import pytest
from uuid import UUID
from uuid import uuid4

from taskforge.domain.task import Task


def test_title_is_trimmed_and_cannot_be_empty():
    t = Task("  Learn OOP  ")
    assert t.title == "Learn OOP"

    with pytest.raises(ValueError):
        Task("   ")


def test_from_dict_and_generates_id_if_missing():
    data = {"title": "Test ID task", "done": False}

    t = Task.from_dict(data)

    assert isinstance(t.id, UUID)
    assert t.title == "Test ID task"
    assert t.done is False

def test_tasks_with_same_id_are_equal():

    t1 = Task("Learn OOP")
    t2 = Task("Different title", task_id=t1.id)
    t3 = Task("Another task")

    # Same ID → equal
    assert t1 == t2
    assert t3 == t3
    
    # Different ID → not equal
    assert t1 != t3
    assert t2 != t3
    

def test_to_dict_roundtrip_keeps_id():
    original = Task("Roundtrip", done=True)
    data = original.to_dict()
    loaded = Task.from_dict(data)

    assert loaded.id == original.id
    assert loaded.title == original.title
    assert loaded.done == original.done

def test_task_from_text_done():
    t = Task.from_text("Done|Buy milk")
    assert t.done
    assert t.title == "Buy milk"

def test_task_from_text_undone():
    t = Task.from_text("Undone|Study")

    assert not t.done
    assert t.title == "Study"
