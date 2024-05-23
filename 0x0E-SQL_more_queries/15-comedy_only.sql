-- Script to list all shows contained in hbtn_0d_tvshows without a genre linked
SELECT ts.title
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name IS NULL OR tg.name != 'Comedy'
ORDER BY ts.title ASC;
