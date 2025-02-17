from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to ProManage Backend"}

@app.get("/health")
async def health_check():
    return {"status": "OK"} 