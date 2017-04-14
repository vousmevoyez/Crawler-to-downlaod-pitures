# Match Info
from datetime import date, timedelta as td

start = time.clock()
d1 = date(2002, 7, 1)
d2 = date(2016, 7, 1)

delta = d2 - d1

for i in range(delta.days + 1):
    time = d1 + td(days=i)
    year = time.year
    month = time.month
    day = time.day
    
    if month == 8: continue
    
    url = 'http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate={0}%2F{1}%2F{2}'.format(month,day,year)
    params = {
        'DayOffset':"0",
        'LeagueID':"00",
        'gameDate':"{}/{}/{}".format(month,day,year)
    }

    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
        'Accept':"application/json, text/plain, */*",
        'Referer':"http://stats.nba.com/scores/",
    }
    r1 = requests.get(url,headers = headers,params=params)
    entry4 = r1.json()
    if not entry4['resultSets'][1]['rowSet']:
        continue
    else:
        try:
            for j in xrange(len(entry4['resultSets'][0]['rowSet'])):
                game_id = entry4['resultSets'][0]['rowSet'][j][2]
                match_season = '{}-{}'.format(year,str(year+1)[-2:])

                team_url = 'http://stats.nba.com/stats/boxscoresummaryv2?GameID={}'.format(game_id)
                player_url = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID={}&RangeType=0&Season={}&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'\
                            .format(game_id,match_season)

                match_path = 'C:/Users/KrystalU/Documents/nba/new_match/{}/'.format(game_id)
                os.makedirs(match_path)

                r4 = requests.get(team_url,params=params,headers=headers)
                entry6 = r4.json()  
                boxscore = match_path + 'boxscore' + '.csv'
                other_stats = match_path + 'other_stats' + '.csv'
                player_stats = match_path + 'player_stats' + '.csv'
                temp1 = {boxscore:5,other_stats:1}

                for subfile in temp1:
                    with open(subfile, 'wb') as f_output6:
                        csv_output = csv.writer(f_output6)
                        csv_output.writerow(entry6['resultSets'][temp1[subfile]]['headers'])
                        csv_output.writerows(entry6['resultSets'][temp1[subfile]]['rowSet'])

                r5 = requests.get(player_url,params=params,headers=headers)
                entry7 = r5.json()
                player_csv = match_path + 'player_stats' + '.csv'

                with open(player_csv, 'wb') as f_output7:
                    csv_output = csv.writer(f_output7)
                    csv_output.writerow(entry7['resultSets'][0]['headers'])
                    csv_output.writerows(entry7['resultSets'][0]['rowSet'])
        except Exception as e:
            print year,month,day

print time.clock() - start