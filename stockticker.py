import pusherclient
import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

xar = []
yar = []

def connect_handler(data): #this gets called when the Pusher connection is established
    trades_channel = pusher.subscribe("live_trades")
    trades_channel.bind('trade', trade_callback)

def trade_callback(data): #some callbacs to do something when the event occours
    y = json.loads(data)['price']
    yar.append(y)
    xar.append(len(yar))
    print y

pusher = pusherclient.Pusher('de504dc5763aeef9ff52')
pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    ax1.clear()
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig,animate, interval=1000)
plt.show()

raw_input()
