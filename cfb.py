import urllib.request, json, time
def getrelevantscores(data):
    games=[]
    for i in range(len(data)):
        if("groups" in data[i]["competitions"][0]):
            if(data[i]["competitions"][0]["groups"]["shortName"]=="Big 12" or data[i]["competitions"][0]["competitors"][0]["curatedRank"]["current"]<26 or data[i]["competitions"][0]["competitors"][1]["curatedRank"]["current"]<26):
                games.append(data[i])
    file="index.html"
    f=open(file,"w+")
    linestowrite=[]
    i=0
    while(i<(len(games))):
        home=games[i]["competitions"][0]["competitors"][0]
        away=games[i]["competitions"][0]["competitors"][1]
        if(home["curatedRank"]["current"]<26):
            home["team"]["abbreviation"]=str(home["curatedRank"]["current"])+" "+home["team"]["abbreviation"]
        if(away["curatedRank"]["current"]<26):
            away["team"]["abbreviation"]=str(away["curatedRank"]["current"])+" "+away["team"]["abbreviation"]
            
        linestowrite.append(home["team"]["abbreviation"]+":	"+home["score"]+"\n"+away["team"]["abbreviation"]+":	"+away["score"]+'\n\n')
        i=i+1
    linestowrite.append("last updated: \n"+time.strftime("%b %d %I:%M%p"))
    f.writelines(linestowrite)
    f.close()
        


def getscores(season, week):
    with urllib.request.urlopen("http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?lang=en&region=us&calendartype=blacklist&limit=300&dates="+season+"&seasontype=2&week="+week+"&groups=80") as url:
        data = json.loads(url.read().decode())
        return getrelevantscores(data["events"])
#while(True):
#    getscores("2018", "8")
#    print('waiting 60 seconds...')
#    time.sleep(59)
getscores("2018", "8")

import http.server
import socketserver

PORT = int(os.environ.get("PORT", 5000))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
