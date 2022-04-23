import statsapi



endpoints = {
    "attendance" : "https://statsapi.mlb.com/api/v1/attendance",
    "conferences" : "https://statsapi.mlb.com/api/v1/conferences",
    "divisions" : "https://statsapi.mlb.com/api/v1/divisions",
    "game": "https://statsapi.mlb.com/api/v1/game/{gamePk}/feed/live",
    # "leagueLeaderTypes": ""

}

# GET
# statsapi.get(endpoint, params, force=False)


# META
llTypes = statsapi.meta('leagueLeaderTypes')

print(llTypes)
