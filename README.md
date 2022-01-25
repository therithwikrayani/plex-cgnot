# plex-cgnot
A Python script to access Plex behind CGNAT using an ngrok tunnel.
<br>
You can use Plex behind CGNAT using an ngrok tunnel regularly, but you'll have to change Plex configuration every time you reboot and open a new tunnel.
Given that on a free ngrok plan, you don't get to choose the ngrok IP you're given, I opted to write a simple script to open a tunnel and set the tunnel IP in Plex.
<br>
Installation is described for Windows, but should work for other operating systems similarly.

# Installation

## Plex Media Server Setup
- Get and Setup Plex Media Server from https://www.plex.tv/media-server-downloads/#plex-media-server.
- Make sure you have some media.
- Disable Remote Access.
- Optimally set all quality settings to original.

## ngrok Setup
- Sign up for ngrok at https://dashboard.ngrok.com/signup
- Download ngrok for Windows.
- Unzip and run ngrok.exe.
- Connect your ngrok account as described in the ngrok dashboard. (Enter `ngrok authtoken XYZ` into the cmd window, replace `XYZ` with your actual authtoken). Close the window.
- Open the ngrok config file (`C:\Users\<Your Username>\.ngrok2\ngrok.yml`) with notepad and add in the region in a new line as `region: us` or equivalent as per these codes:
	- `us`: United States (Default)
	- `eu`: Europe
	- `ap`: Asia Pacific
	- `au`: Australia
	- `sa`: South Africa
	- `jp`: Japan
	- `in`: India
- Relaunch ngrok.exe and type in `ngrok tcp 32400`. You should see session status information. You may close the window.

## Python  Setup
- Go to https://www.python.org/downloads/ and install python 3 for your machine. Make sure to add Python to PATH.
- Go to cmd and type in the following:
  - `python --version` — you should see your python version.
  - `pip install --upgrade pip`
  - `pip install pyngrok`
  - `pip install plexapi`
  - `pip list` — you should see pyngrok and PlexAPI.
- You may close the window.

## The Final Stretch
- Go to any media in your Plex library.
- Go to the Kebab Menu (⋮)
- Click on `Get Info`
- Click on `View XML` — a new tab should open up.
- Go to the very end of the URL. You should see a 20 character string after `X-Plex-Token=`. Copy this string.
- Download `plex-ngrok-tunnel.py` from this GitHub repository. Right click and Edit with IDLE (or another editor if you're familiar).
- Go to line 6 and replace `<your-token-here>` with the copied string. (Make sure its in quotes). Save and Close.
- Now, run `plex-ngrok-tunnel.py`. As long as you keep this window open, you will have a way to Plex Media Server through a CGNAT thanks to an ngrok tunnel. I recommend leaving it open in another desktop.
- Plex should work now outside your network. If you go to Plex settings and then network, turn on advanced settings, you should see a URL in `Custom server access URLs`. 
- If you play from outside your network, you can get original quality, and it shows up as a local connection in Plex Dashboard.

# Troubleshooting
- Make sure Plex Media Server is open before running the script.
- You can only run one ngrok tunnel at a time with a free account, but there are no bandwidth caps.
- For any other help, do raise an issue in this repository.
