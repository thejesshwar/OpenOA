from fastapi import FastAPI
from pydantic import BaseModel
import openoa
import pandas as pd

app = FastAPI()

# This class defines the data we expect from the frontend
class AnalysisRequest(BaseModel):
    site_name: str
    capacity_mw: float

@app.get("/")
def home():
    return {
        "message": "OpenOA API is Live", 
        "library_version": openoa.__version__,
        "status": "Ready for Analysis"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/simulate_analysis")
def simulate_analysis(request: AnalysisRequest):
    # In a real scenario, you would load data here using openoa.PlantData()
    return {
        "site": request.site_name,
        "capacity": request.capacity_mw,
        "analysis_result": "Optimization Complete",
        "predicted_aep_gwh": request.capacity_mw * 8.76 * 0.35, # Simple formula for demo
        "status": "Success"
    }