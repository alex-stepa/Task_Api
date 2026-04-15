from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", description="Jednoduché REST API pro správu úkolů")

# Úložiště úkolů v paměti
tasks: list[dict] = []
next_id  = 1

# --- Modely ---

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None


# --- Pomocná funkce ---

def find_task(task_id: int) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Úkol s ID {task_id} nebyl nalezen")


# --- Endpointy ---

@app.get("/tasks", summary="Získat všechny úkoly")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", summary="Získat úkol podle ID")
def get_task(task_id: int):
    return find_task(task_id)


@app.post("/tasks", status_code=201, summary="Vytvořit nový úkol")
def create_task(task: TaskCreate):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.put("/tasks/{task_id}", summary="Upravit úkol")
def update_task(task_id: int, update: TaskUpdate):
    task = find_task(task_id)
    if update.title is not None:
        task["title"] = update.title
    if update.description is not None:
        task["description"] = update.description
    if update.done is not None:
        task["done"] = update.done
    return task


@app.delete("/tasks/{task_id}", summary="Smazat úkol")
def delete_task(task_id: int):
    task = find_task(task_id)
    tasks.remove(task)
    return {"message": f"Úkol '{task['title']}' byl smazán"}
