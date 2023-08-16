-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE name NOT IN (SELECT name
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
JOIN tv_shows AS s
ON s.id = sg.show_id
WHERE title = 'Dexter')
ORDER BY tv_genres.name ASC;
