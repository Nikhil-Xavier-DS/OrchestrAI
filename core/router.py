def route_task(state):
    task = state.get("task", "").lower()

    if "email" in task or "slack" in task:
        return "comms"
    elif "data" in task or "sql" in task:
        return "data"
    elif "deploy" in task or "repo" in task:
        return "dev"
    else:
        return "research"