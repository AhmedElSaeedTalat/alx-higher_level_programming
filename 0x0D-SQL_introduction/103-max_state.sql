-- script that displays the max temperature of each state (ordered by State name).
SELECT STATE, MAX(value) FROM temperatures GROUP BY state ORDER BY state;
