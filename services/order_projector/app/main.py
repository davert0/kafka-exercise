import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pkg import contracts

from services.order_projector.app.config import load_settings
from services.order_projector.app.http import router


def create_app() -> FastAPI:
    settings = load_settings()
    logging.basicConfig(level=settings.log_level)
    logger = logging.getLogger(settings.service_name)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        logger.info("Starting %s", settings.service_name)
        logger.debug("Contracts loaded: %s", contracts.EventType.ORDER_CREATED.value)
        yield
        logger.info("Shutting down %s", settings.service_name)

    app = FastAPI(title=settings.service_name, lifespan=lifespan)
    app.state.settings = settings
    app.include_router(router)
    return app


app = create_app()
