import configparser
import socket
import re
from sentiment_analysis_spanish import sentiment_analysis
import time
from time import clock

sock = socket.socket()

config = configparser.ConfigParser()
config.read('config.ini')
token=config['config']['token']
nickname=config['config']['nickname']
channel=config['config']['channel']
server=config['config']['server']
port=int(config['config']['port'])

sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

sock.send((f'PRIVMSG {channel} :{"Cargando IA..."}\n').encode())
time.sleep(5)
sock.send((f'PRIVMSG {channel} :{"Carga completada Kappa"}\n').encode())

clf = sentiment_analysis.SentimentAnalysisSpanish()

def sendEmote(emote,canal=channel):
    sock.send((f'PRIVMSG {canal} :{emote}\n').encode())

n= count= suma= promedio = 0

while True:
    f = time.perf_counter()
    print(f'inicio {f}')
    #f=clock()
    soc = sock.recv(2048).decode('utf-8')
    if soc.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    r = re.search(r':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', soc)
    
    if r:
        username, channel, message= r.groups()
        #print(f"Channel: {channel} \nUsername: {username} \nMessage: {message}")
        message=message.rstrip('\r\n')
        if message=="!finalizar" and username =="vitoya":
            sock.send((f'PRIVMSG {channel} :{"Adiós."}\n').encode())
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            break
        
        
        sentimiento = clf.sentiment(message)
        print(f'sentimiento por mensaje {sentimiento}')
        count=count + 1
        suma = suma + sentimiento
        promedio = suma/count
    
    #n=time.perf_counter()
    #print(n)
    print(f'diferencia {time.perf_counter()-f}')
    if time.perf_counter()-f > 100:
               
        print(f'promedios {promedio}') 
        if promedio>0 and promedio<0.1:
            sendEmote("BibleThump")
        elif promedio>=0.1 and promedio<0.25:
            sendEmote("WutFace")
        elif promedio>=0.25 and promedio<0.45:
            sendEmote("Kappa")
        elif promedio>=0.45 and promedio<=1.0:
            sendEmote("LUL")
                    
        #n=f
        count = suma = 0
sock.close()


