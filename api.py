from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from graph import build_graph
from memory import ComponentMemory
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
graph = build_graph()
memory = ComponentMemory()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: PromptRequest):
    state = {
        "user_prompt": req.prompt,
        "design_system": json.load(open("design_system.json")),
        "component": {},
        "errors": [],
        "retry_count": 0,
        "memory": memory
    }

    result = graph.invoke(state)
    return result["component"]