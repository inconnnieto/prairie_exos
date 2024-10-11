CREATE TABLE people (
    name VARCHAR NOT NULL,
    dob DATE,
    height FLOAT
);

CREATE TABLE city (
    name VARCHAR NOT NULL,
    lat FLOAT,
    lon FLOAT
);

INSERT INTO city(name, lat, lon)
VALUES ('Seoul', 37.5, 126.9);

INSERT INTO people(name, dob, height)
VALUES ('Kim Namjoon', '1994-09-12', 1.81);

ALTER TABLE people ADD COLUMN city_id INT;
--
ALTER TABLE city ADD COLUMN city_id SERIAL PRIMARY KEY;

UPDATE people SET city_id = (
    SELECT city_id FROM city
    WHERE name = 'Seoul')
    WHERE name = 'Kim Namjoon';

--ALTER TABLE people ADD CONSTRAINT fk_city FOREIGN KEY (city_id) REFERENCES city(city_id);

RETURNING *;