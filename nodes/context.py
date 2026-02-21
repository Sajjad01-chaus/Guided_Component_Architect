def context_node(state):
    memory = state["memory"]
    previous = memory.get()
    if previous:
        state["previous_component"] = previous
    else:
        state["previous_component"] = None
    return state