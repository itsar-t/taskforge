from pathlib import Path

from taskforge.services.tracker import Tracker
from taskforge.storage.json_repo import JsonTrackerRepo


def test_json_repo_roundtrip(tmp_path: Path):
    path = tmp_path / "tasks.json"
    repo = JsonTrackerRepo(path)

    tr = Tracker()
    t1 = tr.add_title("A")
    tr.add_title("B")
    tr.mark_done_by_id(t1.id)

    repo.save(tr)
    loaded = repo.load()

    assert len(loaded.all()) == 2
    assert len(loaded.done()) == 1
    assert len(loaded.pending()) == 1


def test_json_repo_load_missin_file_returns_empty_tracker(tmp_path: Path):
    path = tmp_path / "does_not_exist.json"
    repo = JsonTrackerRepo(path)

    loaded = repo.load()

    assert len(loaded.all()) == 0
