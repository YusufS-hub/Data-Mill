-- Create table to store lists all anime names, genre, episodes, rating, member
CREATE TABLE IF NOT EXISTS Anime_Name (
    anime_id INT GENERATED ALWAYS AS IDENTITY,
    anime_name VARCHAR(255) NOT NULL,
    genre_name VARCHAR(255),
    episodes_number INTEGER,
    rating FLOAT,
    members INTEGER,
    PRIMARY KEY(anime_id)
);

