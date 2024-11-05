# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.delay_prediction import router as delay_router
from api.price_prediction import router as price_router
from api.travel_prediction import router as travel_router

# Initialize FastAPI app with metadata for documentation
app = FastAPI(
    title="Flight Prediction API",
    description="An API to predict flight delays, prices, and travel metrics",
    version="1.0.0",
)

# Enable CORS for cross-origin requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for different endpoints
app.include_router(delay_router, prefix="/api/delay", tags=["Delay Prediction"])
app.include_router(price_router, prefix="/api/price", tags=["Price Prediction"])
app.include_router(travel_router, prefix="/api/travel", tags=["Travel Metrics Prediction"])

# Root endpoint for health check
@app.get("/", tags=["Health Check"])
def read_root():
    return {"message": "API is up and running!"}

# If running as the main script, start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
