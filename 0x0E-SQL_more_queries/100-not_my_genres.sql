-- Script to list all genres not linked to the show Dexter from the hbtn_0d_tvshows database
SELECT tg.name
FROM tv_genres tg
LEFT JOIN (
    SELECT tsg.genre_id
    FROM tv_show_genres tsg
    INNER JOIN tv_shows ts ON tsg.show_id = ts.id
    WHERE ts.title = 'Dexter'
) linked_genres ON tg.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tg.name ASC;
