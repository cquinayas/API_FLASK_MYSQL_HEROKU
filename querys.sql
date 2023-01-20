use sql10591684;

-- 1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
select title, count(*)
from netflix
where title like "%love%";

-- 2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
select id, count(*) as cant
from netflix 
where release_year=2010 and score>85; 

select id, release_year, score, count(*) as cant
from amazon
where release_year=2010 and score>35; 

-- 3. La segunda película con mayor score para una plataforma determinada, según el orden 
-- alfabético de los títulos
select title
from amazon
where score = 100
order by title asc limit 2;


-- 4. Película que más duro segun año, plataforma y tipo de duración
select title, duration_int
from netflix
where release_year = 2016 and duration_type = "min"
order by duration_int desc limit 1;


-- 5. Cantidad de series y peliculas por rating
select rating, count(*)
from amazon
where rating = '18+';