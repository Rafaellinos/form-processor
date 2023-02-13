from fastapi import FastAPI
from app.config.settings import get_settings
from app.database.database import Database
from app.routes.router import router

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    root_path=settings.API_PREFIX,
    debug=settings.DEBUG,
    port=settings.PORT,
)


@app.on_event("startup")
async def startup():
    await Database.connect()

app.include_router(router, prefix=settings.API_PREFIX)
