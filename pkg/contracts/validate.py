from pydantic import ValidationError

from pkg.contracts.event import Event


def validate_event_dict(data: dict) -> None:
    try:
        Event.model_validate(data)
    except ValidationError as exc:
        details = "; ".join(
            f"{'.'.join(str(part) for part in err['loc'])}: {err['msg']}"
            for err in exc.errors()
        )
        raise ValueError(f"Invalid event payload: {details}") from exc
