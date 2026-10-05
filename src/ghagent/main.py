from ghagent.ops import router as ops_router
from fastapi import FastAPI, HTTPException
from ghagent.agent import InputError, run

app = FastAPI()
app.include_router(ops_router, prefix="/v1")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/agent/run")
def post_run(body: dict):
    try:
        return run(body.get("goal"), body.get("payload") or body)
    except InputError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
