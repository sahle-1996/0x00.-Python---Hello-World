-- Prints the sorted database, filtering records with a score greater than or equal to 10
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY 1 DESC, 2;
