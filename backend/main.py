from fastapi import FastAPI, WebSocket
from database import Base, engine
from auth.routes import router as auth_router
from websocket.ws import websocket_endpoint

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return {"status": "MedPulse Running"}

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket_endpoint(websocket)
