from fastapi import FastAPI
from database import Base, engine
from routes import customer_routes, product_routes, transaction_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShopperSmart API")

app.include_router(customer_routes.router)
app.include_router(product_routes.router)
app.include_router(transaction_routes.router)
