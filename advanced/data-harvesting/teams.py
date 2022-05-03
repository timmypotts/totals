import statsapi
import json
import sqlalchemy

db = sqlalchemy.create_engine('postgresql://postgres:a0E24me@localhost:5432/mlb')


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

# Returns home team stats and player stats
print(json.dumps(boxscore["home"]))


awayTeamID = boxscore["away"]["team"]["id"]
awayTeamBattingStats = boxscore["away"]["teamStats"]["batting"]
awayTeamBattingStats["avg"] = float(awayTeamBattingStats["avg"])
awayTeamBattingStats["obp"] = float(awayTeamBattingStats["obp"])
awayTeamBattingStats["slg"] = float(awayTeamBattingStats["slg"])
awayTeamBattingStats["ops"] = float(awayTeamBattingStats["ops"])

awayTeamPitchingStats = boxscore["away"]["teamStats"]["pitching"]
awayTeamPitchingStats["obp"] = float(awayTeamPitchingStats["obp"])
awayTeamPitchingStats["era"] = float(awayTeamPitchingStats["era"])
awayTeamPitchingStats["inningsPitched"] = float(awayTeamPitchingStats["inningsPitched"])


homeTeamID = boxscore["home"]["team"]["id"]

homeTeamBattingStats = boxscore["away"]["teamStats"]["batting"]
homeTeamBattingStats["avg"] = float(homeTeamBattingStats["avg"])
homeTeamBattingStats["obp"] = float(homeTeamBattingStats["obp"])
homeTeamBattingStats["slg"] = float(homeTeamBattingStats["slg"])
homeTeamBattingStats["ops"] = float(homeTeamBattingStats["ops"])

homeTeamPitchingStats = boxscore["away"]["teamStats"]["pitching"]
homeTeamPitchingStats["obp"] = float(homeTeamPitchingStats["obp"])
homeTeamPitchingStats["era"] = float(homeTeamPitchingStats["era"])
homeTeamPitchingStats["inningsPitched"] = float(homeTeamPitchingStats["inningsPitched"])


# print(json.dumps(awayTeamBattingStats))
# print(json.dumps(awayTeamPitchingStats))


# print(json.dumps(homeTeamBattingStats))
# print(json.dumps(homeTeamPitchingStats))


awayTeamPlayerStats = boxscore["away"]["players"]
for key in awayTeamPlayerStats:
    player = awayTeamPlayerStats[key]
    idAndName = player["person"]
    jerseyNumber = player["jerseyNumber"]
    position = player["position"]["abbreviation"]
    team = player["parentTeamId"]
    gameStatsBatting = player["stats"]["batting"]
    gameStatsPitching = player["stats"]["pitching"]
    seasonStatsBatting = player["seasonStats"]["batting"]
    seasonStatsPitching = player["seasonStats"]["pitching"]

homeTeamPlayerStats = boxscore["home"]["players"]
for key in awayTeamPlayerStats:
    player = awayTeamPlayerStats[key]
    idAndName = player["person"]
    jerseyNumber = player["jerseyNumber"]
    position = player["position"]["abbreviation"]
    team = player["parentTeamId"]
    gameStatsBatting = player["stats"]["batting"]
    gameStatsPitching = player["stats"]["pitching"]
    seasonStatsBatting = player["seasonStats"]["batting"]
    seasonStatsPitching = player["seasonStats"]["pitching"]
    print(idAndName["fullName"], jerseyNumber, position, team, gameStatsBatting, seasonStatsBatting)


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
