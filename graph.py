from langgraph.graph import StateGraph, END
from config import MAX_RETRIES
from nodes.guard import guard_node
from nodes.context import context_node
from nodes.generator import generator_node
from nodes.validator import validator_node
from nodes.corrector import corrector_node

def should_retry(state):
    if state["errors"] and state["retry_count"] < MAX_RETRIES:
        return "retry"
    return "end"

def build_graph():
    workflow = StateGraph(dict)

    workflow.add_node("guard", guard_node)
    workflow.add_node("context", context_node)
    workflow.add_node("generate", generator_node)
    workflow.add_node("validate", validator_node)
    workflow.add_node("correct", corrector_node)

    workflow.set_entry_point("guard")

    workflow.add_edge("guard", "context")
    workflow.add_edge("context", "generate")
    workflow.add_edge("generate", "validate")

    workflow.add_conditional_edges(
        "validate",
        should_retry,
        {"retry": "correct", "end": END}
    )

    workflow.add_edge("correct", "validate")

    return workflow.compile()