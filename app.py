from app.main import app
from app.config.settings import get_settings

settings = get_settings()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
