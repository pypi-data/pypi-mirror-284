from __future__ import annotations

from pylav.players.filters.misc import FilterMixin


class Echo(FilterMixin):
    __slots__ = ("_delay", "_decay", "_default")

    def __init__(self, delay: float | None = None, decay: float | None = None) -> None:
        super().__init__()
        self.delay = delay
        self.decay = decay

    def to_dict(self) -> dict[str, float | bool | None]:
        return {
            "delay": self.delay,
            "decay": self.decay,
        }

    @classmethod
    def from_dict(cls, data: dict[str, float | bool | None]) -> Echo:
        return cls(delay=data["delay"], decay=data["decay"])

    def __repr__(self) -> str:
        return f"<Echo: delay={self.delay}, decay={self.decay}>"

    @property
    def delay(self) -> float | None:
        return self._delay

    @delay.setter
    def delay(self, v: float | None) -> None:
        if v is None:
            self._delay = None
            return
        if v < 0:
            raise ValueError(f"Delay must be must be greater than 0, not {v}")
        self._delay = v

    @property
    def decay(self) -> float | None:
        return self._decay

    @decay.setter
    def decay(self, v: float | None) -> None:
        if v is None:
            self._decay = v
            return
        if not (0.0 < v <= 1.0):
            raise ValueError(f"Decay must be must be 0.0 < x ≤ 1.0, not {v}")
        self._decay = v

    @classmethod
    def default(cls) -> Echo:
        return cls()

    def get(self) -> dict[str, float]:
        if self.off:
            return {}
        response = {}
        if self.delay is not None:
            response["delay"] = self.delay
        if self.decay is not None:
            response["decay"] = self.decay
        return response

    def reset(self) -> None:
        self.delay = self.decay = None
