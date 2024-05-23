-- Command to list all records of the table second_table from the database hbtn_0c_0 where the name is not empty
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC;
