import time
from pyngrok import ngrok
from plexapi.server import PlexServer

TOKEN = '<your-token-here>' # Make sure token is in quotes
PUBLIC_PORT = 32400 # 32400 is the default port for Plex, do not change unless you know what you're doing.

while True:        
    # Open ngrok tunnel
    tunnel = ngrok.connect(PUBLIC_PORT, "tcp")
    print('ngrok tunnel opened')

    # Set Plex Custom URL
    baseurl = 'http://localhost:' + str(PUBLIC_PORT)
    plex = PlexServer(baseurl, TOKEN)
    plex.settings.get('customConnections').set(tunnel.public_url)
    plex.settings.save()
    print('Plex custom URL set')

    time.sleep(4 * 3600) # Keep tunnel online, restart tunnel every 4 hours

    print('ngrok tunnel restarting')
    ngrok.disconnect(tunnel.public_url)
