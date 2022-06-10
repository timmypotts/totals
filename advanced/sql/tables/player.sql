CREATE TABLE player (
    id serial PRIMARY KEY,
    full_name text NOT NULL,
    number integer NOT NULL,
    position text NOT NULL,
    bats text,
    throws text,
    injured boolean NOT NULL DEFAULT false,
    ba decimal NOT NULL,
    team integer NOT NULL,
    FOREIGN KEY (team) REFERENCES team(id) ON UPDATE CASCADE
);
