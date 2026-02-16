
from __future__ import annotations
from pathlib import Path
from uuid import UUID

import argparse

from taskforge.storage.json_repo import JsonTrackerRepo
from taskforge.services.tracker import Tracker


DATA_PATH = Path("data/tasks.json")

def _load_tracker() -> tuple[JsonTrackerRepo, Tracker]:
    repo = JsonTrackerRepo(DATA_PATH)
    tracker = repo.load()
    return repo, tracker
def _parse_task_id(tracker: Tracker, raw: str) -> UUID:
    raw = raw.strip()

    # Is it full UUID?

    try:
        return UUID(raw)
    except ValueError:
        pass

    # short id prefix (first 8 chars)
    matches = [t.id for t in tracker.all() if str(t.id).startswith(raw)]

    if len(matches) == 1:
        return matches[0]
    if len(matches) == 0:
        raise ValueError(f"--- No task matches id prefix: {raw!r} ---")
    raise ValueError(f"--- Ambiguous id prefix: {raw!r} (matches {len(matches)}) ---")

def cmd_list(args: argparse.Namespace) -> None:
    _, tracker = _load_tracker()

    if args.isdone:
        tasks = tracker.done() 
    elif args.ispending:
        tasks = tracker.pending()
    else:
        tasks = tracker.all()

    if not tasks:
        print("--- No tasks yet ---")
        return
    
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t}")

def cmd_add(args: argparse.Namespace) -> None:
    repo, tracker = _load_tracker()
    task = tracker.add_title(args.title)
    repo.save(tracker)
    print(f"--- Added: {task} ---")


def cmd_done(args: argparse.Namespace) -> None:
    repo, tracker = _load_tracker()
    task_id = _parse_task_id(tracker, args.id)
    task = tracker.mark_done_by_id(task_id)
    repo.save(tracker)
    print(f"--- Done: {task} ---") 

def cmd_undone(args: argparse.Namespace) -> None:
    repo, tracker = _load_tracker()
    task_id = _parse_task_id(tracker, args.id)
    task = tracker.mark_undone_by_id(task_id)
    repo.save(tracker)
    print(f"--- Undone: {task} ---") 

def cmd_switch_done(args: argparse.Namespace) -> None:
    repo, tracker = _load_tracker()
    task_id = _parse_task_id(tracker, args.id)
    task = tracker.switch_done_by_id(task_id)
    repo.save(tracker)
    print(f"--- Switch: {task} ---") 

def cmd_rm(args: argparse.Namespace) -> None:
    repo, tracker = _load_tracker()
    task_id = _parse_task_id(tracker, args.id)
    task = tracker.remove_by_id(task_id)
    repo.save(tracker)
    print(f"--- Removed: {task} ---")
    
    
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="taskforge", description="Taskforge CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List all tasks")
    p_list.add_argument("--isdone", action="store_true", help="List tasks which is done")
    p_list.add_argument("--ispending", action="store_true", help="List tasks which is pending")
    p_list.set_defaults(func=cmd_list)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title", help="Task title (Note: title \"the title\")")
    p_add.set_defaults(func=cmd_add)

    p_done = sub.add_parser("done", help="Mark task done by ID (full or prefix)")
    p_done.add_argument("id", help="Task ID (full UUID or prefix)")
    p_done.set_defaults(func=cmd_done)

    p_undone = sub.add_parser("undone", help="Mark task undone by ID (full or prefix)")
    p_undone.add_argument("id", help="Task ID (full UUID or prefix)")
    p_undone.set_defaults(func=cmd_undone)

    p_done = sub.add_parser("switch", help="Switch task done/undone by ID (full or prefix)")
    p_done.add_argument("id", help="Task ID (full UUID or prefix)")
    p_done.set_defaults(func=cmd_switch_done)

    p_rm = sub.add_parser("rm", help="Remove task by ID (full or prefix)")
    p_rm.add_argument("id", help="Task ID (full UUID or prefix)")
    p_rm.set_defaults(func=cmd_rm)


    return p

def run() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    
    
    
    