--  script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT s.title, SUM(r.rate) AS rating
FROM tv_shows AS s
JOIN tv_show_ratings AS r
ON r.show_id = s.id
GROUP BY s.title
ORDER BY SUM(r.rate) DESC;
