# uvicorn main:app --reload --host 0.0.0.0

from typing import Optional

from fastapi import FastAPI
import importlib

from enum import Enum

class enumPsutilCPU(str, Enum):
    cpu_times = "cpu_times"
    cpu_percent = "cpu_percent"
    cpu_times_percent = "cpu_times_percent"
    cpu_count = "cpu_count"
    cpu_stats = "cpu_stats"
    cpu_freq = "cpu_freq"
    getloadavg = "getloadavg"

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/built-in/psutil/CPU/{_func}")
def psutil_cpu(_func: enumPsutilCPU, 
            percpu: Optional[bool] = None, 
            interval: Optional[int] = None,
            logical: Optional[bool] = None,
            ):
    psutil = importlib.import_module('psutil')

    
    return "Wrong input"
