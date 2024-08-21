from fastapi import FastAPI
from app.routers import api

app = FastAPI()

app.include_router(router=api.router, prefix="/api")


@app.get("/")
async def read_root():
    return {"Health_check": "Ok"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
