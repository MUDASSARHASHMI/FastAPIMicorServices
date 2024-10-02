from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request
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

class Orders(HashModel):
    product: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, refunded

    class Meta:
        database = redis
    
@app.get('/orders/{pk}')
async def get_order(pk: str):
    return Orders.get(pk)

@app.post('/orders')
async def create_order(order: Orders):
    order.save()
    return order.to_dict()
@app.put('/orders/{pk}')
async def update_order(pk: str, order: Orders):
    order.pk = pk
    order.save()
    return order

@app.post('/orders')
