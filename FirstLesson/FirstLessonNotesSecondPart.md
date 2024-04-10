# Lesson Notes


## first lesson 3.4 second part

## Author's Note

This document was written by Yaniv Gabay. While every effort has been made to ensure the accuracy and completeness of this material, it is possible that it may contain errors or omissions. Readers are advised to use this material as a general guide and to verify information with appropriate professional sources.
in order to see the pictures taken from the presentation, please make sure you cloned the pictures themselves.

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
- we MUST PAY,  that the 3,6,1 are only for the COLS we SELECTED and not the orignal, that why this syntax is NOT reccomended
- Preferably we will use the name of the cols it is better

- ASC | DESC

```
SELECT *
FROM table1
ORDER BY id DESC
```

```
SELECT *
FROM table1
ORDER BY score ASC
```

- we can use order by with ASC and DESC in the arguemnts

```
SELECT DISTINCT last_n, first_n, age
FROM table1
ORDER BY last_n ASC, age DESC
```

- LIMIT limit at the end, will limit the results for 3 rows
at the of the experession

```
SELECT id, last_n, first_n,
to_date, course
FROM table1
ORDER BY id
LIMIT 3
```

- without ORDER BY, we can get 3 different results each time, cus we dont know how the table is ordered etc, and we dont know what the from will give us back with limit 3, pay attenion we order by a unique id, so we will always get the same results with the LIMIT 3 command
- LIMIT with ,

```
SELECT id, last_n, first_n,
to_date, course
FROM table1
ORDER BY id DESC
LIMIT 2,5
```

- so the above example from the second row (after we orderedby) get us 5 rows from that.
- important, limit starts from 0,
- better to use offset
- OFFSET

```
SELECT id, last_n, first_n,
to_date, course
FROM table1
ORDER BY id
LIMIT 2 OFFSET 5
```

- above example much more readable,orderby need to be UNIQUE if we want to get the same results each time and not random

- STRING CONCAT, this will return us a table, will give us a single col forn first_n and ' ' and last_n, and we also added 3 to the age in the new table we got (not the original)

```
SELECT first_n || ' ' || last_n, age+3
FROM table1
ORDER BY 1
```

- order by 1 here is by (id)

- if we want to add this new col, to the current full table

```
SELECT *, first_n || ' --> ' || course
FROM table1
ORDER BY id
```

- the above example, will return a view with * (all the cols) and the new additional new course

-COLUMN NAMES

```
SELECT first_n AS name,
    'student' AS type,
    (cost * score) AS some_calc
FROM table1
ORDER BY 1
```

- basicly, take the string student, and put it on a new col called type (page47)

- we dont have to use AS
- we select, the first col and give it a new name
- than we get a value, into a new col called points
- and than we take each cost, double by 2, and put in a col called double cost

```
SELECT first_n name,
    17 points,
    (cost * 2) "double cost"
FROM table1
ORDER BY 1
```

- Table Name

```
SELECT table1.first_n   name,
table1.cost + 6  new_cost
FROM table1
ORDER BY 1
```

- we tell him specificly from taht table, take that specific col.
- and we change the names of the new cols to name and new_cost.

- in this example, we first call table1 students, so we can call it much more readble.

```
SELECT students.first_n   name,
students.cost + 6  new_cost
FROM table1 AS students
ORDER BY 1
```

- this acts just the same

```
SELECT students.first_n   name,
students.cost + 6  new_cost
FROM table1 students
ORDER BY 1
```

- we can use comments:

```
SELECT 1 c1, -- comment 1
        2 c2, -- comment 2
        3 c3  /* and also this
        is supported.. */

```

- above example, will create a table with c1,c2,c3 cols, with 1,2,3 with values to each responding col (page 53)

- Types

```
SELECT NULL,    -- type: NULL
        17,      -- type: INTEGER - signed integer
        -56,     -- type: INTEGER - signed integer
        23.48,   -- type: REAL - floating point value
        'Hi',    -- type: TEXT - text string
        x'0500'  -- type: BLOB

```

- will create col names and values as following above

- BOOL

```
SELECT 'a' = 'a'       c1,
'b' = 'c'       c2,
's' != 't'      c3,
'r' = NULL      c4,
'u' != NULL     c5,
NULL = NULL     c6,
'a' IS 'a'      c7,
'b' IS 'c'      c8,
's' IS NOT 't'  c9,
'r' IS NULL     c10,
'u' IS NOT NULL c11,
NULL IS NULL    c12
SQL: Bool / Null - Example #46 - A:
SELECT 'a' = 'a'       c1,
'b' = 'c'       c2,
's' != 't'      c3,
'r' = NULL      c4,
'u' != NULL     c5,
NULL = NULL     c6,
'a' IS 'a'      c7,
'b' IS 'c'      c8,
's' IS NOT 't'  c9,
'r' IS NULL     c10,
'u' IS NOT NULL c11,
NULL IS NULL    c12
c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12
1 0 1 None None None 1 0 1 0 1 1
```

- results:

```
c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12
1 0 1 None None None 1 0 1 0 1 1
```

- so with = and null, it always return null.
- if we want it to return true false etc, we should use IS

```
SELECT 1 = 1      c1,
    1 = 7      c2,
    1 != 7     c3,
    1 <> 7     c4,
    NOT 1 = 7  c5
```

- Casting in SQL

```
SELECT CAST('1' AS INTEGER)    c1,
CAST('12ab' AS INTEGER) c2,
CAST('cd34' AS INTEGER) c3,
CAST('ef' AS INTEGER)   c4,
CAST(1.12 AS INTEGER)   c4,
CAST(1.99 AS INTEGER)   c6,
ROUND(1.12)             r1,
ROUND(1.99)             r2,
CAST('1' AS REAL)       f1,
CAST('-1.23' AS REAL)   f2,
CAST(2 AS REAL)         f3,
CAST(11 AS TEXT)        t1,
CAST(12.2 AS TEXT)      t2
```

- results:
- pay attenion, when we convert to int, he stopped at the first char so  12ab turn into 12.
- casting int ef into 0 (no numbers)
- casting int cd34 into 0 (found a char so finished)

```
c1 c2 c3 c4 c4 c6 r1 r2 f1 f2 f3 t1 t2
1 12 0 0 1 1 1.0 2.0 1.0 -1.23 2.0 11 12.2
```

- round still make it float.
- '1' as REAL will be 1.0

-math operatos

```
SELECT 1+2,
        2.0+3.0,
        5-3,
        3-5

```

- results:

```

1+2 2.0+3.0 5-3 3-5
3 5.0 2 -2
```

- math operations are like real life, multiply before adding etc.

- BUILD IN FUNCTIONS
- abs
- dividing by 0 gives a null
- random
- round (1.22233,3) will give us 3 numbers after.
- coalesce (4/0 NULL,'ZZ','YY) will return the first value which isnt NULL

- example with coalesce

```
SELECT name,
coalesce(age, 2022 - birth, 'NA') as fixed_age
FROM children
```

- this will put 'NA' if we have NULL in some values, will return age, if its null than 2022-birth, if that null so NA

- instr replace and substr just things to do to strings

```
SELECT instr('abcdefghij', 'ef')        instr_1,
instr('abcdefghij', 'm')         instr_2,
replace('abcdefghij','de','ZZ')  replace_,
substr('abcdefghij', 5)          substr_1,
substr('abcdefghij', 5,3)        substr_2,
substr('abcdefghij', 5,-3)       substr_3,
substr('abcdefghij',-5,3)        substr_4,
substr('abcdefghij',-5,-3)       substr_5
```

- trim (page 68)
- can do rtrim only to r
- we can also use trim ('  qrsWZqrs','qrs)
- will only delete the right qrs, cus there are spaces at the start

- mixed example:

```
SELECT id*2                        double_id,
replace(last_n, 'e', 'Z-')  last_n_replaced,
upper(course)               course,
length(course)              letters_in_course,
cost + score                some_thing
FROM table1
ORDER BY 1
```

- will create a col called double_id after we doubled each id
- replace each row in that col last_n, will replace e with Z-
- upper will make a col with upper case letter etc
- etc.
- and the end we order by the first COL which is double id

- CASE WHEN

```
SELECT DISTINCT course,
CASE course
    WHEN 'math' THEN 'Hard'
    WHEN 'history' THEN 'Easy'
    ELSE 'NA'
    END level
FROM table1
```

- the name of the new col will be level (after END)
- page 73
```
SELECT id, last_n, first_n,
course, score,
CASE
    WHEN score > 95 THEN 'High'
    WHEN score > 80 AND score <= 95 THEN 'Medium'
    WHEN score > 70 AND score <= 80 THEN 'Low'
    ELSE 'Very Low'
END rate
FROM table1
```
