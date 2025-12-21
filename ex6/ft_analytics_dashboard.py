def get_high_scorers(players):
    return [name for name, data in players.items() if data.get("score") >= 2000]

def double_scores(players):
    return [data.get("score") * 2 for name, data in players.items()]

def active_players(players):
    return [name for name, data in players.items() if data.get("active")]


print("=== Game Analytics Dashboard ===")

players = {
    "alice": {
        "score": 2300,
        "achievements": 5,
        "active": True,
        "region": "north"
    },
    "bob": {
        "score": 1800,
        "achievements": 3,
        "active": True,
        "region": "east"
    },
    "charlie": {
        "score": 2150,
        "achievements": 7,
        "active": True,
        "region": "central"
    },
    "diana": {
        "score": 2050,
        "achievements": 2,
        "active": False,
        "region": "north"
    }
}

print("=== List Comprehension  Examples ===")
print(f"High scorers (>2000): {get_high_scorers(players)}")
print(f"Scores doubled: {double_scores(players)}")
print(f"Active players: {active_players(players)}")
print("")
print("=== Dict Comprehension  Examples ===")
