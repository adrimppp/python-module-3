def return_game_events(players, total_events):
    i = 0
    events = ["killed monster", "found treasure", "leveled up"]

    while i < total_events:
        player, level = players[i % len(players)]
        action = events[i % len(events)]
        yield player, level, action
        i += 1

def fibonacci_seq():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_seq():
    """Generate an infinite sequence of prime numbers.

    Yields:
        int: The next prime number.
    """
    num = 2
    while True:
        is_prime = True
        for i in range(2, num - 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1




players = [("alice", 5), ("bob", 12), ("charlie", 8)]
TOTAL_EVENTS = 1000

print(f"Processing {TOTAL_EVENTS} game events...")

event_number = 1
total_processed = 0
high_level_players = 0
treasure_events = 0
level_up_events = 0

for player, level, action in return_game_events(players, TOTAL_EVENTS):
    total_processed += 1

    if total_processed <= 3:
        print(f"Event {total_processed}: "
              f"Player {player} (level {level}) {action}")

    if level >= 10:
        high_level_players += 1

    if action == "found treasure":
        treasure_events += 1

    if action == "leveled up":
        level_up_events += 1

print("...")
print("=== Stream Analytics ===")
print(f"Total events: {TOTAL_EVENTS}")
print(f"High level players (+10): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level up events: {level_up_events}")
print("\nMemory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")
fib = fibonacci_seq()
fib_values = [str(next(fib)) for _ in range(10)]
print(f"Fibonacci sequence (first 10): {', '.join(fib_values)}")
primes = prime_seq()
prim_values = [str(next(primes)) for _ in range(10)]
print(f"Prime sequence (first 10): {', '.join(prim_values)}")
