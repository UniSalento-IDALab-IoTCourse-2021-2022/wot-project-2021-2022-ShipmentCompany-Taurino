from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from AI import *
import json

app = FastAPI()


class Courier(BaseModel):
    id: Optional[str] = None
    RPE: int

class Product(BaseModel):
    id: Optional[str] = None
    volume: float
    weight: float
    minT: int
    maxT: int

class Truck(BaseModel):
    id: Optional[str] = None
    t_est: int
    t_cont: int
    t_cell: int
    dist: float


with open('couriers.json', 'r') as f:
    couriers = json.load(f)

with open('trucks.json', 'r') as f:
    trucks = json.load(f)


@app.put('/interrogateAI', status_code=200)
def get_suggest(product: Product):
    new_product = {
        "id": product.id,
        "volume": product.volume,
        "weight": product.weight,
        "minT": product.minT,
        "maxT": product.maxT
    }
    sugg = process(new_product)
    print('AI suggestion:')
    print(sugg)
    feedback = {
        "courier": sugg[0][0],
        "truck": sugg[0][1]
    }
    return feedback['courier'], feedback['truck']


@app.put("/updateCourier", status_code=204)
def update_courier(courier: Courier):
    new_courier = {
        "id": courier.id,
        "RPE": courier.RPE
    }
    courier_list = [c for c in couriers if c['id'] == courier.id]
    if len(courier_list) > 0:
        couriers.remove(courier_list[0])
        position = int(courier.id.lstrip('courier_')) - 1
        couriers.insert(position, new_courier)
        with open('couriers.json', 'w') as f:
            json.dump(couriers, f)
        return new_courier
    else:
        raise HTTPException(status_code=404,detail=f"Courier with ID {courier.id} does not exist!")


@app.put("/updateTruck", status_code=204)
def update_truck(truck: Truck):
    new_truck = {
        "id": truck.id,
        "t_est": truck.t_est,
        "t_cont": truck.t_cont,
        "t_cell": truck.t_cell,
        "dist": truck.dist
    }
    truck_list = [t for t in trucks if t['id'] == truck.id]
    if len(truck_list) > 0:
        trucks.remove(truck_list[0])
        position = int(truck.id.lstrip('truck_')) - 1
        trucks.insert(position, new_truck)
        with open('trucks.json', 'w') as f:
            json.dump(trucks, f)
        return new_truck
    else:
        raise HTTPException(status_code=404, detail=f"Truck with ID {truck.id} does not exist!")