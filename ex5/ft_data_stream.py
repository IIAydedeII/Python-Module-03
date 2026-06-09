#!/usr/bin/env python3
from typing import Generator
import random

Event = tuple[str, str]

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> Generator[Event]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(events: list[Event]) -> Generator[Event]:
    while events:
        yield events.pop(random.randrange(len(events)))


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = gen_event()

    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    pick_ten = [next(gen) for _ in range(10)]
    print("Built list of 10 events", pick_ten)

    for event in consume_event(pick_ten):
        print("Got event from list:", event)
        print("Remains in list:", pick_ten)


if __name__ == "__main__":
    main()
