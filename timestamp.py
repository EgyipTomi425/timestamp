from base64 import decode
from cgitb import html
from encodings.utf_8 import encode
from pickle import TRUE
import webbrowser
import os
import requests
import json

def time_calculate(list_of_touple):
    index=0
    torlesszam=0
    try:
        while True:
            if str(list_of_touple[index][0]).replace(":","1").isnumeric():
                if count_substring(list_of_touple[index][0],":")==1:
                    list_of_touple[index]=timeconvert(list_of_touple[index],"m")
                elif count_substring(list_of_touple[index][0],":")==0:
                    list_of_touple[index]=timeconvert(list_of_touple[index],"s")
                elif count_substring(list_of_touple[index][0],":")==2:
                    list_of_touple[index]=timeconvert(list_of_touple[index],"h")
                index=index+1
            else:
                del list_of_touple[index]
    except:
        index=index

def link_calculate(list_of_touple,ylink):
    index=0
    for i in list_of_touple:
        list_of_touple[index]=(list_of_touple[index][0],list_of_touple[index][1],ylink+"&t="+str(list_of_touple[index][2])+"s")
        index=index+1

def count_substring(string, sub_string):
    count=0
    len_sub=len(sub_string)
    for i in range(0,len(string)):
        if(string[i:i+len_sub]==sub_string):
            count+=1
    return count

def timeconvert(mytouple,string):
    time=mytouple[0]
    ylinktime=int(0)
    sec=int(0)
    min=int(0)
    hour=int(0)
    if string=="s":
        sec=int(time)
    elif string=="m":
        min=int(time[0:time.find(":")])
        sec=int(time[time.find(":")+1:])
    elif string=="h":
        hour=int(time[0:time.find(":")])
        min=int(time[time.find(":")+1:][0:time[time.find(":")+1:].find(":")])
        sec=int(time[time.find(":")+1:][time[time.find(":")+1:].find(":")+1:])
    time=secconvert(str(hour*3600+min*60+sec))
    ylinktime=hour*3600+min*60+sec
    return (time,mytouple[1],ylinktime)

def secconvert(string):
    time=int(string)
    if time<60:
        if len(string)<2:
            return "00:0" + str(time)
        else:
            return "00:" + str(time)
    elif time<3600:
        if len(str(int(time/60)))<2:
            if(len(str((time-int(time/60)*60)))<2):
                return "0" + str(int(time/60)) + ":0" + str((time-int(time/60)*60))
            else:
                return "0" + str(int(time/60)) + ":" + str((time-int(time/60)*60))
        else:
            if(len(str((time-int(time/60)*60)))<2):
                return str(int(time/60)) + ":0" + str((time-int(time/60)*60))
            else:
                return str(int(time/60)) + ":" + str((time-int(time/60)*60))
    else:
            ora=str(int(time/3600))
            time=time-int(time/3600)*3600
            if time<60:
                if len(string)<2:
                    return ora + ":" + "00:0" + str(time)
                else:
                    return ora + ":" + "00:" + str(time)
            elif time<3600:
                if len(str(int(time/60)))<2:
                    if(len(str((time-int(time/60)*60)))<2):
                        return ora + ":" + "0" + str(int(time/60)) + ":0" + str((time-int(time/60)*60))
                    else:
                        return ora + ":" + "0" + str(int(time/60)) + ":" + str((time-int(time/60)*60))
                else:
                    if(len(str((time-int(time/60)*60)))<2):
                        return ora + ":" + str(int(time/60)) + ":0" + str((time-int(time/60)*60))
                    else:
                        return ora + ":" + str(int(time/60)) + ":" + str((time-int(time/60)*60))

def sorgen(ido,cim,link):
    return '''
            <tr>
                <td>''' + ido + '''</td>
                <th>''' + cim + '''</th>
                <td><a target="_blank" rel="noopener noreferrer" href="''' + link + '''">'''+ link + '''</a></td>
            </tr>
            '''

def listagen(list_of_touple):
    kimenet=""
    for i in list_of_touple:
        kimenet=kimenet+sorgen(i[0],i[1],i[2])
    return kimenet

def main():
    bemenet=open("bemenet.txt", "r", encoding='utf8')
    url=bemenet.readline()[0:-1]
    if (url.find("https://www.youtube.com/watch?v=")==-1 or count_substring(url,"?")!=1 or url.find("&")!=-1 or count_substring(url,"=")!=1):
        print("Hibás link!")
        exit()
    
    r = requests.get("https://www.youtube.com/oembed?url=" + url, allow_redirects=True)
    open(os.path.dirname(__file__) + "\media\kimenet.json", 'wb').write(r.content)
    
    info=[(line[0:line.find(" ")],line[line.find(" ")+1:-1],"") if line.find(" ")!=-1 else (line[0:-1],"Névtelen","") for line in bemenet]
    
    bemenet.close()
    
    time_calculate(info)
    link_calculate(info,url)
    
    with open(os.path.dirname(__file__) + "\media\kimenet.json", 'r') as json_file:
        json_load = json.load(json_file)
    
    szovegkimenet = open('szovegkimenet.txt', 'w')
    line=' '.join("Cím: " + json_load["title"])
    szovegkimenet.write(line + '\n' + '\n')
    for i in info:
        line=' '.join(str(x) for x in i)
        szovegkimenet.write(line + '\n')
    szovegkimenet.close()
    
    htmlkimenet='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./media/megjelenito.css">
    <title>YouTube Timestamp</title>
</head>
<body>
    <table class="main">
        <thead>
            <tr>
                <th colspan="3">Menyhárt Tamás</th>
            </tr>
            <tr>
                <td colspan="3"><a target="_blank" rel="noopener noreferrer" href="''' + url + '''">''' + url + '''</a></td>
            </tr>
            <tr>
                <th colspan="3">''' + json_load["title"] + '''</>
            </tr>
        </thead>
        <tbody>'''
    htmlkimenet=htmlkimenet + listagen(info)
    htmlkimenet=htmlkimenet + '''</tbody>
    </table>
</body>
</html>'''
    
    kimenet=open("kimenet.html", "w", encoding='utf8')
    kimenet.write(htmlkimenet)
    kimenet.close()
    webbrowser.open(os.path.dirname(__file__) + "\kimenet.html")

if __name__=="__main__":
    main()