TOOLS = ["list_pulls", "summarize"]
WRITES = ("merge", "delete", "force",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = [p["title"] for p in payload.get("pulls") or [] if p.get("state") == "open"]
    return {"refused": False, "tools": TOOLS, "open": result, "wrote": False, "applied": False}
