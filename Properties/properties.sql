DROP TABLE Properties;

CREATE TABLE Properties (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         year INTEGER,
         square INTEGER,
         district VARCHAR(50),
         price INTEGER);

INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'shev', 90000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'shev', 70000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'shev', 45000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'svyt', 65000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'svyt', 35000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'svyt', 75000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'dis', 80000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'dis', 40000);
INSERT INTO Properties (year, square, district, price)
VALUES (1939, 45, 'dis', 30000);

select * from properties;


select price
from properties
where year = 1939 and square = 45 and district = 'shev'
order by price
limit 1;


