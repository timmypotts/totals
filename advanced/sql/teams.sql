CREATE TABLE team (
    id serial PRIMARY KEY,
    name text NOT NULL,
    state text NOT NULL,
    city text NOT NULL,
    field integer,
    FOREIGN KEY (field) REFERENCES field(id) ON UPDATE CASCADE
);
