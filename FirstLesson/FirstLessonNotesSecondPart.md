# Lesson Notes

## Learn Sql
- we get a table, we will not learn ho to create one
- we have, id,last_n,first_n,age,course,to_date,cost,score (cols)
- to get all the the table we do:
``` SELECT *
    FROM table1
```
-we can use WHERE to get a specific row so:
``` 
    SELECT *
    FROM table1
    WHERE id = 7
```
``` 
    SELECT *
    FROM table1
    WHERE age > 23
```
``` 
    SELECT *
    FROM table1
    WHERE course != 'math' AND score >= 80
```

```
SELECT *
FROM table1
WHERE course != 'math' OR score >= 80
```
- important to use () when using several logics

``` 
SELECT *
FROM table1
WHERE (cost >= 18 OR score < 80) AND age > 22
```
- so always put () when using AND or OR

```
SELECT *
FROM table1
WHERE cost >= AND cost <=19
```
- we can write it much better with BETWEEN
```
SELECT *
from table1
WHERE cost BETWEEN 17 AND 19
```
- IN
```
SELECT *
FROM table1
WHERE last_n = 'Levi' OR last_n = 'Peled'
```
- we can use in
```
SELECT *
FROM table1
WHERE last_n IN ('Levi','Peled')
```
- this example will return empty:
```
SELECT *
FROM table1

WHERE last_n = 'Levi' AND last_n = 'Peled'
```

- NOT
- example with between etc
```
SELECT *
FROM table1
WHERE cost NOT BETWEEN 17 AND 19
```
- NOT with IN will return all the names, which are NOT levi or peled
```
ELECT *
FROM table1
WHERE last_n NOT IN ('Levi', 'Peled')
```
- same thing as above with , but worse syntax
```
SELECT *
FROM table1
WHERE last_n != 'Levi' AND last_n != 'Peled
```
- if we use or, we will get all of them which is a mistake
```
SELECT *
FROM table1
WHERE last_n != 'Levi' OR last_n != 'Peled'
```
- LIKE command, so we can search by strings, we can use regex but we wont use it. LIKE is our alternative. % means between 0- inifnity chars, so it will bring all courses that start with the letter m.
```
SELECT *
FROM table1
WHERE course LIKE 'm%'
```
- we can use underscore for LIKE command _, will return only values that start with m and 4 letters after
```
SELECT *
FROM table 1
WHERE course LIKE 'm____' (we used 4 underscores _)
```
- start, or m in the middle, or at the end
```
SELECT *
FROM table1
WHERE course LIKE '%m%'
```

- Example with LIKE %en (all names end with en)
```
SELECT *
FROM table1
WHERE last_n LIKE '%en'
```
- lets say we want some of the cols and not all of them:
```
SELECT last_n, first_n, age
FROM table1

```
- DISTINCT
```
SELECT course
FROM table1
```
- the above will give as all courses but with duplicates if we want unique ones we can use:
```
SELECT DISTINCT course
FROM table1
```
- we will get only unique courses so we will get only rows equal to unique types
```
SELECT DISTINCT last_n, first_n
FROM table1
```
- the above example will bring back the uniques couples, we can still have duplicates in a single col (31 in the presenation)

- ORDER BY
```
SELECT *
FROM table1
ORDER BY age
```
- the above example, will return a new table already ordered

```
SELECT DISTINCT last_n, first_n, age
FROM table1
ORDER BY last_n
``` 
- the above will give us the unique ages and first and last name SELECT always first, than FROM, and than ORDER, the order is very importatnt
- so it will return a order table by last name (page 35)

```
SELECT id, last_n, first_n, course, to_date, cost
FROM table1
ORDER BY 3,6,1
```
- the above example, we order by something, something,something
- lets take a phone book, so first we order by lastname, is there are equals, we will order by firstname, and than other one
- so specifcly this will sort first by the third col (firstname)
- all the equals will be sorted by the 6th col (which is cost)
- if there are still equals sort by the first col (which is ID)
- we can use the names of the cols of the number of the cols
