def achievement_tracker() -> None:
    """
    Shows simple achievement analysis using sets operations
    """
    # Sets
    alice = {
            'first_kill',
            'level_10',
            'treasure_hunter',
            'speed_demon'
                        }
    bob = {
            'first_kill',
            'level_10',
            'boss_slayer',
            'collector'
                        }
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'}
    # Set operations
    achievement_list = alice.union(bob, charlie)
    common_achievements = alice.intersection(bob, charlie)
    unique_set1 = alice.difference(bob, charlie)
    unique_set2 = bob.difference(alice, charlie)
    unique_set3 = charlie.difference(alice, bob)
    rare_achievements = unique_set1 | unique_set2 | unique_set3
    # Output
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alice achievements: {alice}")
    print(f"Player Alice achievements: {bob}")
    print(f"Player Alice achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    # All unique achievements
    print(f"All unique achievements: {achievement_list}")
    print(f"Total unique achievements: {len(achievement_list)}\n")
    # Common and rare achivements
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achivements (1 player): {rare_achievements}\n")
    # Sets comparison
    print(f"Alice vs Bob common: {alice.union(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    achievement_tracker()
