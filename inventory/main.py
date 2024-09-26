from redis-om import get_redis_connection, HashModel
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.config['CORS_ORIGINS'] = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=app.config['CORS_ORIGINS'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host="localhost",
    port=6379,
    decode_responses=True
)
class Products(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


