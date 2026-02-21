from langchain_groq import ChatGroq
from config import MODEL_NAME
import json

llm = ChatGroq(model=MODEL_NAME, temperature=0)

def critic_node(state):
    review_prompt = f"""
You are a senior Angular code reviewer.

Review the following Angular component JSON.

STRICT:
Return ONLY JSON in this format:
{{
  "valid": true/false,
  "issues": ["issue1", "issue2"]
}}

Check:
- Angular structure validity
- Proper decorator usage
- Logical mistakes
- Design token adherence
- Missing module requirements (e.g. FormsModule for ngModel)

Component:
{json.dumps(state["component"], indent=2)}
"""

    response = llm.invoke(review_prompt)

    try:
        result = json.loads(response.content)
    except:
        return {**state, "errors": ["Critic parsing failed"]}

    if not result.get("valid", False):
        return {**state, "errors": result.get("issues", ["Critic rejected component"])}

    return state