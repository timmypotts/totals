CREATE TABLE team (
    id serial PRIMARY KEY,
    name text NOT NULL,
    state text NOT NULL,
    city text NOT NULL,
    home_field integer,
    FOREIGN KEY (field_id) REFERENCES field(id) ON UPDATE CASCADE,
)
