from cgitb import html
import webbrowser
import os

def main():
    ##kimenet=open("kimenet.html", "w")
    ##kimenet.write()
    ##kimenet.close()
    webbrowser.open(os.path.dirname(__file__) + "\media\kimenet.html")
    a=webbrowser.get("https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=lr3y5deXNQU&format=json")
    print(a)


    url = 'https://www.facebook.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)

    open('facebook.ico', 'wb').write(r.content)

if __name__=="__main__":
    main()