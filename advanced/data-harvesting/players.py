import statsapi

league_leader_types = [
    # OFFENSE
    'battingAverage',
    'shutouts',
    'sluggingPercentage',
    'onBasePlusSlugging',
    'runs',
    'homeRuns',
    'numberOfPitches',
    'onBasePercentage',
    'totalBases',
    'doubles',
    'hits',
    'atBats',
    'triples',
    'extraBaseHits',
    'runsBattedIn',
    'earnedRun',
    'totalPlateAppearances',
    # DEFENSE
    'earnedRunAverage',
    'fieldingPercentage',
    'walksAndHitsPerInningPitched',
    'errors',
    'strikeouts',
    'inningsPitched',
    'pitchesPerInning',
    'hitsPer9Inn',
    # OVERALL
    'gamesStarted',
    'wins'
    'losses',
    'winPercentage'

    # EXTRANEOUS
    'sacrificeBunts',
    'sacrificeFlies',
    'groundoutToFlyoutRatio',
    'stolenBases',
    'assists',
    'groundOuts',

    'caughtStealing',
    'groundIntoDoublePlays',
    'flyouts',
    'hitByPitches',
    'gamesPlayed',
    'walks',
    'intentionalWalks',
    'saves',   'wildPitch',   'airOuts',   'balk',
    'blownSaves',   'catcherEarnedRunAverage',   'catchersInterference',   'chances',   'completeGames',
    'doublePlays',         'gamesFinished',
    'hitBatsman',      'holds',   'innings',
    'outfieldAssists',   'passedBalls',   'pickoffs',     'putOuts',
    'rangeFactorPerGame',   'rangeFactorPer9Inn',   'saveOpportunities',   'stolenBasePercentage',   'strikeoutsPer9Inn',
    'strikeoutWalkRatio',   'throwingErrors',   'totalBattersFaced',   'triplePlays',   'walksPer9Inn'
]

# generate a formatted list of stat leaders for current or specified season
# rookie_hr_leaders = statsapi.league_leaders('homeRuns', season=2022, playerPool = 'rookies', limit=5)
# rookie_hr_leaders = rookie_hr_leaders.split('\n')
# print(rookie_hr_leaders)


# TEAM LEADER FOR STAT

# EX:
# Print the top 5 team leaders in runs for the 2022 Giants
# print(statsapi.team_leaders(137,'runs',limit=5,season=2022))

# top 5 players for runs
# r_leaders = statsapi.team_leaders(
#     115, 'earnedRunAverage', limit=5, season=2021)
# print(r_leaders)


# PLAYER STAT DATA
playerStats = statsapi.player_stat_data(
    personId, group="[hitting,pitching,fielding]", type="season")
