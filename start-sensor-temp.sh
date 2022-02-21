#!/usr/bin/env bash
cd /home/pi/monitor-temperatura/server
nohup sudo node /home/pi/monitor-temperatura/server/index.js >/dev/null 2>&1 &
cd /
#Startando o Ambiente Virtual do Python
source monitor-temperatura/venv/bin/activate

#python /home/pi/monitor-temperatura/exemplo.py

python3 /home/pi/monitor-temperatura/temperatura.py

#node /home/pi/monitor-temperatura/server/index.js
