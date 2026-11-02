from fastapi import FastAPI
from app.config import settings
from app.routers.system import router as system_router
from app.routers.services import router as services_router  # если роутер сервисов уже подключён
from app.routers.objects import router as objects_router
from app.routers.auth import router as auth_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    debug=settings.debug
)

app.include_router(system_router)
app.include_router(services_router)
app.include_router(objects_router)
app.include_router(auth_router)