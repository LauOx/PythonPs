data = [
    {'id': 1, 'player': 'frank', 'event_type': 'login', 'timestamp': '2024-01-01T23:17', 'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}},
    {'id': 2, 'player': 'frank', 'event_type': 'login', 'timestamp': '2024-01-22T23:57', 'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}},
    {'id': 3, 'player': 'diana', 'event_type': 'login', 'timestamp': '2024-01-01T02:13', 'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}},
    {'id': 4, 'player': 'alice', 'event_type': 'level_up', 'timestamp': '2024-01-07T22:41', 'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}},
    {'id': 5, 'player': 'bob', 'event_type': 'death', 'timestamp': '2024-01-19T08:51', 'data': {'level': 1, 'score_delta': 63, 'zone': 'pixel_zone_4'}},
    {'id': 6, 'player': 'charlie', 'event_type': 'kill', 'timestamp': '2024-01-05T06:48', 'data': {'level': 22, 'score_delta': 4, 'zone': 'pixel_zone_1'}},
    {'id': 7, 'player': 'diana', 'event_type': 'login', 'timestamp': '2024-01-12T11:38', 'data': {'level': 17, 'score_delta': -56, 'zone': 'pixel_zone_4'}},
    {'id': 8, 'player': 'eve', 'event_type': 'login', 'timestamp': '2024-01-30T12:05', 'data': {'level': 36, 'score_delta': 200, 'zone': 'pixel_zone_5'}},
    {'id': 9, 'player': 'charlie', 'event_type': 'level_up', 'timestamp': '2024-01-07T22:04', 'data': {'level': 3, 'score_delta': 133, 'zone': 'pixel_zone_3'}},
    {'id': 10, 'player': 'alice', 'event_type': 'logout', 'timestamp': '2024-01-28T03:24', 'data': {'level': 18, 'score_delta': 364, 'zone': 'pixel_zone_3'}},
    {'id': 11, 'player': 'bob', 'event_type': 'kill', 'timestamp': '2024-01-12T06:42', 'data': {'level': 18, 'score_delta': -27, 'zone': 'pixel_zone_5'}},
    {'id': 12, 'player': 'frank', 'event_type': 'logout', 'timestamp': '2024-01-18T23:15', 'data': {'level': 11, 'score_delta': 373, 'zone': 'pixel_zone_4'}},
    {'id': 13, 'player': 'charlie', 'event_type': 'item_found', 'timestamp': '2024-01-23T17:14', 'data': {'level': 44, 'score_delta': 232, 'zone': 'pixel_zone_1'}},
    {'id': 14, 'player': 'bob', 'event_type': 'login', 'timestamp': '2024-01-26T10:25', 'data': {'level': 18, 'score_delta': -33, 'zone': 'pixel_zone_2'}},
    {'id': 15, 'player': 'eve', 'event_type': 'item_found', 'timestamp': '2024-01-11T06:41', 'data': {'level': 32, 'score_delta': 305, 'zone': 'pixel_zone_4'}},
    {'id': 16, 'player': 'bob', 'event_type': 'kill', 'timestamp': '2024-01-05T07:47', 'data': {'level': 36, 'score_delta': 451, 'zone': 'pixel_zone_3'}},
    {'id': 17, 'player': 'frank', 'event_type': 'level_up', 'timestamp': '2024-01-14T18:25', 'data': {'level': 24, 'score_delta': 124, 'zone': 'pixel_zone_2'}},
    {'id': 18, 'player': 'eve', 'event_type': 'death', 'timestamp': '2024-01-03T01:55', 'data': {'level': 8, 'score_delta': 56, 'zone': 'pixel_zone_2'}},
    {'id': 19, 'player': 'frank', 'event_type': 'death', 'timestamp': '2024-01-20T02:24', 'data': {'level': 25, 'score_delta': 379, 'zone': 'pixel_zone_5'}},
    {'id': 20, 'player': 'charlie', 'event_type': 'level_up', 'timestamp': '2024-01-28T00:43', 'data': {'level': 47, 'score_delta': 17, 'zone': 'pixel_zone_5'}},
    ]

with open("events.txt", "w") as f:
    for event in data:
        line = f"{event['id']},{event['player']},{event['event_type']},{event['data']['level']}\n"
        f.write(line)