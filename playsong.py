import urllib.request
import urllib.parse
import re


def play_music(track_name):
 

    query_string = urllib.parse.urlencode({"search_query" : track_name})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("https://www.youtube.com/watch?v=" + search_results)
   