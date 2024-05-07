from fastapi import FastAPI
from datetime import datetime,timezone

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/timenow")
async def timenow():
    now_utc = datetime.now(timezone.utc)
    return {"UTC": now_utc}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

