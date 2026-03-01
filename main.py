from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from agent_service import agent
from todo_service import get_tasks
import os

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(query: Query):
    reply = agent(query.message)
    return {"reply": reply}

@app.get("/tasks")
async def tasks_endpoint():
    return get_tasks()

# הנתיב הראשי שמגיש את דף ה-HTML
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)