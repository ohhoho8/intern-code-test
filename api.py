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

@app.get("/", response_model=WorkerResponse)
async def trigger_worker_task(background_tasks: BackgroundTasks):
    """
    Worker task를 실행하여 Redis에 객체를 생성하고 삭제합니다.

    Parameters:
    - background_tasks (BackgroundTasks): 백그라운드 작업을 처리하기 위한 FastAPI의 BackgroundTasks 객체입니다.

    Returns:
    - dict: 실행된 worker task에 대한 메시지와 생성된 객체들의 정보가 포함된 딕셔너리입니다.
    """
    objects = await runTask(redis_conn)
    return {"message": "Worker task started in the background.", "objects": objects}

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'hello': 'world'}