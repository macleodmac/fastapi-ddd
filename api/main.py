from api.routers.event import router
from fastapi import FastAPI
import uvicorn


def app():
    app = FastAPI()
    app.include_router(router)

    return app


if __name__ == "__main__":
    app = app()

    uvicorn.run(app, host="localhost", port=8000)
