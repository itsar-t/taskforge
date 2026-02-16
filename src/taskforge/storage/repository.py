from __future__ import annotations

from abc import ABC, abstractmethod

from taskforge.services.tracker import Tracker

class TrackerRespository(ABC):
    @abstractmethod
    def load(self) -> Tracker:
        raise NotImplementedError
    
    @abstractmethod
    def save(self, tracker: Tracker) -> None:
        raise NotImplementedError