import spotipy

# To access authorized Spotify data
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'ba98b97b650d4287bc97fd204e92e33f'
client_secret = '7acdbf4eaa3f4da8a0dee6d6698fd35b'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Spotify object to access API
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Chosen artist
name = "Oh Hiroshima"

result = sp.search(name)
(result['tracks']['items'][0]['artists'])