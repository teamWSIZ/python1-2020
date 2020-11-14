import requests
from time import sleep

def recent_logins():
    # zbiera loginname userów 30 ostatnich zdarzeń na github
    r = requests.get('https://api.github.com/events')
    j = r.json()  # to jest tablica słowników/dict
    users = []
    for e in j:
        users.append(e['actor']['login'])
    return users

users = recent_logins()
print(users)
sleep(10)
users = recent_logins()
print(users)