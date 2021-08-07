import urllib.request
import urllib.parse
import re
import webbrowser

#function for playing the track input

def play_music(track_name):
 
    #the request fro the url is made
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + track_name)

    #the track name(user input) is converted in to the youtube request  format for youtube
    search_results = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #the url is combined with the search results output above
    video_link = "https://www.youtube.com/watch?v=" + search_results[0]

    #the link is printed
    print(video_link)
    response='successful'
    #web browser is prompted.
    return webbrowser.open(video_link),response

   
