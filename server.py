from fastapi import FastAPI
from My_Project.main import pixyData
pixy = pixyData()
app = FastAPI()

@app.get("/")
async def cords():
    return  pixy.json