from fastapi import FastAPI

app = FastAPI(title="simple fastapi server")

@app.get("/")
def root():
    return {"Hello DevOps"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
