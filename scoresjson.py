import json

with open('scores.json') as f:
    json_data = json.load(f)

tournament = json_data['events'][0]['tournament']['name']
player1 = json_data['events'][0]['homeTeam']['name']
player2 = json_data['events'][0]['awayTeam']['name']
player1score = json_data['events'][0]['homeScore']['period1']
player2score = json_data['events'][0]['awayScore']['period1']

for match in json_data['events']:
    tournament = match['tournament']['name']
    player1 = match['homeTeam']['name']
    player2 = match['awayTeam']['name']
    player1score = match['homeScore']['period1']
    player2score = match['awayScore']['period1']
    print(tournament, "|", player1, player1score, "-", player2score, player2)

#print("\n")

