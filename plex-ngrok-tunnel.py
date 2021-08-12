import time
import socket
from pyngrok import ngrok
import plexapi
from plexapi.server import PlexServer

# Open ngrok tunnel
tunnel = ngrok.connect(32400, "tcp")
url = tunnel.public_url[6:].split(":")[0]
ip = socket.gethostbyname(url)
port = tunnel.public_url[6:].split(":")[1]
full_ip = "https://" + ip + ":" + port

print('ngrok tunnel opened')

# Set Plex Custom URL
baseurl = 'http://localhost:32400'
token = '<your-token-here>'
plex = PlexServer(baseurl, token)
plex.settings.get('customConnections').set(full_ip)
plex.settings.save()

print('Plex custom URL set')

while True:
    time.sleep(3600)
