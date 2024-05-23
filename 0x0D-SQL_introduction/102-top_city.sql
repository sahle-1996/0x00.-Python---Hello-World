-- Command to display the top 3 cities with the highest average temperature during July and August, ordered by temperature (descending)
SELECT city,
       AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY 2 DESC
LIMIT 3;
