from __future__ import annotations
from typing import Self, Any, Dict
from uuid import UUID, uuid4


class Task:
    """
    Represents a single task in the system.

    Invariant:
        - title must never be empty
    """

    def __init__(
        self, title: str, done: bool = False, task_id: UUID | None = None
    ) -> None:
        self.id = task_id or uuid4()
        self.title = title  # Will go through setter
        self.done = done

    # ----------------------------
    # Property (validation layer)
    # ----------------------------

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("Task title cannot be empty")
        self._title = value

    # ----------------------------
    # Behavior
    # ----------------------------

    def mark_done(self) -> None:
        self.done = True

    def mark_undone(self) -> None:
        self.done = False

    def switch_done(self) -> None:
        self.done = not self.done

    # ----------------------------
    # Factory
    # ----------------------------

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": str(self.id),
            "title": self.title,
            "done": self.done,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(
            title=str(data["title"]),
            done=bool(data.get("done", False)),
            task_id=UUID(str(data["id"])) if "id" in data else None,
        )

    @classmethod
    def from_text(cls, text: str) -> Self:
        """
        :param cls: The class
        :param text: "Done|Buy milk" or "Undone|Study"
        :type text: str
        :return: New class object
        :rtype: Self
        """
        status, title = text.split("|", 1)
        done = status == "Done"
        return cls(title=title, done=done)

    # ----------------------------
    # Representation
    # ----------------------------

    def __str__(self) -> str:
        status = "Done" if self.done else "Undone"
        short_id = str(self.id)[:8]
        return f"[{status}] ({short_id}) {self.title}"

    def __repr__(self) -> str:
        return (
            f"Task (id={str(self.id)!r}), (title={self.title!r}), (done={self.done!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash((self.title, self.done))
