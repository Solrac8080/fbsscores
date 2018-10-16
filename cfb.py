import urllib.request, json, time, os, threading
from threading import Thread
def getrelevantscores(data):
    games=[]
    for i in range(len(data)):
        if("groups" in data[i]["competitions"][0]):
            if(data[i]["competitions"][0]["groups"]["shortName"]=="Big 12" or data[i]["competitions"][0]["competitors"][0]["curatedRank"]["current"]<26 or data[i]["competitions"][0]["competitors"][1]["curatedRank"]["current"]<26):
                games.append(data[i])
    file="index.html"
    f=open(file,"w+")
    linestowrite=[]
    linestowrite.append("<style>table {font-family: arial, sans-serif;font-size: 12px;border-collapse: collapse;width: auto;}td, th {border: 1px solid #dddddd;padding: 1px;}.table td,.table th{text-align:right;}.table td + td,.table th + th{text-align:left}</style>")
    linestowrite.append("<table>")
    i=0
    while(i<(len(games))):
        home=games[i]["competitions"][0]["competitors"][0]
        away=games[i]["competitions"][0]["competitors"][1]
        if(home["curatedRank"]["current"]<26):
            home["curatedRank"]["actual"]=str(home["curatedRank"]["current"])
        else:
            home["curatedRank"]["actual"] = ""
        if(away["curatedRank"]["current"]<26):
            away["curatedRank"]["actual"]=str(away["curatedRank"]["current"])
        else:
            away["curatedRank"]["actual"] = ""
        #linestowrite.append(home["team"]["abbreviation"]+": "+home["score"]+away["team"]["abbreviation"]+": "+away["score"])
        linestowrite.append("<tr>")
        linestowrite.append("<td>"+games[i]["competitions"][0]["status"]["type"]["description"]+"</td>")
        linestowrite.append("<td>"+games[i]["competitions"][0]["status"]["displayClock"]+"</td>")
        linestowrite.append("<td></td>")
        linestowrite.append("</tr>")
        linestowrite.append("<tr>")
        linestowrite.append("<td>"+home["curatedRank"]["actual"]+"</td>")
        linestowrite.append("<td>"+home["team"]["location"]+"</td>")
        linestowrite.append("<td>"+home["score"]+"</td>")
        linestowrite.append("</tr>")
        linestowrite.append("<tr>")
        linestowrite.append("<td>"+away["curatedRank"]["actual"]+"</td>")
        linestowrite.append("<td>"+away["team"]["location"]+"</td>")
        linestowrite.append("<td>"+away["score"]+"</td>")
        linestowrite.append("</tr>")
        linestowrite.append("<tr>")
        linestowrite.append("<td></td>")
        linestowrite.append("<td></td>")
        linestowrite.append("<td></td>")
        linestowrite.append("</tr>")
        i=i+1
    linestowrite.append("<div>last updated: \n"+time.strftime("%b %d %I:%M%p%Z</div>"))
    f.writelines(linestowrite)
    print("writing index.html")
    f.close()
        


def getscores(season, week):
    with urllib.request.urlopen("http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?lang=en&region=us&calendartype=blacklist&limit=300&dates="+season+"&seasontype=2&week="+week+"&groups=80") as url:
        data = json.loads(url.read().decode())
        return getrelevantscores(data["events"])
def aa():
    while(True):
        getscores("2018", "8")
        print('waiting 60 seconds...')
        time.sleep(59)

import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 5000))

Handler = http.server.SimpleHTTPRequestHandler
def ab():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    Thread(target = aa).start()
    Thread(target = ab).start()

