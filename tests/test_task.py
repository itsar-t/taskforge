import pytest
from uuid import UUID

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

def test_to_dict_roundtrip_keeps_id():
    original = Task("Roundtrip", done=True)
    data = original.to_dict()
    loaded = Task.from_dict(data)

    assert loaded.id == original.id
    assert loaded.title == original.title
    assert loaded.done == original.done
    
