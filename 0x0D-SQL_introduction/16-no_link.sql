-- show rows for its value

SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
