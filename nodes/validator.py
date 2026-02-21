from validators.schema import validate_schema
from validators.ts_ast import validate_typescript_structure
from validators.design_tokens import validate_tokens

def validator_node(state):
    component = state["component"]

    errors = []
    errors += validate_schema(component)
    errors += validate_typescript_structure(component)
    errors += validate_tokens(component, state["design_system"])

    return {**state, "errors": errors}