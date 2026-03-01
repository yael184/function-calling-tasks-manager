import json
import os
import datetime

DB_FILE = "tasks.json"

def _load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_db(tasks):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def get_tasks(status: str = None, category: str = None):
    tasks = _load_db()
    if status:
        tasks = [t for t in tasks if t['status'].lower() == status.lower()]
    if category:
        tasks = [t for t in tasks if t['category'].lower() == category.lower()]
    return tasks

def add_task(title: str, notes: str = "", category: str = "General", due_date: str = None):
    tasks = _load_db()
    new_id = max([t['id'] for t in tasks], default=100) + 1
    entry = {
        "id": new_id,
        "title": title,
        "notes": notes,
        "category": category,
        "date": due_date or str(datetime.date.today()),
        "status": "pending"
    }
    tasks.append(entry)
    _save_db(tasks)
    return entry

def remove_task(task_id: int):
    tasks = _load_db()
    initial_len = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    _save_db(tasks)
    return {"success": len(tasks) < initial_len}