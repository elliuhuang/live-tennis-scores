import requests
import json

url = "https://api.sofascore.com/api/v1/sport/tennis/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": "W/\"a554173478\"",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers)

json_data = json.loads(response.text)

for match in json_data['events']:
    tournament_type = match['tournament']['category']['name']
    tournament = match['tournament']['name']
    player1 = match['homeTeam']['name']
    player2 = match['awayTeam']['name']
    player1set1 = match['homeScore']['period1']
    player2set1 = match['awayScore']['period1']
    try:
        player1set2 = match['homeScore']['period2']
        player2set2 = match['homeScore']['period2']
        print(tournament_type, "|", tournament, "|", player1, player1set1, "-", player2set1, player1set2, "-", player2set2, player2)
    except:
        print(tournament_type, "|", tournament, "|", player1, player1set1, "-", player2set1, player2)

    #print(tournament, "|", player1, player1set1, "-", player2set1, player1set2, "-", player2set2, player2)
