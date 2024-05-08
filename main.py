from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from datetime import datetime,timezone

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/timenow")
async def timenow():
    now_utc = datetime.now(timezone.utc)
    return {"UTC": now_utc}

@app.get("/test-file")
async def file_download():
    def iterfile():
        with open("./test.txt", mode='rb') as f:
            yield from f
    
    return StreamingResponse(iterfile(), media_type='text/plain')


@app.get("/test-video")
async def file_download():
    def iterfile():
        with open("./flower.webm", mode='rb') as f:
            yield from f
    
    return StreamingResponse(iterfile(), media_type='video/webm')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)