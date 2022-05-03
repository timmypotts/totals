CREATE TABLE batting_stats (
    player_id integer,
    at_bats integer,
    runs integer,
    hits integer,
    home_runs integer,
    rbis integer,
    strikeouts integer,
    left_on_base integer,
    singles integer,
    doubles integer,
    triples integer, 
    avg decimal,
    obs decimal,
    obp decimal,
    slg decimal,
    at_bats_per_home_run decimal,
    game_id integer,
)

CREATE TABLE pitching_stats (
    era decimal,
    innings_pitched decimal,
    hits integer,
    runs integer,
    earned_runs integer,
    walks integer,
    strikeouts integer,
    home_runs integer,
    singles integer,
    doubles integer,
    triples integer, 
    player_id integer,
    game_id integer,
)

