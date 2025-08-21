from fastapi import FastAPI
from task2.server.router import router
app = FastAPI()
app.include_router(router)

