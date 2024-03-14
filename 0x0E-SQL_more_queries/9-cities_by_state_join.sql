-- list cities in the dtb hbtn_0d_usa
-- list rows for particular column in dtb
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
