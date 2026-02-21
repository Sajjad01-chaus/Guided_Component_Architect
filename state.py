from typing import TypedDict, List, Dict


class ComponentState(TypedDict):
    user_prompt: str
    design_system: Dict
    component: Dict   # structured JSON output
    errors: List[str]
    retry_count: int