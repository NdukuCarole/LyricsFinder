import requests
from lyrics_api import *
from playsong import play_music


def searchsong():


 while True: 
        print("Whats's the name of the artist?")
        artist_name = input("> ")
        print("What's the name of the track?")
        track_name = input("> ")
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']

        print("API Call: " + api_call)
        print()
        print(data['lyrics']['lyrics_body'])


        print()
        choice = input('''
                                1:play song \n
                                2:exit\n
                                
                                please enter your choice\n''')
#prompt the browser to play the youtube song
        if choice == "1":
         play_music(track_name)
        elif choice == "2":
        #the program is terminated
             break

        else:
                exit = input("Do you want to search another song (y/n)? ")
        if exit.lower() == 'n':
                break
        
     







           
    

   


 



             
    