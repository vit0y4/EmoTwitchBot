# EmoTwitchChatBot

Evalúa las emociones de los mensajes de chat de un canal de twitch en directo.

## Comenzando 

Proximamente será un archivo ejecutable, pero por ahora deberás bajar el EmoTwitchChatbot.py y ejecutarlo desde la consola con python. 
Deberás crear un archivo config.py donde debes colocar:

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'lacuentabot'
token = 'oauth:eltokendelacuentabot'
channel = '#elcanaldondeseharálaclasificación'

### Pre-requisitos 

EmoTwitchChatBot usa las siguientes librerías:

-socket (para conectar con el API de twitch)
-re (para decoding)
-classifier (para la clasificacion de los sentimientos de los mensajes del chat con SentimentClassifier)
-time (clock para contar el tiempo)

### Instalación 

No requiere instalación.

## Autores ✒️

## Licencia 📄



---
By [Vitoya](https://github.com/vit0y4)