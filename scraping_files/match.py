import pymysql
import bs4
import requests 
#import python_mysql_dbconfig
urls0 = ['http://www.espncricinfo.com/series/8048/scorecard/1136561/mumbai-indians-vs-chennai-super-kings-1st-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136562/kings-xi-punjab-vs-delhi-daredevils-2nd-match-indian-premier-league-2018' ,'http://www.espncricinfo.com/series/8048/scorecard/1136563/kolkata-knight-riders-vs-royal-challengers-bangalore-3rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136564/sunrisers-hyderabad-vs-rajasthan-royals-4th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136565/chennai-super-kings-vs-kolkata-knight-riders-5th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136566/rajasthan-royals-vs-delhi-daredevils-6th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136567/sunrisers-hyderabad-vs-mumbai-indians-7th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136568/royal-challengers-bangalore-vs-kings-xi-punjab-8th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136569/mumbai-indians-vs-delhi-daredevils-9th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136570/kolkata-knight-riders-vs-sunrisers-hyderabad-10th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136571/royal-challengers-bangalore-vs-rajasthan-royals-11th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136572/kings-xi-punjab-vs-chennai-super-kings-12th-match-indian-premier-league-2018' ,'http://www.espncricinfo.com/series/8048/scorecard/1136573/kolkata-knight-riders-vs-delhi-daredevils-13th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136574/mumbai-indians-vs-royal-challengers-bangalore-14th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136575/rajasthan-royals-vs-kolkata-knight-riders-15th-match-indian-premier-league-2018', 'http://www.espncricinfo.com/series/8048/scorecard/1136576/kings-xi-punjab-vs-sunrisers-hyderabad-16th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136577/chennai-super-kings-vs-rajasthan-royals-17th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136578/kolkata-knight-riders-vs-kings-xi-punjab-18th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136579/royal-challengers-bangalore-vs-delhi-daredevils-19th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136580/sunrisers-hyderabad-vs-chennai-super-kings-20th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136581/rajasthan-royals-vs-mumbai-indians-21st-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136582/delhi-daredevils-vs-kings-xi-punjab-22nd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136583/mumbai-indians-vs-sunrisers-hyderabad-23rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136584/royal-challengers-bangalore-vs-chennai-super-kings-24th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136585/sunrisers-hyderabad-vs-kings-xi-punjab-25th-match-indian-premier-league-2018' ]
urls1 = ['http://www.espncricinfo.com/series/8048/scorecard/1136586/delhi-daredevils-vs-kolkata-knight-riders-26th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136587/chennai-super-kings-vs-mumbai-indians-27th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136588/rajasthan-royals-vs-sunrisers-hyderabad-28th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136589/royal-challengers-bangalore-vs-kolkata-knight-riders-29th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136590/chennai-super-kings-vs-delhi-daredevils-30th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136590/chennai-super-kings-vs-delhi-daredevils-30th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136592/delhi-daredevils-vs-rajasthan-royals-32nd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136593/kolkata-knight-riders-vs-chennai-super-kings-33rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136594/kings-xi-punjab-vs-mumbai-indians-34th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136595/chennai-super-kings-vs-royal-challengers-bangalore-35th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136596/sunrisers-hyderabad-vs-delhi-daredevils-36th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136597/mumbai-indians-vs-kolkata-knight-riders-37th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136598/kings-xi-punjab-vs-rajasthan-royals-38th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136599/sunrisers-hyderabad-vs-royal-challengers-bangalore-39th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136599/sunrisers-hyderabad-vs-royal-challengers-bangalore-39th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136601/kolkata-knight-riders-vs-mumbai-indians-41st-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136601/kolkata-knight-riders-vs-mumbai-indians-41st-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136603/rajasthan-royals-vs-chennai-super-kings-43rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136603/rajasthan-royals-vs-chennai-super-kings-43rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136603/rajasthan-royals-vs-chennai-super-kings-43rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136603/rajasthan-royals-vs-chennai-super-kings-43rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136607/mumbai-indians-vs-rajasthan-royals-47th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136608/kings-xi-punjab-vs-royal-challengers-bangalore-48th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136609/kolkata-knight-riders-vs-rajasthan-royals-49th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136610/mumbai-indians-vs-kings-xi-punjab-50th-match-indian-premier-league-2018']
urls2 = ['http://www.espncricinfo.com/series/8048/scorecard/1136611/royal-challengers-bangalore-vs-sunrisers-hyderabad-51st-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136612/delhi-daredevils-vs-chennai-super-kings-52nd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136613/rajasthan-royals-vs-royal-challengers-bangalore-53rd-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136614/sunrisers-hyderabad-vs-kolkata-knight-riders-54th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136615/delhi-daredevils-vs-mumbai-indians-55th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136616/chennai-super-kings-vs-kings-xi-punjab-56th-match-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136617/sunrisers-hyderabad-vs-chennai-super-kings-qualifier-1-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136618/kolkata-knight-riders-vs-rajasthan-royals-eliminator-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136619/kolkata-knight-riders-vs-sunrisers-hyderabad-qualifier-2-indian-premier-league-2018','http://www.espncricinfo.com/series/8048/scorecard/1136620/chennai-super-kings-vs-sunrisers-hyderabad-final-indian-premier-league-2018']
urls = [ urls0,urls1,urls2]

def Matches(url, cursor):
    #Soup Object
    sauce = requests.get(url)
    soup = bs4.BeautifulSoup(sauce.text, 'lxml')

    #FIND NAMES OF TEAMS
    team_list = []
    for name in soup.find_all('a', {'class':'app_partial'}):
        # print(name)
        for teams in name.find_all('span', {'class' : 'cscore_name cscore_name--short'}):
            # print(teams)
            for team in teams:
                team_list.append(str(team.string))
    #FIND ID OF TEAM
    cursor.execute("select team_id from team where name = '" + team_list[0] + "'")
    team1_id = cursor.fetchone()[0]
    cursor.execute("select team_id from team where name = '" + team_list[1] + "'")
    team2_id = cursor.fetchone()[0]

    #FIND GROUND
    name = ((soup.find('div', {'class' : 'stadium-details'})).find('a')).find('span').string.split(',')[0]
    cursor.execute("select venue from team where name = '" + team_list[0] + "'")
    team1_ground = cursor.fetchone()[0]
    if name.split()[0] in team1_ground :
        ground_id = team1_id
    else :
        ground_id = team2_id

    #FIND DATES
    dates = soup.find_all('div', {'class':'match-detail--left'})
    i = 1
    for date in dates:
        if 'days' in date.find('h4').string:
            break
        i += 1
    j = 1
    for date in soup.find_all('div', {'class':'match-detail--right'}):
        if j == i:
            days = date.find('span').string
            break
        j += 1
    items = days.split()
    months = {"January":'01', "February":'02', "March":'03', "April":'04', "May":'05', "June":'06', "July":'07',"August":'08', "September":'09',"October":'10', "November":'11', "December":'12'}
    date = items[2] + "-" + months[items[1]] + "-" + items[0].split(',')[0]



    #FIND TOSS and DECISION BAT = 1, FIELD = 0
    tosses = soup.find_all('div', {'class':'match-detail--left'})
    i = 1
    for toss in tosses:
        if toss.find('h4').string == 'Toss':
            break
        i += 1
    tosses = soup.find_all('div', {'class':'match-detail--right'})
    j = 1
    for toss in tosses:
        if j == i:
            s = toss.find('span').string.split(',')
            break
        j += 1
    if s[0].strip() == team_list[0]:
        toss = team1_id
        loss = team2_id
    else:
        toss = team2_id
        loss = team1_id

    if 'bat' in s[1]:
        batfirst = toss
    else:
        batfirst = loss

    #FIND WINNING TEAM
    team = soup.find_all('span', {'class' : 'cscore_notes_game'})[1].string.split()[0]
    d = {'Delhi Daredevils':'DD', 'Chennai Super Kings': 'CSK', 'Kings XI Punjab':'KXIP', 'Kolkata Knight Riders':'KKR', 'Mumbai Indians':'MI', 'Rajasthan Royals':'RR', 'Royal Challengers Bangalore':'RCB', 'Sunrisers Hyderabad':'SRH'}
    if team in team_list[0] or team in d[team_list[0]]:
        team_won = team1_id
    else:
        team_won = team2_id

    return (team1_id, team2_id, ground_id, date, toss, batfirst, team_won)


def connect():
    #Connect to Database
    conn = pymysql.connect(host='localhost', database='cricket', user='root', password='')
    cursor = conn.cursor()

    for links in urls:
        for url in links:
            data = Matches(url, cursor)
            print(data)
            cursor.execute("INSERT INTO matches(team1_id, team2_id, ground_id, dates, toss, batfirst, team_won) VALUES(%s, %s, %s,DATE %s, %s, %s, %s);",data)
    conn.commit()
    cursor.close()
    conn.close()


connect()



