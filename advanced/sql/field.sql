-- Might not even need
CREATE TABLE field (
    id serial PRIMARY KEY,
    name text NOT NULL,
    parkfactor decimal,
    has_roof boolean,
    latitude decimal,
    longitude decimal
);