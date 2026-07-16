from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Har baar jab dashboard request karega, ye check karega
@app.get("/get_status")
def get_status():
    status = {}
    routers = {"Router site1": "192.168.1.1", "Router headquater": "192.168.1.2", "Router site2": "192.168.1.3"}
    for name, ip in routers.items():
      response = os.system(f"ping -n 1 -w 1000 {ip} > nul")
      status[name] = "UP" if response == 0 else "DOWN"
    return status