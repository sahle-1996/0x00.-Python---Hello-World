-- Script to list all genres from hbtn_0d_tvshows and display the number of shows linked to each
SELECT tg.name AS genre,
       COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY tg.id
ORDER BY number_of_shows DESC,
         tg.id ASC;
