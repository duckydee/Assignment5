from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, sandwiches, resources, recipes
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Order Endpoints
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

#Sandwich Endpoints
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_order(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_orders(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get("/sandwiches/{sandwiches_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = sandwiches.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/sandwich/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_order(order_id: int, order: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    order_db = sandwiches.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.update(db=db, sandwich=order, order_id=order_id)


@app.delete("/sandwich/{sandwich_id}", tags=["Sandwiches"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = sandwiches.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.delete(db=db, order_id=order_id)

#Resources Endpoints
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_order(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_orders(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = resources.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_order(order_id: int, order: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    order_db = resources.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.update(db=db, resource=order, order_id=order_id)


@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = resources.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.delete(db=db, order_id=order_id)

#Recipe Endpoints
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_order(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)


@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_orders(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = recipes.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_order(order_id: int, order: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    order_db = recipes.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.update(db=db, recipe=order, order_id=order_id)


@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = recipes.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.delete(db=db, order_id=order_id)

#Order Detail Endpoints
#OrderDetail Endpoints
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["Order Details"])
def create_order(order_detail: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, order_detail=order_detail)


@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["Order Details"])
def read_orders(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/order_details/{order_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = recipes.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/order_details/{order_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def update_one_order(order_id: int, order: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    order_db = recipes.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.update(db=db, order_detail=order, order_id=order_id)


@app.delete("/order_details/{order_id}", tags=["Order Details"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = recipes.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.delete(db=db, order_id=order_id)


