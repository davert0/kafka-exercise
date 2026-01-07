from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from pkg.contracts.event_types import EventType


class Event(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    event_id: str
    event_type: EventType
    order_id: str = Field(min_length=1)
    occurred_at: datetime
    schema_version: int = Field(ge=1)
    producer: str = Field(min_length=1)
    payload: dict

    @field_validator("event_id")
    @classmethod
    def _validate_event_id(cls, value: str) -> str:
        try:
            UUID(value)
        except ValueError as exc:
            raise ValueError("event_id must be a valid UUID string") from exc
        return value

    @field_validator("occurred_at")
    @classmethod
    def _validate_occurred_at(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            raise ValueError("occurred_at must be timezone-aware")
        return value

    def to_json(self) -> str:
        return self.model_dump_json()

    @classmethod
    def from_json(cls, json_str: str) -> "Event":
        return cls.model_validate_json(json_str)


__all__ = ["Event", "ValidationError"]
