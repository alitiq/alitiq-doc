""" simple server """
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]
# Define the FastAPI server
app = FastAPI(middleware=middleware)

app.mount("/", StaticFiles(directory="/app/site"), name="docs")