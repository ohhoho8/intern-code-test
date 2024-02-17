import asyncio
import random
import time
from uuid import uuid4
from redis import Redis

redis_conn = Redis(host='test_redis', port=6379)

async def generate_objects():
    for _ in range(50):
        key = str(uuid4())
        value = int(time.time())
        redis_conn.setex(key, 10, value)
        await asyncio.sleep(random.uniform(0.1, 1))

async def delete_random_objects():
    keys = redis_conn.keys()
    num_to_delete = random.randint(0, min(10, len(keys)))
    keys_to_delete = random.sample(keys, num_to_delete)
    if keys_to_delete:
        redis_conn.delete(*keys_to_delete)

def count_objects():
    return len(redis_conn.keys())

def get_objects(limit: int):
    keys = redis_conn.keys()
    keys_to_return = random.sample(keys, min(limit, len(keys)))
    return {key.decode(): redis_conn.get(key).decode() for key in keys_to_return}

async def runTask():
    await generate_objects()
    await delete_random_objects()
    num_objects = count_objects()
    objects = get_objects(num_objects)
    print(objects)

if __name__ == "__main__":
    asyncio.run(runTask())
