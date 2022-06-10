import statsapi
import json
import sqlalchemy
import psycopg2


db = sqlalchemy.create_engine(
    'postgresql://postgres:a0E24me@localhost:5432/mlb')


teams = {
    # ======================== NATIONAL LEAGUE ========================
    # NL WEST
    "Diamondbacks": 109,
    "Rockies": 115,
    "Dodgers": 119,
    "Padres": 135,
    "Giants": 137,
    # NL CENTRAL
    "Cubs": 112,
    "Reds": 113,
    "Pirates": 134,
    "Cardinals": 138,
    "Brewers": 158,
    # NL EAST
    "Nationals": 120,
    "Mets": 121,
    "Phillies": 143,
    "Braves": 144,
    "Marlins": 146,
    # ======================== AMERICAN LEAGUE ========================
    # AL WEST
    "Angels": 108,
    "Athletics": 133,
    "Astros": 117,
    "Mariners": 136,
    "Rangers": 140,
    # AL CENTRAL
    "Guardians": 114,
    "Tigers": 116,
    "Royals": 118,
    "Twins": 142,
    "White Sox": 145,
    # AL EAST
    "Orioles": 110,
    "Red Sox": 111,
    "Rays": 139,
    "Blue Jays": 141,
    "Yankees": 147,
}


# GET LAST GAME ID FOR TEAM
lastGame = statsapi.last_game(teams["Giants"])
# print("Giants last game: ", lastGame)

# BOXSCORE DICTIONARY
boxscore = statsapi.boxscore_data(lastGame, timecode=None)
# print(json.dumps(boxscore))
# print(boxscore["gameId"])

MLBGameID = boxscore["gameId"]
gameDate = MLBGameID[0: 10]
print(gameDate)

# Returns home team stats and player stats
# print(json.dumps(boxscore["home"]))
# sqlStatment_GAME = 'INSERT INTO player (id, date, home_team, away_team, home_team_runs, away_team_runs, home_team_starting_pitcher, away_team_starting_pitcher) VALUES ($1, $2, $3, $4, $5, $6, $7, $8);'


awayTeamID = boxscore["away"]["team"]["id"]
awayTeamBattingStats = boxscore["away"]["teamStats"]["batting"]
awayAVG = float(awayTeamBattingStats["avg"])
awayOBP = float(awayTeamBattingStats["obp"])
awaySLG = float(awayTeamBattingStats["slg"])
awayOPS = float(awayTeamBattingStats["ops"])

awayTeamPitchingStats = boxscore["away"]["teamStats"]["pitching"]
awayOBP = float(awayTeamPitchingStats["obp"])
awayERA = float(awayTeamPitchingStats["era"])
# awayTeamPitchingStats["inningsPitched"] = float(awayTeamPitchingStats["inningsPitched"])


homeTeamID = boxscore["home"]["team"]["id"]

homeTeamBattingStats = boxscore["away"]["teamStats"]["batting"]
homeAVG = float(awayTeamBattingStats["avg"])
homeOBP = float(awayTeamBattingStats["obp"])
homeSLG = float(awayTeamBattingStats["slg"])
homeOPS = float(awayTeamBattingStats["ops"])

homeTeamPitchingStats = boxscore["away"]["teamStats"]["pitching"]
homeOBP = float(awayTeamPitchingStats["obp"])
homeERA = float(awayTeamPitchingStats["era"])


# print(json.dumps(awayTeamBattingStats))
# print(json.dumps(awayTeamPitchingStats))


# print(json.dumps(homeTeamBattingStats))
# print(json.dumps(homeTeamPitchingStats))

conn = psycopg2.connect(dbname="mlb", user="postgres",
                        password="a0E24me", host="localhost")
cur = conn.cursor()
sqlStatement_PLAYER = 'INSERT INTO player (id, full_name, number, position, ba, team) VALUES (%s, %s, %s, %s, %s, %s);'


# awayTeamPlayerStats = boxscore["away"]["players"]
# for key in awayTeamPlayerStats:
#     player = awayTeamPlayerStats[key]
#     playerID = player["person"]["id"]
#     playerName = player["person"]["fullName"]
#     jerseyNumber = player["jerseyNumber"]
#     position = player["position"]["abbreviation"]
#     team = player["parentTeamId"]
#     awayBattingStats_GAME = player["stats"]["batting"]
#     awayPitchingStats_GAME = player["stats"]["pitching"]
#     awayBattingStats_SEASON = player["seasonStats"]["batting"]
#     awayPitchingStats_SEASON = player["seasonStats"]["pitching"]
#     ba_SEASON = float(awayBattingStats_SEASON["avg"])
#     print(playerID)
#     print(awayBattingStats_SEASON["avg"])
#     cur.execute(sqlStatement_PLAYER, (playerID,
#                                       playerName, jerseyNumber, position, ba_SEASON, awayTeamID))


# conn.commit()
# cur.close()
# conn.close()
# records = cur.fetchall()

# print(records)

homeTeamPlayerStats = boxscore["home"]["players"]
for key in homeTeamPlayerStats:
    player = homeTeamPlayerStats[key]
    playerID = player["person"]["id"]
    playerName = player["person"]["fullName"]
    jerseyNumber = player["jerseyNumber"]
    position = player["position"]["abbreviation"]
    team = player["parentTeamId"]
    homeBattingStats_GAME = player["stats"]["batting"]
    homePitchingStats_GAME = player["stats"]["pitching"]
    homeBattingStats_SEASON = player["seasonStats"]["batting"]
    homePitchingStats_SEASON = player["seasonStats"]["pitching"]
    ba_SEASON = float(homeBattingStats_SEASON["avg"])
    cur.execute(sqlStatement_PLAYER, (playerID,
                                      playerName, jerseyNumber, position, ba_SEASON, homeTeamID))


conn.commit()
cur.close()
conn.close()


awayTeamBattingLineUp = boxscore["away"]["batters"]
awayTeamBattingOrder = boxscore["away"]["battingOrder"]
awayTeamPitchers = boxscore["away"]["pitchers"]


homeTeamBattingLineUp = boxscore["home"]["batters"]
homeTeamBattingOrder = boxscore["home"]["battingOrder"]
homeTeamPitchers = boxscore["home"]["pitchers"]


# print("home: %i,  away: %i" % (homeTeamID, awayTeamID))


# SCORING PLAYS
# scoring = statsapi.game_scoring_play_data(lastGame)
# print(json.dumps(scoring))


# LOOKUP TEAM
# for team in statsapi.lookup_team(''):
#     print(json.dumps(team))

# https://github.com/toddrob99/MLB-StatsAPI/wiki/Function:-roster
# statsapi.roster - generate a formatted list of players on a team's roster

# EXAMPLE: statsapi.roster(teamId, rosterType=None, season=datetime.now().year, date=None)

# Prints the Phillies roster
# print(statsapi.roster(143))
