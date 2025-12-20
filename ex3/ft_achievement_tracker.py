def print_player_achievements(player_name: str, player_achievements: set):
    """
        Prints player name and its achievements.
        Params:
            player_name -> the player name as a string
            plaeyr_achievements -> the player
            achievements in a set
    """
    print(f"Player {player_name} achievements: {player_achievements}")

if __name__ == "__main__":

    print("")
    alice_achievements= {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
    bob_achievements= {"first_kill", "level_10", "boss_slayer", "collector"},
    charlie_achievements = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

    print("=== Achievement Tracker System ===")
    print_player_achievements("alice", alice_achievements)
    print_player_achievements("bob", bob_achievements)
    print_player_achievements("charlie", charlie_achievements)


