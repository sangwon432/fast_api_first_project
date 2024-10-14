from fastapi import APIRouter

# test: http localhost:8001/health
# review this later

router = APIRouter(prefix = "/health", tags=["Health"])

@router.get("")
async def health() -> dict[str, str]:
    return {
        "ok": "okay2"
    }