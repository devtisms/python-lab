from fastapi import FastAPI

app = FastAPI(
    title="Python Lab",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "app": "Python Lab",
        "status": "online",
        "environment": "development"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
