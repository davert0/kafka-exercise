from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/health")
async def health(request: Request) -> dict[str, str]:
    settings = request.app.state.settings
    return {"status": "ok", "service": settings.service_name}


@router.get("/")
async def root(request: Request) -> dict[str, str | int]:
    settings = request.app.state.settings
    return {"service": settings.service_name, "schema_version": 1}
