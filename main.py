from dotenv import load_dotenv
load_dotenv()

import os
import json
from graph import build_graph
from export import export_component
from memory import ComponentMemory

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("Missing GROQ_API_KEY in environment.")

def load_design_system():
    with open("design_system.json") as f:
        return json.load(f)

if __name__ == "__main__":
    app = build_graph()
    memory = ComponentMemory()

    while True:
        user_prompt = input("Describe component (or type 'exit'): ")
        if user_prompt.lower() == "exit":
            break

        state = {
            "user_prompt": user_prompt,
            "design_system": load_design_system(),
            "component": {},
            "errors": [],
            "retry_count": 0,
            "memory": memory
        }

        final_state = app.invoke(state)

        if final_state["errors"]:
            print("Validation failed:", final_state["errors"])
        else:
            print("Component generated successfully.")
            memory.update(final_state["component"])
            export_component(final_state["component"])
            print("Exported to generated_component/")