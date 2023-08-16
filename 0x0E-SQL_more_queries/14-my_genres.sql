-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name
FROM tv_genres AS genres
JOIN tv_show_genres AS sg ON genres.id = sg.genre_id
JOIN tv_shows AS s ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY genres.name ASC;
