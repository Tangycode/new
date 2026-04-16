from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Khel AI Sports API")

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def home():
    return {"message": "API is live"}

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------
# Request Schema
# -----------------------------
class StrikeRateRequest(BaseModel):
    runs: int
    balls: int

# -----------------------------
# Functional Endpoint
# -----------------------------
@app.post("/strike-rate")
def calculate_strike_rate(data: StrikeRateRequest):
    if data.balls == 0:
        return {"strike_rate": 0}

    strike_rate = (data.runs / data.balls) * 100

    return {
        "runs": data.runs,
        "balls": data.balls,
        "strike_rate": round(strike_rate, 2)
    }
