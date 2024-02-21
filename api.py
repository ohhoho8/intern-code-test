#api.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from worker import runTask
from typing import Dict

app = FastAPI()

class WorkerResponse(BaseModel):
    message: str
    objects: Dict[str, str]

redis_conn = Redis(host='redis_queue', port=6379)
q = Queue('my_queue', connection=redis_conn)

@app.get("/run-worker-task", response_model=WorkerResponse)
async def trigger_worker_task(background_tasks: BackgroundTasks):
    objects = await runTask(redis_conn)
    return {"message": "Worker task started in the background.", "objects": objects}

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'hello': 'world'}