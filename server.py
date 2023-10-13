import requests
import time
from fastapi import FastAPI
import asyncio
import os
import aiohttp
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

start = False

@app.get("/")
async def main():

    if not start:
        start = True
        asyncio.create_task(run())

    return "Program Start"


async def run():
    while True:
        async with aiohttp.ClientSession() as session:
            request = await session.get(os.environ.get("URL"))
            print(request.status)
            time.sleep(30)
