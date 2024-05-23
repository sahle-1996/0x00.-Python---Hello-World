-- Script to list all shows contained in hbtn_0d_tvshows without a genre linked
SELECT ts.title,
       'No Genre' AS genre_id
FROM tv_shows ts
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres tsg
    WHERE ts.id = tsg.show_id
)
ORDER BY ts.title;
