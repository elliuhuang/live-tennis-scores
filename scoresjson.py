import json

with open('scores.json') as f:
    json_data = json.load(f)

tournament = json_data['events'][5]['tournament']['name']
player1 = json_data['events'][5]['homeTeam']['name']
player1country = json_data['events'][5]['homeTeam']['country']
player2 = json_data['events'][5]['awayTeam']['name']
player2country = json_data['events'][5]['awayTeam']['country']
player1score = json_data['events'][5]['homeScore']['period1']
player2score = json_data['events'][5]['awayScore']['period1']

# for match in json_data['events']:
#     tournament = match['tournament']['name']
#     player1 = match['homeTeam']['name']
#     player1c = match['homeTeam']['country']
#     player2 = match['awayTeam']['name']
#     player1score = match['homeScore']['period1']
#     player2score = match['awayScore']['period1']
#     print(tournament, "|", player1, player1score, "-", player2score, player2)

print(tournament, "|", player1, player1country['name'], player1score, "-", player2score, player2, player2country['name'])

