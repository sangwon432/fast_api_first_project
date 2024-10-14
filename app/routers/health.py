from fastapi import APIRouter

# test: http localhost:8001/health

router = APIRouter(prefix = "/health", tags=["Health"])

@router.get("")
async def health() -> dict[str, str]:
    return {
        "ok": "true"
    }