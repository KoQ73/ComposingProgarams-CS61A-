.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color FROM students AS first, students AS second
  WHERE first.time < second.time AND first.pet = second.pet AND first.song = second.song;


CREATE TABLE sevens AS
  SELECT s.seven FROM students AS s, numbers AS c WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) as lowest FROM inventory GROUP BY item;

CREATE TABLE best_deal AS
  SELECT name, min(MSRP / rating) FROM products GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT name, store FROM best_deal, lowest_prices WHERE name = item;

CREATE TABLE bandwidth_per_store AS
  SELECT s.store, sum(Mbs) as Mbs FROM stores as s, shopping_list as l GROUP BY s.store, l.store HAVING s.store = l.store;

CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) FROM bandwidth_per_store;

