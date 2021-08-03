import config
import socket
import re
from classifier import SentimentClassifier
from time import clock

sock = socket.socket()
sock.connect((config.server, config.port))

sock.send(f"PASS {config.token}\n".encode('utf-8'))
sock.send(f"NICK {config.nickname}\n".encode('utf-8'))
sock.send(f"JOIN {config.channel}\n".encode('utf-8'))

clf = SentimentClassifier()

def sendEmote(emote,canal=config.channel):
    sock.send((f'PRIVMSG {canal} :{emote}\n').encode())

n= count= suma= promedio = 0

while True:
    #sock.send((f'PRIVMSG {config.channel} :{"Inicio..."}\n').encode())

    f=clock()

    if f-n<100:

        r = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', sock.recv(2048).decode('utf-8'))
       
        if r:
            username, channel, message= r.groups()
            #print(f"Channel: {channel} \nUsername: {username} \nMessage: {message}")
            sentimiento = clf.predict(message)
            #print(sentimiento)
            count=count + 1
            suma = suma + sentimiento
            promedio = suma/count
    else:
               
        print(promedio) 
        if promedio>0 and promedio<0.1:
            sendEmote("BibleThump")
        elif promedio>=0.1 and promedio<0.25:
            sendEmote("WutFace")
        elif promedio>=0.25 and promedio<0.45:
            sendEmote("Kappa")
        elif promedio>=0.45 and promedio<=1.0:
            sendEmote("LUL")
                    
        n=f
        count = suma = 0

sock.close()


