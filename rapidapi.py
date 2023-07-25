from flask import Flask, render_template
import requests
import json
from datetime import date

app = Flask(__name__)


@app.route("/")
def live_scores():

    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"tennis","Timezone":"-7"}

    headers = {
	    "X-RapidAPI-Key": "4babb981dbmshfff34a0c1b9df5ap1a6f90jsn985f72b4a576",
	    "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    json_data = data['Stages']

    scores = {}

    # for row in json_data:
    #     scores['tournament_type'] = row['Cnm']
    #     scores['matches'] = {}
    #     for match in row['Events']:

    #     events = row['Events']


    return render_template('live_scores.html', scores=scores)


# response = requests.get(url, headers=headers, params=querystring)

# json_data = response.json()

# print(len(json_data['Stages']))
# for stage in json_data['Stages']:
#     print(stage['Cnm'])

#print(response.json())

# json_data = json.loads(response.text)

# json_object = json.dumps(json_data, indent=4)

# with open("livescores.json", 'w') as outfile: 
#     outfile.write(json_object)

