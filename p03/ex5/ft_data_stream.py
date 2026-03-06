import time
import random
from typing import Generator

# ───────────────────────────────────────────────
# 1. Game event generator (the "data stream")
# ───────────────────────────────────────────────
def game_event_stream(count: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie", "diana", "emma", "frank", "grace"]
    actions = [
        "killed monster",
        "found treasure",
        "leveled up",
        "died to trap",
        "opened chest",
        "cast spell",
        "defeated boss"
    ]

    for i in range(1, count + 1):
        player = random.choice(players)
        level = random.randint(1, 20)
        action = random.choice(actions)
        
        # We could also yield a dict/tuple → but string keeps output simple
        yield f"Player {player} (level {level}) {action}"


# ───────────────────────────────────────────────
# 2. Filtering generators (composable!)
# ───────────────────────────────────────────────
def high_level_events(events: Generator[str, None, None]) -> Generator[str, None, None]:
    for event in events:
        if "(level " in event:
            level_part = event.split("(level ")[1].split(")")[0]
            if int(level_part) >= 10:
                yield event


def treasure_events(events: Generator[str, None, None]) -> Generator[str, None, None]:
    for event in events:
        if "treasure" in event.lower():
            yield event


def level_up_events(events: Generator[str, None, None]) -> Generator[str, None, None]:
    for event in events:
        if "leveled up" in event.lower():
            yield event


# ───────────────────────────────────────────────
# 3. Simple stats collector using generators
# ───────────────────────────────────────────────
def collect_stats(event_stream: Generator[str, None, None]) -> dict:
    total = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    # We chain generators → very memory efficient
    for event in event_stream:
        total += 1
        
        if "treasure" in event.lower():
            treasure_count += 1
        if "leveled up" in event.lower():
            levelup_count += 1
        if "(level " in event:
            try:
                lvl = int(event.split("(level ")[1].split(")")[0])
                if lvl >= 10:
                    high_level_count += 1
            except:
                pass

    return {
        "total": total,
        "high_level": high_level_count,
        "treasure": treasure_count,
        "levelups": levelup_count
    }


# ───────────────────────────────────────────────
# 4. Classic examples
# ───────────────────────────────────────────────
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes(count: int) -> Generator[int, None, None]:
    num = 2
    found = 0
    while found < count:
        if is_prime(num):
            yield num
            found += 1
        num += 1


# ───────────────────────────────────────────────
# Main demonstration
# ───────────────────────────────────────────────
def main():
    print("=== Game Data Stream Processor ===")
    EVENT_COUNT = 1000

    print(f"Processing {EVENT_COUNT} game events...")

    # We create the stream only once
    stream = game_event_stream(EVENT_COUNT)

    # Show first few events (without consuming the whole stream yet)
    print("Event 1:", next(stream))
    print("Event 2:", next(stream))
    print("Event 3:", next(stream))
    print("...")

    print("\n=== Stream Analytics ===")

    # Reset stream for stats (in real life you might not want to reset → use tee() or process once)
    # For demo simplicity we recreate it
    stream_for_stats = game_event_stream(EVENT_COUNT)

    start = time.time()
    stats = collect_stats(stream_for_stats)
    duration = time.time() - start

    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['levelups']}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {duration:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    
    print("Fibonacci sequence (first 10):", end=" ")
    print(", ".join(map(str, fibonacci(10))))
    
    print("Prime numbers (first 5):", end=" ")
    print(", ".join(map(str, primes(5))))


if __name__ == "__main__":
    main()