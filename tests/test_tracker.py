import pytest

from taskforge.services.tracker import Tracker
from taskforge.domain.task import Task
from uuid import uuid4

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

    assert tr.get_by_id(t.id).done
    assert len(tr.pending()) == 1
    assert len(tr.done()) == 1


def test_add_and_switch_done_by_id():
    tr = Tracker()
    t = tr.add_title("A")
    # First switch done -> True
    tr.switch_done_by_id(t.id)
    assert tr.get_by_id(t.id).done
    assert len(tr.done()) == 1

    # Second switch done -> False
    tr.switch_done_by_id(t.id)
    assert not tr.get_by_id(t.id).done
    assert len(tr.done()) == 0
    

   


def test_add_and_mark_undone_by_id():
    tr = Tracker()
    t = tr.add_title("A")
    tr.add_title("B")

    tr.mark_done_by_id(t.id)

    assert tr.get_by_id(t.id).done
    assert len(tr.pending()) == 1
    assert len(tr.done()) == 1

    tr.mark_undone_by_id(t.id)

    assert not tr.get_by_id(t.id).done
    assert len(tr.pending()) == 2
    assert len(tr.done()) == 0


def test_remove_by_id_removes_correct_task():
    tr = Tracker()
    t1 = tr.add_title("A")
   

    removed = tr.remove_by_id(t1.id)

    assert removed == t1
    assert len(tr) == 0

    with pytest.raises(KeyError):
        tr.get_by_id(t1.id)

def test_remove_by_id_raises_for_missing_id():
    tr = Tracker()
    tr.add_title("A")

    with pytest.raises(KeyError):
        tr.remove_by_id(uuid4())