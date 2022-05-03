CREATE TABLE players (
    id serial PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    title text,
    bats text NOT NULL,
    throws text NOT NULL,
    position text NOT NULL,
    injured boolean NOT NULL DEFAULT false,
    ba decimal NOT NULL   
)