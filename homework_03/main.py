from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/ping/")
def ping():
    return {"message": "pong"}
