from base64 import decode
from cgitb import html
from encodings.utf_8 import encode
from pickle import TRUE
import webbrowser
import os
import requests

def main():
    bemenet=open("bemenet.txt", "r", encoding='utf8')
    url=bemenet.readline()
    bemenet.readline() #empthy line
    
    r = requests.get("https://www.youtube.com/oembed?url=" + url, allow_redirects=True)
    open(os.path.dirname(__file__) + "\media\kimenet.json", 'wb').write(r.content)
    
    info=[(line[0:int(line.find("-"))-1],line[int(line.find("-"))+2:-1]) for line in bemenet]
    
    bemenet.close()
    
    links=[]
    
    kimenet=open("kimenet.html", "w", encoding='utf8')
    kimenet.write("")
    kimenet.close()
    #webbrowser.open(os.path.dirname(__file__) + "\kimenet.html")

if __name__=="__main__":
    main()