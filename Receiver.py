from gpiozero import MCP3208
from time import sleep
tmp = MCP3208(channel=0, device=0)

while True:
    blightness = tmp.value
    print (round(blightness,5))
    sleep(0.5)