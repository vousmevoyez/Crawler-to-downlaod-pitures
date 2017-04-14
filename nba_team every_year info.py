# Player Info
start = time.clock()
SeasonType = ['Regular+Season']
#StatCategory=['PTS','REB','AST','BLK','STL']

for st in SeasonType:
    for year in xrange(1970,2016):
        url = 'http://stats.nba.com/stats/leaguedashplayerstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={}&SeasonSegment=&SeasonType={}&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision='\
                        .format(str(year)+'-'+str(year+1)[-2:],st)
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",\
                   'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
        r = requests.get(url,headers = headers)
        entries = r.json()
        for j in xrange(len(entries['resultSets'][0]['rowSet'])):
            player_id = entries['resultSets'][0]['rowSet'][j][0]
            common_url = 'http://stats.nba.com/stats/commonplayerinfo?LeagueID=00&PlayerID={}&SeasonType=Regular+Season'.format(player_id)
            by_year_stats_url = 'http://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID={}&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='.format(player_id)
            try:
                entry1 = requests.get(common_url,headers=headers).json()
                entry2 = requests.get(by_year_stats_url,headers=headers).json()
                filename1 = 'C:/Users/KrystalU/Documents/nba/players/common_info/'+str(player_id)+'.csv'
                filename2 = 'C:/Users/KrystalU/Documents/nba/players/by_year_stats/'+str(player_id)+'.csv'

                with open(filename1, 'wb') as f_output1:
                    csv_output1 = csv.writer(f_output1)
                    csv_output1.writerow(entry1['resultSets'][0]['headers'])
                    csv_output1.writerows(entry1['resultSets'][0]['rowSet'])

                with open(filename2, 'wb') as f_output2:
                    csv_output2 = csv.writer(f_output2)
                    csv_output2.writerow(entry2['resultSets'][1]['headers'])
                    csv_output2.writerows(entry2['resultSets'][1]['rowSet'])
            except Exception as e:
                print player_id

print time.clock()-start