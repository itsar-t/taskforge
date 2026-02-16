import pytest

from taskforge.services.tracker import Tracker
from taskforge.domain.task import Task

def test_add_adds_task_to_tracker():
    tr = Tracker()
    task = Task("Test")
                
    tr.add(task)

    with pytest.raises(TypeError):
        tr.add("")

    all_tasks = tr.all()

    assert len(all_tasks) == 1
    assert all_tasks[0] is task

def test_add_and_mark_done_by_id():
    tr = Tracker()
    t = tr.add_title("A")
    tr.add_title("B")

    tr.mark_done_by_id(t.id)

    assert tr.get_by_id(t.id).done is True
    assert len(tr.pending()) == 1
    assert len (tr.done()) == 1

def test_add_and_switch_done_by_id():
    tr = Tracker()
    t = tr.add_title("A")
    tr.add_title("B")

    tr.switch_done_by_id(t.id)

    assert tr.get_by_id(t.id).done is True
    assert len(tr.pending()) == 1
    assert len (tr.done()) == 1

def test_add_and_mark_undone_by_id():
    tr = Tracker()
    t = tr.add_title("A")
    tr.add_title("B")
   

    tr.mark_done_by_id(t.id)
    
    assert tr.get_by_id(t.id).done is True
    assert len(tr.pending()) == 1
    assert len (tr.done()) == 1

    tr.mark_undone_by_id(t.id)

    assert tr.get_by_id(t.id).done is False
    assert len(tr.pending()) == 2
    assert len (tr.done()) == 0
    
def test_remove_by_id_removes_correct_task():
    tr = Tracker()
    t1 = tr.add_title("A")
    t2 = tr.add_title("B")

    removed = tr.remove_by_id(t1.id)

    assert removed.id == t1.id
    assert tr.get_by_id(t2.id).title == "B"

    with pytest.raises(KeyError):
        tr.get_by_id(t1.id)