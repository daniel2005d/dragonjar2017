import requests
import json

comodines = ["!", "{", "}", "[", "]", "-", "*", "(", ")", "^"]

proxies = {'http':'http://@localhost:8080'}
header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
for c in comodines:
    for i in range(0,1024):
        data = {'m':c+'445943744'}
        print('Consumiendo {}{}445943744'.format(str(i), c))
        response = requests.post('http://challenge-wargame.rhcloud.com/wtf3?n='+ str(i), data=json.dumps(data),headers=header, proxies=proxies)
        if response.status_code == 200:
            data = json.loads(response.text)
            if (data["msg"] != 'nope'):
                print("Este es \n\n\n\n\n\n\n ")
                i=1025

