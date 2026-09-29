# spotify-agent
Creating an agent for Spotify. This will have a personalised Spotify DJ, semantic LLM

# Setup
## Spotify Keys
Go to the spotify developers website: `https://developer.spotify.com/` and create an app. This is where you'll create your access ID and Secret keys. Create a `.env` file and add these keys:

```
SPOTIFY_CLIENT_ID="your access id"
SPOTIFY_CLIENT_SECRET="your secret key"
SPOTIFY_REDIRECT_URI="your redirect url entered when creating spotify app"
```
__Note: ensure before you commit anything that the `.gitignore` includes your `.env` file, otherwise your secrets will be committed to github!__

## Install the Dependencies
Open terminal and install the python libraries using the command:
```
pip install -r requirements.txt
```
