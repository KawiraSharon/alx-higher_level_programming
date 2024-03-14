-- lists cities in California in dtb
-- list rows for column in dtb
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
