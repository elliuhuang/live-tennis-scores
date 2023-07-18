from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def get_live_scores():
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

    requests.request("GET", url, data=payload, headers=headers)
    json_data = json.loads(response.text)

    live_scores = {}
    for match in json_data['events']:
        tournament = match['tournament']['category']['name'] + " " + match['tournament']['name']
        score = {
                #  'tournament_type': match['tournament']['category']['name'], 
                #  'tournament': match['tournament']['name'], 
                 'player1': match['homeTeam']['name'], 
                 'player1cc': "",
                 'player2': match['awayTeam']['name'], 
                 'player2cc': "",
                 'player1set1': match['homeScore']['period1'], 
                 'player2set1': match['awayScore']['period1'], 
                 'player1set2': -1,
                 'player2set2': -1,
                 'player1set3': -1,
                 'player2set3': -1,
                 'player1set4': -1,
                 'player2set4': -1,
                 'player1set5': -1,
                 'player2set5': -1
        }
        try: 
            score['player1cc'] = "https://flagcdn.com/w20/" + match['homeTeam']['country']['alpha2'].lower() + ".png"
            score['player2cc'] = "https://flagcdn.com/w20/" + match['awayTeam']['country']['alpha2'].lower() + ".png"
        except:
            pass
        try:
            score['player1set2'] = match['homeScore']['period2']
        except:
            pass
        else:
            score['player2set2'] = match['awayScore']['period2']
            score['player1set2'] = match['homeScore']['period2']
        try:
            score['player1set3'] = match['homeScore']['period3']
        except:
            pass
        else:
            score['player1set3'] = match['homeScore']['period3']
            score['player2set3'] = match['awayScore']['period3']
        try:
            score['player1set4'] = match['homeScore']['period4']
        except:
            pass
        else:
            score['player1set4'] = match['homeScore']['period4']
            score['player2set4'] = match['awayScore']['period4']
        try:
            score['player1set5'] = match['homeScore']['period5']
        except:
            pass
        else:
            score['player1set5'] = match['homeScore']['period5']
            score['player2set5'] = match['awayScore']['period5']
        finally: 
            if (tournament in live_scores.keys()):
                live_scores[tournament].append(score)
            else:
                live_scores[tournament] = [score]

    '''
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
    '''

    return render_template('index.html', live_scores=live_scores)
