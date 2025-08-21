import uvicorn
from fastapi import FastAPI
from task2.server.router import router
if __name__ == "__main__":
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(
        app=app,
        host='localhost',
        port=8000,
    )