from __future__ import annotations
from typing import Iterable, List, Optional, Any, Dict, Self
from uuid import UUID
from taskforge.domain.task import Task

class Tracker:
    """
    Application/service layer.
    Owns a collection of tasks and provides operations on them

    Note: No file IO, no printing. Pure logic.
    """

    def __init__(self, tasks: Optional[Iterable[Task]] = None) -> None:
        self._tasks: List[Task] = list(tasks) if tasks else []

    def add(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise TypeError("Expected Task instance")
        self._tasks.append(task)
    
    def add_title(self, title: str) -> Task:
        task = Task(title)
        self.add(task)
        return task
    
    def get_by_id(self, task_id: UUID) -> Task:
        for t in self._tasks:
            if t.id == task_id:
                return t
        raise KeyError(f"--- No task with ID {task_id}")
    
    def all(self) -> List[Task]:
        return list(self._tasks)
    
    def pending(self) -> List[Task]:
        return [t for t in self._tasks if not t.done]

    def done(self) -> List[Task]:
        return [t for t in self._tasks if t.done]
    
    def mark_done_by_index(self, index: int) -> Task:
        task = self._tasks[index]
        task.mark_done()
        return task
    
    def mark_done_by_id(self, task_id: UUID) -> Task:
        task = self.get_by_id(task_id)
        task.mark_done()
        return task
    
    def mark_undone_by_id(self, task_id: UUID) -> Task:
        task = self.get_by_id(task_id)
        task.mark_undone()
        return task
    
    def switch_done_by_id(self, task_id: UUID) -> Task:
        task = self.get_by_id(task_id)
        task.switch_done()
        return task
    
    
    def remove_by_index(self, index: int) -> Task:
        return self._tasks.pop(index)
    
    def remove_by_id(self, task_id: UUID) -> Task:
        for i, t in enumerate(self._tasks):
            if t.id == task_id:
                return self._tasks.pop(i)
        raise KeyError(f"--- No task with ID {task_id} ---")

    def __len__(self) -> int:
        return len(self._tasks)
    
    def to_dict(self) -> Dict[str, Any]:
        return {"tasks": [t.to_dict() for t in self._tasks]}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        tasks_data = data.get("tasks", [])
        tasks = [Task.from_dict(d) for d in tasks_data]
        return cls(tasks=tasks)