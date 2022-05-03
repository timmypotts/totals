CREATE TABLE game (
    id serial PRIMARY KEY,
    date timestamp,
    home_team integer,
    away_team integer,
    home_team_runs integer,
    away_team_runs integer,
    home_team_starting_pitcher integer,
    away_team_starting_pitcher integer,
    home_team_relief_pitcher integer,
    away_team_relief_pitcher integer
)