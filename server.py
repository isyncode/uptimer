import requests
import time
from fastapi import FastAPI
import asyncio
import os
import aiohttp
from dotenv import load_dotenv
import uvicorn
load_dotenv()

app = FastAPI()

start = False

@app.get("/")
async def main():
    async with aiohttp.ClientSession() as session:
        request = await session.get(os.environ.get("URL"))
        print(request.status)

    return "Program Start"

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0")
