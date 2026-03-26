from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "MedPulse API Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    return {
        "level": random.choice(["Low", "Medium", "High"]),
        "confidence": round(random.uniform(70, 95), 2),
        "features": {
            "tremor_index": 0.82,
            "stroke_variance": 0.74,
            "edge_density": 0.61
        },
        "importance": {
            "tremor_index": 0.4,
            "stroke_variance": 0.35,
            "edge_density": 0.25
        }
    }
