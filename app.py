from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.urls import RoutesConfiguration

app = FastAPI(
    version="0.0.1",
    debug=True,
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "x-user-uuid"],
)

routes_config = RoutesConfiguration(app)
routes_config.configure()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug"
    )