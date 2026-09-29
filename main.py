import spotipy
from spotipy.oauth2 import SpotifyOAuth
from langchain.tools import tool

from dotenv import load_dotenv
load_dotenv()

# Initialise authentication with the scopes needed to control playback and access user data 
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=load_dotenv("SPOTIPY_CLIENT_ID"),
    client_secret=load_dotenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=load_dotenv("SPOTIPY_REDIRECT_URI"),
    scope="user-modify_playback_state user-read-playback-state user-read-currently-playing user-library-read user-library-modify playlist-read-private playlist-modify-public playlist-modify-private"
))

@tool
def queue_up_spotify_track(track_id: str) -> str:
    """Use this tool to queue a specific song on the user's Spotify account using its track ID."""
    try:
        spotify.add_to_queue(uri=f"spotify:track:{track_id}")
        return "Song successfully queued"
    except Exception as e:
        return f"An error occurred while trying to queue the song: {str(e)}"
    
@tool
def pause_spotify_playback() -> str:
    """Use this tool to pause the active Spotify player"""
    spotify.pause_playback()
    return "Playback paused"
