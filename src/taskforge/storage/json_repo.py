from __future__ import annotations

import json
from pathlib import Path

from taskforge.services.tracker import Tracker
from taskforge.storage.repository import TrackerRespository

class JsonTrackerRepo(TrackerRespository):
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> Tracker:
        if not self.path.exists():
            return Tracker()
        
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        return Tracker.from_dict(data)
    
    def save(self, tracker: Tracker) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

        data = tracker.to_dict()
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)