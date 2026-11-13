from fastapi import FastAPI
from prometheus_client import make_asgi_app

app = FastAPI(title="JurisFlow API")

# Add prometheus asgi middleware to route /metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/health")
async def health():
    return {"status": "ok"}
