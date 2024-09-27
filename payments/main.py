from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host="redis-17385.c212.ap-south-1-1.ec2.redns.redis-cloud.com",
    port=17385,
    password="1EiKRHN7h15Ipyn6o85VHPibG9atymxd",
    decode_responses=True
)

