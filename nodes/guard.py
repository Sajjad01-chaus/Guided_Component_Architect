def guard_node(state):
    blocked_patterns = [
        "ignore previous",
        "system prompt",
        "delete design system",
        "bypass validation"
    ]

    lowered = state["user_prompt"].lower()

    for pattern in blocked_patterns:
        if pattern in lowered:
            raise ValueError("Potential prompt injection detected.")

    return state