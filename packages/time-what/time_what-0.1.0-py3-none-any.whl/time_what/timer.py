from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Self, Callable, Any
from functools import partialmethod
import time


@dataclass
class TimeCounter:
    base: int
    count: int = field(default=0, init=False)

    second_base: ClassVar[int] = 1
    millisecond_base: ClassVar[int] = 1000
    microsecond_base: ClassVar[int] = 1000000
    nanosecond_base: ClassVar[int] = 1000000000

    @classmethod
    def nano_counter(cls) -> Self:
        return cls(base=TimeCounter.nanosecond_base)

    @classmethod
    def second_counter(cls) -> Self:
        return cls(base=TimeCounter.second_base)

    def as_unit(self, base: int) -> float:
        if base == self.base:
            return self.count
        return (self.count * base) / self.base

    as_seconds = partialmethod(as_unit, second_base)
    as_milli = partialmethod(as_unit, millisecond_base)
    as_micro = partialmethod(as_unit, microsecond_base)
    as_nano = partialmethod(as_unit, nanosecond_base)

    def add(self, other: int):
        self.count += other

    def add_timer(self, other: TimeCounter):
        if self.base == other.base:
            self.count += other.count
            return

        self.count += int(other.as_unit(self.base))

    def add_unsafe_timer(self, other: TimeCounter):
        self.count += other.count

    def reset(self) -> None:
        self.count = 0

    def __lt__(self, other: TimeCounter) -> bool:
        return self.as_nano() < other.as_nano()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TimeCounter):
            return False
        return self.as_nano() == other.as_nano()

@dataclass
class BaseTimer:
    # todo: make repr nicer
    __start_time: int = field(default=0, init=False, repr=False)

    total_time: TimeCounter = field(default_factory=TimeCounter.nano_counter, init=True,kw_only=True)

    # total_time: int = field(default=0, init=False, repr=True)
    is_running: bool = field(default=False, init=False, repr=True)

    def start(self) -> Self:
        """Start a new timer"""
        self.__start_time = time.perf_counter_ns()
        self.is_running = True
        return self

    def as_seconds(self):
        return self.total_time.as_seconds()

    def stop(self) -> float:
        now = time.perf_counter_ns()
        elapsed = now - self.__start_time
        self.is_running = False
        self.total_time.add(elapsed)
        return self.as_seconds()

    def reset(self):
        self.total_time.reset()

    def __enter__(self) -> Self:
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info: Any) -> None:
        """Stop the context manager timer"""
        self.stop()


@dataclass
class Timer(BaseTimer):
    name: str | None = field(default=None, repr=True)
    logger: Callable[[str], Any] | None = field(default=print, repr=False)

    def stop(self) -> float:
        elapsed_time = super().stop()

        self.reset()
        if self.logger:
            # todo: units
            message = f'Elapsed time: {elapsed_time:0.4f} seconds'
            if self.name:
                message = f'{self.name} - {message}'

            self.logger(message)

        return elapsed_time
