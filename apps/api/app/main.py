from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.db.models

from app.api.analytics import router as analytics_router
from app.api.automation import router as automation_router
from app.api.printing import router as printing_router
from app.api.auth import router as auth_router
from app.api.bakeries import router as bakeries_router
from app.api.capacity import router as capacity_router
from app.api.customers import router as customers_router
from app.api.ember import router as ember_router
from app.api.forecast import router as forecast_router
from app.api.health import router as health_router
from app.api.inventory import router as inventory_router
from app.api.inventory_projections import router as inventory_projections_router
from app.api.recurring import router as recurring_router
from app.api.market import router as market_router
from app.api.orders import router as orders_router
from app.api.planner import router as planner_router
from app.api.products import router as products_router
from app.api.production_runs import router as production_runs_router
from app.api.recipes import router as recipes_router
from app.api.scheduling import router as scheduling_router
from app.api.shopping import router as shopping_router
from app.api.today import router as today_router
from app.api.users import router as users_router
from app.api.websocket import router as websocket_router
from app.core.config import settings
from app.middleware.errors import global_exception_handler


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(websocket_router)

app.include_router(health_router, prefix=settings.API_V1_PREFIX)
app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
app.include_router(users_router, prefix=settings.API_V1_PREFIX)
app.include_router(bakeries_router, prefix=settings.API_V1_PREFIX)
app.include_router(customers_router, prefix=settings.API_V1_PREFIX)
app.include_router(recipes_router, prefix=settings.API_V1_PREFIX)
app.include_router(production_runs_router, prefix=settings.API_V1_PREFIX)
app.include_router(orders_router, prefix=settings.API_V1_PREFIX)
app.include_router(products_router, prefix=settings.API_V1_PREFIX)
app.include_router(inventory_router, prefix=settings.API_V1_PREFIX)
app.include_router(inventory_projections_router, prefix=settings.API_V1_PREFIX)
app.include_router(recurring_router, prefix=settings.API_V1_PREFIX)
app.include_router(shopping_router, prefix=settings.API_V1_PREFIX)
app.include_router(scheduling_router, prefix=settings.API_V1_PREFIX)
app.include_router(ember_router, prefix=settings.API_V1_PREFIX)

app.include_router(capacity_router, prefix=settings.API_V1_PREFIX)
app.include_router(forecast_router, prefix=settings.API_V1_PREFIX)
app.include_router(planner_router, prefix=settings.API_V1_PREFIX)
app.include_router(today_router, prefix=settings.API_V1_PREFIX)
app.include_router(market_router, prefix=settings.API_V1_PREFIX)
app.include_router(analytics_router, prefix=settings.API_V1_PREFIX)
app.include_router(automation_router, prefix=settings.API_V1_PREFIX)
app.include_router(printing_router, prefix=settings.API_V1_PREFIX)


@app.get("/")
async def root():
    return {
        "message": "Crumbkeeper API running"
    }
