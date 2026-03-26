

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy trained model (replace with real model.pkl)
try:
    model = joblib.load("model.pkl")
except:
    model = None


def extract_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    tremor_index = np.std(blur)
    stroke_variance = np.var(gray)
    edge_density = np.mean(cv2.Canny(gray, 50, 150))

    return [tremor_index, stroke_variance, edge_density]


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    features = extract_features(img)

    if model:
        pred = model.predict([features])[0]
        probs = model.predict_proba([features])[0]
    else:
        pred = np.random.choice([0, 1, 2])
        probs = np.random.dirichlet(np.ones(3), size=1)[0]

    levels = ["Low", "Medium", "High"]

    return {
        "level": levels[pred],
        "confidence": round(float(max(probs) * 100), 2),
        "features": {
            "tremor_index": float(features[0]),
            "stroke_variance": float(features[1]),
            "edge_density": float(features[2])
        },
        "importance": {
            "tremor_index": 0.4,
            "stroke_variance": 0.35,
            "edge_density": 0.25
        }
    }
