from fastapi import FastAPI
from app.config import settings
from app.routers.system import router as system_router
from app.routers.services import router as services_router  # если роутер сервисов уже подключён

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    debug=settings.debug
)

app.include_router(system_router)
app.include_router(services_router)