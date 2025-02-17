from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from CRUD.authen import auth
from CRUD.saved_articles import saved_articles_router
import uvicorn
import colorama

colorama.init()
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://personalarticlebookmark.netlify.app",
]

app = FastAPI(docs_url="/api/docs", openapi_url="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth, prefix="/api")
app.include_router(saved_articles_router, prefix="/api")
