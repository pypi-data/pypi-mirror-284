from __future__ import annotations
from attrs import define, field
from abc import ABC
from .base_event import BaseEvent


@define
class BasePromptEvent(BaseEvent, ABC):
    model: str = field(kw_only=True, metadata={"serializable": True})
