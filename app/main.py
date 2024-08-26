from fastapi import FastAPI
from app.api.endpoints import card_routes

app = FastAPI()

# Include the API routes
app.include_router(card_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
