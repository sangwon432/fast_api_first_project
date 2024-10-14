from fastapi import APIRouter

# test: http localhost:8001/health
# review this later
# for some reason, I always have to chmod -x+ before running deploy.

router = APIRouter(prefix = "/health", tags=["Health"])

@router.get("")
async def health() -> dict[str, str]:
    return {
        "ok": "okay3"
    }