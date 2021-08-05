import requests

from lyrics_api import *



def searchalbum():
 while True: 
#user in put of the artist and the album of the artist
        print("Whats's the name of the artist?")
        artist_name = input("> ")
        print("What's the name of the album?")
        album_name = input("> ")
# Api call is made to get the user request and retrieves data from musixmatch using requests
        api_call = base_url + album_tracks  + format_url + artist_search_parameter + artist_name + album_tracks_parameters +album_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
#print the Api call and the album
        print("API Call: " + api_call)
        print()
        print(data)
#display the error message if song is not found
        exit = input("Do you want to search another album (y/n)? ")
        if exit.lower() == 'n':
                break



 