-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE MONTH=7 OR MONTH=8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
