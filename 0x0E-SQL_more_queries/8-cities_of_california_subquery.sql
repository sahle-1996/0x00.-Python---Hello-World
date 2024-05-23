-- Script to list all the cities of California that can be found in database hbtn_0d_usa
SELECT c.id,
       c.name
FROM cities c
JOIN states s ON c.state_id = s.id
WHERE s.name = 'California'
ORDER BY c.id;
