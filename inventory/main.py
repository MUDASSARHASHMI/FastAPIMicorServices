from redis-om import get_redis_connection, HashModel
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.config['CORS_ORIGINS'] = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host="redis-17385.c212.ap-south-1-1.ec2.redns.redis-cloud.com",
    port=17385,
    password="1EiKRHN7h15Ipyn6o85VHPibG9atymxd",
    decode_responses=True
)
class Products(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get('/products')
def all():
    return [format(pk) for pk in Products.all_pks()]
def format(pk=str):
    products = Products.get(pk)
    return {
        "id": pk,
        "name": products.name,
        "price": products.price,
        "quantity": products.quantity
    }

@app.post('/products')
def create(product:Products):
    return product.save()