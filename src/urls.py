from fastapi import FastAPI
from src.routes import router
from fastapi.responses import JSONResponse


class RoutesConfiguration:
    def __init__(self, app: FastAPI):
        self.app = app
    
    def configure(self):
        self.app.include_router(router, prefix="/api/v1")