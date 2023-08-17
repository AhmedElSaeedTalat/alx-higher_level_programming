--  script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
JOIN tv_shows AS s
ON s.id = sg.show_id;
