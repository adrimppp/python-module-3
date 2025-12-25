def get_high_scorers(players):
    return [name for name, data in players.items() if data.get("score") >= 2000]

def double_scores(players):
    return [data.get("score") * 2 for name, data in players.items()]

def active_players(players):
    return [name for name, data in players.items() if data.get("active")]

def get_scores(players):
    return {name: data["score"] for name, data in players.items() if name != "diana"}

def get_all_scores(players):
    return {name: data["score"] for name, data in players.items()}


def get_categories(players):
    return {
        "high": 3,
        "medium": 2,
        "low": 1
    }

def get_unique_achievements():
        return {
        "first_kill",
        "level_10",
        "boss_slayer"
    }

def get_unique_regions(players):
    return {data["region"] for data in players.values()}


def get_achievement_counts(players):
    return {name: data["achievements"]
            for name, data
            in players.items()
            if name != "diana"}

def get_unique_players(players):
    return set(players.keys())

def get_total_achievements(players):
    achievement_counts = get_achievement_counts(players)
    return sum(achievement_counts.values())

def get_average_score(players):
    active_scores = [
        data["score"]
        for data in players.values()
        if data["active"]
    ]
    return sum(active_scores) / len(active_scores)

def get_top_performer(players):
    top_score = -1
    top_player = None
    for name, data in players.items():
        if data["score"] > top_score:
            top_score = data["score"]
            top_player = name
    return (f"{top_player} ({top_score} points, {players[top_player]["achievements"]} achievements)")
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
print(f"Player scores: {get_scores(players)}")
print(f"Score categories {get_categories(players)}")
print(f"Achievement counts: {get_achievement_counts(players)}\n")
print(f"=== Set Comprehension Examples ===")
print(f"Unique players: {get_unique_players(players)}")
print(f"Unique achievements: {get_unique_achievements()}")
print(f"Active regions: {get_unique_regions(players)}")
print(f"=== Combined Analysis ===")
print(f"Total players: {len(players)}")
print(f"Total unique achievements: {get_total_achievements(players)}")
print(f"Average scores: {get_average_score(players)}")
print(f"Top performer {get_top_performer(players)}")
