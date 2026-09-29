from fastapi import FastAPI

app = FastAPI(
    title="GarmentOS API",
    version="0.1.0",
    description="Garment retail shop management API",
)


@app.get("/")
def root():
    return {
        "app": "GarmentOS",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
