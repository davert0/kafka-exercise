from dataclasses import dataclass
import os

DEFAULT_PORT = 8002


@dataclass(frozen=True)
class Settings:
    service_name: str
    port: int
    log_level: str


def load_settings() -> Settings:
    return Settings(
        service_name=os.getenv("SERVICE_NAME", "order_projector"),
        port=int(os.getenv("PORT", str(DEFAULT_PORT))),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
