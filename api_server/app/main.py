from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg":"docker test ok_1"}