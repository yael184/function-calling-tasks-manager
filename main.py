from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import agent_service
import todo_service

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/tasks")
async def list_tasks():
    return todo_service.get_tasks()

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    reply = agent_service.agent(req.message)
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)