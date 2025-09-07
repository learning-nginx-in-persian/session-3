from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return PlainTextResponse("Hello from the backend (FastAPI app)")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
