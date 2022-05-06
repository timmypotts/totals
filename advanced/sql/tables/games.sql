CREATE TABLE game (
    id serial PRIMARY KEY,
    date timestamp,
    home_team integer,
    away_team integer,
    home_team_runs integer,
    away_team_runs integer,
    home_team_starting_pitcher integer,
    away_team_starting_pitcher integer,
    away_avg decimal,
    away_obp decimal,
    away_slg decimal,
    away_ops decimal,
    away_pitching_obp decimal,
    away_era decimal,
    home_avg decimal,
    home_obp decimal,
    home_slg decimal,
    home_ops decimal,
    home_pitching_obp decimal,
    home_era decimal,
    FOREIGN KEY (home_team_starting_pitcher) REFERENCES players(id) ON UPDATE CASCADE,
    FOREIGN KEY (away_team_starting_pitcher) REFERENCES players(id) ON UPDATE CASCADE
);


CREATE TABLE player_game_stats (
    game_id integer,
    player_id integer,
    runs integer,
    doubles integer,
    triples integer,
    home_runs integer,
    ks integer,
    walks integer,
    hits integer,
    at_bats integer,
    stolen_bases integer,
    rbi integer,
    left_on_base integer,
    FOREIGN KEY (game_id) REFERENCES game(id) ON UPDATE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(id) ON UPDATE CASCADE
);