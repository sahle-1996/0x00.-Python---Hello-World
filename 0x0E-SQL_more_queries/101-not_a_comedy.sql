-- Script to list all shows not linked to the genre Comedy from the hbtn_0d_tvshows database
SELECT ts.title
FROM tv_shows ts
LEFT JOIN (
    SELECT tsg.show_id
    FROM tv_show_genres tsg
    INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
    WHERE tg.name = 'Comedy'
) linked_shows ON ts.id = linked_shows.show_id
WHERE linked_shows.show_id IS NULL
ORDER BY ts.title ASC;
