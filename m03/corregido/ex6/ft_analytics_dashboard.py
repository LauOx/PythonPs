#!/usr/bin/env python3

def data_generator(n_players: int) -> dict[str, dict]:
    """
    Generates different combination of data
    to use in the analythics_dashboard()
    """
    name_list = [
        'alice',
        'bob',
        'charlie',
        'diana',
        'lau',
        'john',
        'pedro',
        'pablo',
        'jacinto',
        'jose'
        ]
    achievement_list = [
        'first_blood',
        'level_master',
        'speed_runner',
        'treasure_seeker',
        'boss_hunter',
        'pixel_perfect',
        'combo_king',
        'explorer'
        ]
    players_data = dict()
    i = 0
    range = len(achievement_list)
    while i < n_players:
        achievements = set()
        active = False
        key_name = name_list[i % len(name_list)]
        # score invented math
        score = ((i + 1) * 1353) % 2000
        # active true or false
        if score % 3 == 0:
            active = True
        # achivements sets
        index = i
        loop = index % range
        limit = (range + loop) / 4
        while loop <= limit:
            index += 13
            achievements |= {achievement_list[index % range]}
            loop += 1
        player_data = {
                'score': score,
                'active': active,
                'achievements': achievements
                }
        players_data[key_name] = player_data
        i += 1
    return players_data


def analytics_dashboard(data: dict) -> None:
    """
    shows analytcs using list, dict and sets
    """
    print("=== Game Analytics Dashboard ===\n")
    # list comprehesion
    print("=== List Comprehension Examples ===")
    name_high_scores = [
        player for player, info in data.items()
        if info['score'] > 999
        ]
    active_players = [
        player for player, info in data.items()
        if info['active'] is True
        ]
    scores = [
        info['score'] for player, info in data.items()
        ]
    scores_doubled = [n * 2 for n in scores]
    print(f"High scorers (>1000): {name_high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")
    # dict comprehension
    print("\n=== Dict Comprehension Examples ===")
    player_scores = dict()
    high = sum(1 for player, info in data.items() if info['score'] > 999)
    medium = sum(1 for player, info in data.items()
                 if 900 > info['score'] > 300)
    low = sum(1 for player, info in data.items() if info['score'] < 300)
    scores_categories = {
        'high': high,
        'medium': medium,
        'low': low
    }
    player_scores = {player: info['score'] for player, info in data.items()}
    achievement_count = {player: len(info['achievements'])
                         for player, info in data.items()}
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {scores_categories}")
    print(f"Achievement counts: {achievement_count}")
    # sets comprehension
    print("\n=== Sets Comprehension Examples ===")
    unique_players = {player for player in data.keys()}
    unique_achievements = {achievement for info in data.values()
                           for achievement in info['achievements']}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    # combined analysis
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    top_score = max(scores_doubled) / 2
    for name, score in player_scores.items():
        if score == top_score:
            print(f"Top performer: {name} "
                  f"({score} points, "
                  f"{achievement_count[name]} achievements)")
            break


if __name__ == "__main__":
    data = data_generator(6)
    # for player in data.items():
    #     print(player)
    analytics_dashboard(data)
