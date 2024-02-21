#api.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from worker import runTask

app = FastAPI()

redis_conn = Redis(host='redis_queue', port=6379)
q = Queue('my_queue', connection=redis_conn)

@app.get("/run-worker-task")
async def trigger_worker_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(runTask, redis_conn)
    return {"message": "Worker task started in the background."}

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'hello': 'world'}
