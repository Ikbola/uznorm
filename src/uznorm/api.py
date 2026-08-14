"""HTTP API for uznorm."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from uznorm import normalize_apostrophes

app = FastAPI(
    title="uznorm",
    description="Normalization utilities for Uzbek text",
    version="0.1.0",
)


class NormalizeRequest(BaseModel):
    text: str = Field(..., max_length=10000, description="Uzbek text to normalize")


class NormalizeResponse(BaseModel):
    original: str
    normalized: str
    changed: bool


@app.get("/")
def root():
    """Landing endpoint — points visitors at the docs."""
    return {
        "service": "uznorm",
        "description": "Normalization utilities for Uzbek text",
        "docs": "/docs",
        "endpoints": ["/health", "/normalize"],
    }


@app.get("/health")
def health():
    """Liveness check — deployment platforms poll this."""
    return {"status": "ok"}


@app.post("/normalize", response_model=NormalizeResponse)
def normalize(request: NormalizeRequest) -> NormalizeResponse:
    normalized = normalize_apostrophes(request.text)
    return NormalizeResponse(
        original=request.text,
        normalized=normalized,
        changed=normalized != request.text,
    )
