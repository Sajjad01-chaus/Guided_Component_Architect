from langchain_groq import ChatGroq
from config import MODEL_NAME
import json

llm = ChatGroq(model=MODEL_NAME, temperature=0)

def corrector_node(state):
    correction_prompt = f"""
Fix the Angular component JSON below.

Errors:
{state["errors"]}

Return ONLY valid JSON:
{{
  "typescript": "...",
  "html": "...",
  "css": "..."
}}

Component:
{json.dumps(state["component"], indent=2)}
"""

    response = llm.invoke(correction_prompt)

    try:
        component = json.loads(response.content)
    except:
        component = state["component"]

    return {
        **state,
        "component": component,
        "retry_count": state["retry_count"] + 1
    }