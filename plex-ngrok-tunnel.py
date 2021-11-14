import time
import socket
from pyngrok import ngrok
from plexapi.server import PlexServer

TOKEN = '<your-token-here>' # Make sure token is in quotes
PUBLIC_PORT = 32400 # 32400 is the default port for Plex, do not change unless you know what you're doing.

while True:
    # Open ngrok tunnel
    tunnel = ngrok.connect(PUBLIC_PORT, "tcp")              # tunnel = tcp://abc:xyz
    url = tunnel.public_url[6:].split(":")[0]               # url = abc
    ip = socket.gethostbyname(url)                          # ip = gethostbyname(abc) = 123
    port = tunnel.public_url[6:].split(":")[1]              # port = xyz
    public_url = "https://" + ip + ":" + port               # public_url = https://123:xyz
    print('ngrok tunnel opened')

    # Set Plex Custom URL
    private_url = 'http://localhost:' + str(PUBLIC_PORT)
    plex = PlexServer(private_url, TOKEN)
    plex.settings.get('customConnections').set(public_url)
    plex.settings.save()
    print('Plex custom URL set')

    time.sleep(12 * 3600) # Keep tunnel online, restart tunnel every 12 hours

    print('ngrok tunnel restarting')
    ngrok.disconnect(public_url)
