import requests
import json
from datetime import date, timedelta


# 'Eps'
# - NS = not started, FT = finished, S1 = set 1, S2 = set 2
# 'Spid'
# for a live match, serving player id (1 or 2)
#
'''
Cache all the data in data.json
'''
# url = "https://livescore6.p.rapidapi.com/matches/v2/list-by-date"

# querystring = {"Category":"tennis","Date":"20230720","Timezone":"-7"}

# headers = {
# 	"X-RapidAPI-Key": "4babb981dbmshfff34a0c1b9df5ap1a6f90jsn985f72b4a576",
# 	"X-RapidAPI-Host": "livescore6.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# with open("data.json", "w") as outfile:
#     json.dump(response.json(), outfile)
# print(response.json())


'''
Get the date for today, tomorrow, and yesterday
'''
# today = date.today()
# yesterday = today - timedelta(1)
# tomorrow = today + timedelta(1)
# today_date = str(today.year) + str(today.month) + str(today.day)
# yesterday_date = str(yesterday.year) + str(yesterday.month) + str(yesterday.day)
# tomorrow_date = str(tomorrow.year) + str(tomorrow.month) + str(tomorrow.day)
# print(yesterday_date)
# print(today_date)
# print(tomorrow_date)

with open("data.json", "r") as data:
    json_data = json.load(data)

print(json_data['Stages'][9]['Events'][0].keys())
# print(json_data['Stages'][9])
# for tournament in json_data['Stages']:
#     print(tournament["Csnm"] + " " + tournament["Snm"])
#     print("-------------------")
#     for event in tournament["Events"]:
#         print(event['T1'][0]['Nm'] + " vs " + event['T2'][0]['Nm'])
#     print("\n")