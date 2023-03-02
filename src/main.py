from fastapi import FastAPI
from src.config.settings import get_settings
from src.database.database import Database
from src.routes.router import router

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


@app.get(app.root_path + "/openapi.json")
def custom_swagger_ui_html():
    return app.openapi()


app.include_router(router, prefix=settings.API_PREFIX)

