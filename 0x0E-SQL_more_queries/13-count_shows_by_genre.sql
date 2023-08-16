-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows FROM tv_genres AS g JOIN tv_show_genres AS sg ON g.id = sg.genre_id WHERE sg.show_id IS NOT NULL GROUP BY g.name ORDER BY COUNT(sg.show_id) DESC;
