from langchain_groq import ChatGroq
from prompts import build_generation_prompt
from config import MODEL_NAME
import json

llm = ChatGroq(model=MODEL_NAME, temperature=0)

def generator_node(state):
    prompt = build_generation_prompt(
        state["user_prompt"],
        state["design_system"],
        state.get("previous_component")
    )

    response = llm.invoke(prompt)

    try:
        component = json.loads(response.content)
    except:
        component = {}

    return {**state, "component": component, "errors": []}