def print_player_achievements(player_name: str, player_achievements: set):
    """
        Prints player name and its achievements.
        Params:
            player_name -> the player name as a string
            plaeyr_achievements -> the player
            achievements in a set
    """
    print(f"Player {player_name} achievements: {player_achievements}")


def unique_achievements_info(achievements_1, achievements_2, achievements_3):
    unique_achievements = achievements_1.union(achievements_2, achievements_3)
    common_achievements = achievements_1.intersection(achievements_2, achievements_3)

    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achiements: {len(unique_achievements)}")
    print(f"\nCommon to all players: {common_achievements}")
    print(f"Rare achievements: ") #TODO

def compare_players(player_1: set, player_2:set):
    print(f"Alice vs Bob common: {player_1.intersection(player_2)}")
    print(f"Alice unique: {player_1.difference(player_2)}")
    print(f"Bob unique: {player_2.difference(player_1)}")


if __name__ == "__main__":

    print("")
    alice_achievements= {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob_achievements= {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie_achievements = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

    print("=== Achievement Tracker System ===\n")
    print_player_achievements("alice", alice_achievements)
    print_player_achievements("bob", bob_achievements)
    print_player_achievements("charlie", charlie_achievements)

    print("=== Achievement Analytics ===")
    unique_achievements_info(alice_achievements, bob_achievements, charlie_achievements)

    compare_players(alice_achievements, bob_achievements)