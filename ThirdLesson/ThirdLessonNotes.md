# Lesson Notes

## second lesson 10.4

## Author's Note

This document was written by Yaniv Gabay. While every effort has been made to ensure the accuracy and completeness of this material, it is possible that it may contain errors or omissions. Readers are advised to use this material as a general guide and to verify information with appropriate professional sources.
in order to see the pictures taken from the presentation, please make sure you cloned the pictures themselves.

## summary of last lesson
we went over the join statment
which is very important in SQL
so we have a col that connect between two tables
we will always need a common ground between the tables 
which is the col that we will join on

example of cartisian product using basic join:
![alt text](image-2.png)    
the results
basicly we will get n*m rows in the new table


so if we want only to see the equals,so only when the ids are equal
we will do:
```sql
SELECT *
FROM employees e, works w
WHERE e.id = w.emp_id;
```
![alt text](image-3.png)    
results:
![alt text](image-4.png)





### we stopped the last lesson at more join examples
join with on example:
![alt text](image-5.png)
important to name the tables, so e and p are the tables
the results:
![alt text](image-6.png)
important to notice, we got the same col, id= emp_id
for better, we should use specific select, and not just SELECT *


latest example was:
![alt text](image.png)
which is page 102 in LearnSQL.pdf
the results
![alt text](image-1.png)

teacher lesson example:
same example, with duplicate cols
```sql
SELECT *
FROM CountryLanguange cl
JOIN country co
ON cl.CountryCode = co.Code

```
so we can do:
```sql
SELECT cl.* , co.Name country_name
FROM CountryLanguange cl
JOIN country co
ON cl.CountryCode = co.Code

```
and this will give us all the cols from the cl table, and the country name from the co table


### self join
we can basicly do join on the same table
so we can do:
```sql
SELECT *
FROM employees e1
JOIN employees emp_mngr
ON e.mgr_id = emp_mngr.id
```
so the results of this, will give us the info, which is the manager of each employee. which we can see in the results of the query
![alt text](image-7.png)
the results:
![alt text](image-8.png)
 * we dont use the other tables they are just there

this is the same example, but choosing the new cols
based on logic, and not just show everything

```sql
SELECT e.id
        e.name emp_name
        emp_mngr.name manager_name
FROM employees e
JOIN employees emp_mngr
ON e.mgr_id = emp_mngr.id
```

###  now we talked about the diff between union union all intersect expect

so union will put the other table "below" the first table
but join, will join the cols togther.

UNION ALL will put the other table below the first table, but will not remove the duplicates

UNION without all, will remove the duplicates

INTERSECT will return only the rows that are in both tables

EXCEPT will return only the rows that are in the first table and not in the second table, similar to minus we do in set theory. 

### different between join operations
![alt text](image-9.png)

important when using left join, he will put values from the left table, and if there are no values in the right table, he will put NULL

How to do FULL JOIN?
do union (not all) of two left joins:
```sql
select*
FROM a
LEFT JOIN b
UNION 
select *
from B 
LEFT JOIN a
```




### at this point, we are at the new presenation, called SQL3

### Values
this will create a new table, with some data
we can do math operations inside the col.

```sql
SELECT * 
FROM (VALUES(1,2),(3,4),(5+6,8-7))
```
![alt text](image-10.png)


### With
this will give us that table with a name
so as a "variable" we can use it later in other queries

```sql
WITH tbl1(col1,col2) AS (VALUES(1,2),(3,4),(5+6,8-7))
SELECT *
FROM tbl1
```

![alt text](image-11.png)   

### another example
this is helpfull, to work on created tables, before we want to work on the actual database etc

```sql
WITH tbl1(col1,col2) AS (VALUES(1,2),(3,4),(5+6,8-7)),
tbl2(col1,col2) AS (SELECT col1*2, col2*2 FROM tbl1)
SELECT *
FROM tbl2
```
Results:
![alt text](image-12.png)

### another example of CTE
### common table expression
```sql
WITH only_david AS (SELECT *
                     FROM employees
                      WHERE name = 'David')
SELECT COUNT(*),
      SUM(cost)
FROM only_david
```
results:
![alt text](image-13.png)   

### group by
this is very important, we can use this to make action on some rows
```sql
SELECT course,
        COUNT(*),
        AVG(score)
FROM table1
GROUP BY course
ORDER BY 1
```
basicly, this will create groups based on the courses.
so for all the history rows, do the SELECT OPERATIONS, it is similar to distnict.

Results:
![alt text](image-14.png)

Group by is SUPER helpfull!!!

in the select with groupby, there can only be, the name of the group by argument, and argg functions

another example:
```sql
SELECT course, 
        MAX(cost) max_cost,
        MIN(age) min_age,
        ROUND(AVG(score),2) avg_score,
        GROUP_CONCAT(DISTINCT first_n||' '||
        SUBSTR(last_n,1,1)||'.') all_names
FROM table1
GROUP BY course
ORDER BY 1
```
important, order by 1 is to order it by the same col
maybe its better to write the col name itself
so ORDER BY course 
ORDER BY will order by the SELECT cols, not by the origina cols!!


![alt text](image-15.png)
much more simillar to real life queries we will run

### another example of GROUPBY
we can group by even 2 groups.
```sql
SELECT first_n,last_n,
        AVG(score),
        SUM(cost)
FROM table1
GROUP BY first_n,last_n
ORDER BY 1,2
```
the results:
![alt text](image-16.png)
 
 will create a distnict group based on the first and last name
 very important and useful.

 ### next example
 ![alt text](image-17.png)
results:
![alt text](image-18.png)

same as DISTINCT. 

### Having
this is like where, but for the group by
where will help us filter rows.
having will help us filter groups
so if course, give us 4 groups of courses,
having will help us filter those groups, that their count is atleast 1! and we must use AGG functions in the having, cause it is a term on GROUPS and not on ROWS
```sql
SELECT course,
        COUNT(*)
        AVG(score)
FROM table1
GROUP BY course
HAVING COUNT(*) > 1
```
![alt text](image-19.png)

### another example
we can also use where, but only after the results of the first querry,
cus where will act even before the group by, so its WRONG to use where before the group by
```sql
WITH  count_course AS (
        SELECT course, COUNT(*) cc, AVG(score)
        FROM table1
        GROUP BY course
)
SELECT *
FROM count_course
WHERE cc > 1

```
it is the same as the having, but we can use where, after the group by, and not before.
less usefull,more code,less effiecnt,better to use HAVING

### FILTER

```sql
SELECT 'age gt 22' kind, 
    COUNT(*)    val
FROM table1
WHERE age > 22
UNION ALL
SELECT 'score lt 80' kind, 
    COUNT(*)      val
FROM table1
WHERE score < 80
```
this is a query, of how many people are age > 22 and score < 80
the results is:
![alt text](image-20.png)

we can do the same with join
```sql
SELECT * 
FROM  ( SELECT COUNT(*) high_age 
        FROM table1
        WHERE age > 22 ),
        ( SELECT COUNT(*) low_score
        FROM table1
        WHERE score < 80 )
```
this is an invisible join,with the ,
results:
![alt text](image-21.png)   

with the join method:
```sql
SELECT * 
FROM  ( SELECT COUNT(*) high_age 
        FROM table1
        WHERE age > 22 )
JOIN  ( SELECT COUNT(*) low_score
        FROM table1
        WHERE score < 80 )
ON True -- or you can write 1 | 1=1 | etc..
```

results:
![alt text](image-22.png)   

the filter itself example:

```sql
SELECT COUNT(*) FILTER (WHERE age > 22) high_age,
        COUNT(*) FILTER (WHERE score < 80) low_score
FROM table1
```
results:
![alt text](image-23.png)   

another example:
now we will do the same as the last example, but with group by
```sql
SELECT course,
        COUNT(*) FILTER (WHERE age > 22) high_age,
        COUNT(*) FILTER (WHERE score < 80) low_score
FROM table1
GROUP BY course
```
results:
![alt text](image-24.png)

### another example
this is an example, of using the CASE WHEN instead of filter
if there is a version of SQL without filter.
so here, we will change the values, and than count
than we Bypass the filter method.
```sql
SELECT course,
        COUNT(CASE WHEN age > 22 THEN 1 ELSE NULL END) high_age,
        COUNT(CASE WHEN score < 80 THEN 1 END) low_score
FROM table1
GROUP BY course
```
results:
![alt text](image-25.png)

### another example
this will show us the percentage of the history course from the total score
```sql
SELECT 
    1.0 * SUM(score) / (SELECT SUM(score) FROM table1)
FROM table1
WHERE course = 'history'
```
Results:
![alt text](image-26.png)

but we can use the FILTER method, to do the same
```sql
SELECT 
    1.0 * SUM(score) FILTER (WHERE course = 'history') / 
    SUM(score)
FROM table1
```

take the sum of score, where the course is history, and divide it by the sum of all the scores

results:
![alt text](image-27.png)






