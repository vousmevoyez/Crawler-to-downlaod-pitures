# Team common info
team_id_url = 'http://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision='
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",\
                   'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
r = requests.get(team_id_url,headers=headers)
entries = r.json()
team_dict = {}

def transform(s):
    if type(s) is int:
        return s
    return s.encode('utf-8')

for i in xrange(len(entries['resultSets'][0]['rowSet'])):
    team_dict[entries['resultSets'][0]['rowSet'][i][0]] = entries['resultSets'][0]['rowSet'][i][1]
    
for t_id in team_dict:
    team_common_url = 'http://stats.nba.com/stats/teamdetails?teamID={}'.format(t_id)
    r2 = requests.get(team_common_url,headers=headers)
    entries2 = r2.json()
    filename2 = 'C:/Users/KrystalU/Documents/nba/teams/common_info/'+str(team_dict[t_id])+'.csv'

    with open(filename2, 'wb') as f_output2:
        csv_output2 = csv.writer(f_output2)
        csv_output2.writerow(entries2['resultSets'][0]['headers'])
        csv_output2.writerow(map(transform,entries2['resultSets'][0]['rowSet'][0]))