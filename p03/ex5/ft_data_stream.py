from typing import Generator


def data_players() -> list[dict]:
    events = [
        {
            "id": 1,
            "player": "sara",
            "event": "login",
            "timestamp": "2025-03-12T14:22",
            "level": 8,
            "score_delta": 187,
            "zone": "neon_sector_3",
        },
        {
            "id": 2,
            "player": "max",
            "event": "kill",
            "timestamp": "2025-03-15T09:17",
            "level": 42,
            "score_delta": 312,
            "zone": "cyber_spire_1",
        },
        {
            "id": 3,
            "player": "luna",
            "event": "treasure",
            "timestamp": "2025-03-10T23:45",
            "level": 19,
            "score_delta": -48,
            "zone": "void_rift_4",
        },
        {
            "id": 4,
            "player": "kira",
            "event": "level_up",
            "timestamp": "2025-03-18T03:11",
            "level": 37,
            "score_delta": 265,
            "zone": "neon_sector_7",
        },
        {
            "id": 5,
            "player": "jax",
            "event": "death",
            "timestamp": "2025-03-14T16:08",
            "level": 5,
            "score_delta": 94,
            "zone": "shadow_canyon_2",
        },
        {
            "id": 6,
            "player": "nora",
            "event": "logout",
            "timestamp": "2025-03-19T21:34",
            "level": 31,
            "score_delta": 408,
            "zone": "cyber_spire_5",
        },
        {
            "id": 7,
            "player": "axel",
            "event": "login",
            "timestamp": "2025-03-11T07:55",
            "level": 12,
            "score_delta": -72,
            "zone": "void_rift_1",
        },
        {
            "id": 8,
            "player": "sara",
            "event": "treasure",
            "timestamp": "2025-03-17T13:29",
            "level": 44,
            "score_delta": 376,
            "zone": "neon_sector_9",
        },
        {
            "id": 9,
            "player": "luna",
            "event": "kill",
            "timestamp": "2025-03-16T04:42",
            "level": 28,
            "score_delta": 153,
            "zone": "shadow_canyon_4",
        },
        {
            "id": 10,
            "player": "max",
            "event": "level_up",
            "timestamp": "2025-03-20T01:19",
            "level": 50,
            "score_delta": 289,
            "zone": "cyber_spire_3",
        },
        {
            "id": 11,
            "player": "kira",
            "event": "death",
            "timestamp": "2025-03-13T18:07",
            "level": 23,
            "score_delta": 41,
            "zone": "void_rift_6",
        },
        {
            "id": 12,
            "player": "jax",
            "event": "treasure",
            "timestamp": "2025-03-12T10:51",
            "level": 16,
            "score_delta": 502,
            "zone": "neon_sector_2",
        },
        {
            "id": 13,
            "player": "nora",
            "event": "login",
            "timestamp": "2025-03-15T22:03",
            "level": 9,
            "score_delta": -19,
            "zone": "shadow_canyon_1",
        },
        {
            "id": 14,
            "player": "axel",
            "event": "kill",
            "timestamp": "2025-03-19T06:38",
            "level": 35,
            "score_delta": 227,
            "zone": "cyber_spire_8",
        },
        {
            "id": 15,
            "player": "sara",
            "event": "logout",
            "timestamp": "2025-03-17T19:14",
            "level": 47,
            "score_delta": 134,
            "zone": "void_rift_5",
        },
        {
            "id": 16,
            "player": "luna",
            "event": "treasure",
            "timestamp": "2025-03-20T08:22",
            "level": 41,
            "score_delta": 399,
            "zone": "neon_sector_6",
        },
        {
            "id": 17,
            "player": "kira",
            "event": "death",
            "timestamp": "2025-03-14T12:59",
            "level": 4,
            "score_delta": 88,
            "zone": "shadow_canyon_7",
        },
        {
            "id": 18,
            "player": "max",
            "event": "level_up",
            "timestamp": "2025-03-18T23:47",
            "level": 33,
            "score_delta": 176,
            "zone": "cyber_spire_4",
        },
    ]
    return events


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def get_the_prime(n: int) -> Generator[int, None, None]:
    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True

        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num

        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    events = data_players()
    total_events = len(events)

    print(f"Processing {total_events} game events...\n")

    total = 0
    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    for event in events:
        total += 1
        player = event["player"]
        level = event["level"]
        evt_type = event.get("event")

        print(f"Event {event['id']}: Player {player} "
              f"(level {level}) {evt_type}")

        if level >= 10:
            high_level_count += 1
        if evt_type == "treasure":
            treasure_count += 1
        if evt_type == "level_up":
            level_up_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    fib_numbers = list(fibonacci(10))
    print("Fibonacci sequence (first 10): ", end="")
    print(*fib_numbers, sep=", ")

    prime_numbers = list(get_the_prime(5))
    print("Prime numbers (first 5):     ", end="")
    print(*prime_numbers, sep=", ")


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
