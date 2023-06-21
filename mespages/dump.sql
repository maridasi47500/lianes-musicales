CREATE TABLE IF NOT EXISTS concerts
(
    id integer primary key,
    lieu varchar(200),
    image varchar(200),
    title varchar(200),
    date date
);
CREATE TABLE IF NOT EXISTS recordings
(
    id integer primary key,
    concert_id integer,
    filename varchar(200),
    date date
);
insert or ignore into concerts (lieu,title,date,image)values("l'encre","concert à l'encre","03/15/2023","encre.jpeg");
insert or ignore into concerts (lieu,title,date,image)values("marché","concert fête de la musique","06/21/2023","marcheslm.jpeg");
