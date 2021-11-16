# VitoIA (antes EmoTwitchChatBot)

Proyecto personal para atender directos de twitch mientras trabajo.
La idea principal es monitorear el chat para hacer diferentes cosas.

## Comenzando 

Deberás crear un archivo config.py donde debes colocar:

server = 'irc.chat.twitch.tv'

port = 6667

nickname = 'lacuentabot'

token = 'oauth:eltokendelacuentabot'

channel = '#elcanaldondeseharálaclasificación'


### Pre-requisitos 

EmoTwitchChatBot usa las siguientes librerías:

- socket (para conectar con el API de twitch)

- re (para decoding)

- classifier (para la clasificacion de los sentimientos de los mensajes del chat con SentimentClassifier)

- time (clock para contar el tiempo)


### Instalación 

No requiere instalación.

## Autores 

## Licencia 



---
By [Vitoya](https://github.com/vit0y4)