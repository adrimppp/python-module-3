def player_achievements(name:str, player_achievements:tuple):
    print(f"Player {name} achievements {player_achievements}")

achievements = set(['boss_slayer', 'collector', 'first_kill', 'level_10', 'perfectionist', 'speed_demon', 'treasure_hunter'])

player_1 = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
player_2 = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
player_3 = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'])

print("=== Achievement Tracker System ===")
player_achievements("alice", player_1)
player_achievements("bob", player_2)
player_achievements("charlie", player_3)

unique_achievements = player_1.union(player_2, player_3)
print("=== Achievement Analytics ===")
print(f"All unique achievemenst: {unique_achievements}")
print(f"Total unique achivements: {len(unique_achievements)}")
print(f"Unique achievemets: {player_1.intersection(player_2, player_3)}")
print(f"Rare achievements (1 player):")
print(f"Alice vs Bob common: {player_1.difference(player_2)}")
print(f"Alice unique: {player_1.difference(player_2)}")
print(f"Bob unique: {player_2.difference(player_1)}")