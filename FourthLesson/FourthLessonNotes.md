# Lesson Notes

## fourth lesson 1.5.24

## Author's Note

This document was written by Yaniv Gabay. While every effort has been made to ensure the accuracy and completeness of this material, it is possible that it may contain errors or omissions. Readers are advised to use this material as a general guide and to verify information with appropriate professional sources.
in order to see the pictures taken from the presentation, please make sure you cloned the pictures themselves.

## summary of last lesson

### name and id of 2 highest score
```sql
SELECT id,last_n,first_n, score
FROM table1
ORDER BY score DESC
LIMIT 2
```
![alt text](image.png)  
this is a bad example, why it doesnt work.
cus the avgscore isnt relevant to cohen david, but still that row is with the avg score

another "bad" example:
![alt text](image-1.png)    
we could have fixed this by using group by

the appropriate way to do it is:
![alt text](image-2.png)    
```sql
SELECT id,last_n,first_n
FROM table1
WHERE score = (SELECT MAX(score) FROM table1)
```

there is a better way, without doing the two querries..

to get the two biggest:
![alt text](image-3.png)    
```sql
SELECT id,last_n,first_n,score
FROM table1
ORDER BY score DESC
LIMIT 2
```


we will start from the previous slide, and we will add the new slide when we will finish the previous one.

### COUNT DUPLICATE LINES 1
what is a duplicate line.
this query will just give us how many duplicate lines there are, without knowing which row is row etc. just how many duplicates thre are
```sql
SELECT 
(SELECT count(*) FROM table1) -
(SELECT count(*) FROM (SELECT DISTINCT last_n, first_n 
FROM table1)) count_dup
```
![alt text](image-4.png)

if we want to know which rows:

![alt text](image-5.png)
```sql
SELECT last_n, first_n
FROM table1
GROUP BY last_n, first_n
HAVING COUNT(*) > 1
```
this will show us, only the groups, that have duplciates, but NOT how many rows are duplicates.
![alt text](image-6.png)

important , we cant have select COLX that isnt in groupby opeartion

if we want how many from each group:
```sql
SELECT last_n, first_n, COUNT(*)
FROM table1
GROUP BY last_n, first_n
HAVING COUNT(*) > 1
```
IMPORTANT
SELECT cannot affect on the amount of rows, it can only affect on the amount of columns

if we want to count, this results, (3) we can do:

```sql
SELECT COUNT(*) FROM
(
SELECT last_n, first_n
FROM table1
GROUP BY last_n, first_n
HAVING COUNT(*) > 1
) 
```


```sql
WITH  dup_names AS (
SELECT last_n, first_n
FROM table1
GROUP BY last_n, first_n
HAVING COUNT(*) > 1
)
SELECT COUNT(*) 
FROM dup_names
```

if we wanted for each group, how many duplicates there are, we could do:
```sql

SELECT SUM(ss) FROM
(
SELECT last_n, first_n, COUNT(*)-1 as ss
FROM table1
GROUP BY last_n, first_n
HAVING COUNT(*) > 1
) 
```
here , we get the sum, of ss, which is the col, of how many duplicates each group have
the -1 is because we dont want to count the original row, only the duplicates


![alt text](image-7.png)    
this is the results

### Remove duplicates
![alt text](image-8.png)
```sql
SELECT DISTINCT *
FROM table1
```

also
![alt text](image-9.png)
the intersect

![alt text](image-10.png)
union aswell

this is okay, but we dont see the val
![alt text](image-11.png)

best solution, is to use group by and max
![alt text](image-12.png)   
```sql
SELECT item,id,MAX(val) val
FROM table1
GROUP BY item,id
```
this will remove the duplicates, and also give us a selection, if we want the max dup,etc.

### Simulate FULL OUTER JOIN

```sql
SELECT e.*, w.* 
FROM employees e
LEFT JOIN works w
ON e.id = w.emp_id
UNION
SELECT e.*, w.* 
FROM works w
LEFT JOIN employees e
ON e.id = w.emp_id 
ORDER BY id
```
results:
![alt text](image-13.png)   

### LEFT JOIN - ON VS WHERE
```sql
SELECT e.*, w.* 
FROM employees e
LEFT JOIN works w
ON e.id = w.emp_id
AND proj_id > 10
```
the LEFT join, will bring all the rows of the left table, but if we have rows that wont match the condition, they will be null in the values missing, ON is part of the JOIN

another example, but WHERE runs after the join

```sql
SELECT e.*, w.* 
FROM employees e
LEFT JOIN works w
ON e.id = w.emp_id
WHERE proj_id > 10
```
results:
![alt text](image-14.png)
so we can see, the where, will remove nulls, and remove the rows that proj_id is > 10.

at this point, we are moving to the next slide (3)
### Windows functions

#### OVER
```sql
SELECT *, SUM(amount) OVER()
FROM sales s1
ORDER BY day,hour
```
without the OVER, this querry is ILEGAL (missing group by), but using 
![alt text](image-15.png)   
results:
![alt text](image-16.png)
so the results, is the sum, of the col we asked, and it will be added on each row.
its effective, we calc it once the sum, and we add it to each row

another example:
```sql
SELECT *,SUM(amount) OVER() as all_sum, 
        100.0 * amount / SUM(amount) OVER() as percent
FROM sales s1
ORDER BY day,hour
```
now, we can calculate the percent of each row, in comparison to the total sum
![alt text](image-17.png)

results:
![alt text](image-18.png)
if we wanted to do the same without the over function we could have done:
```sql
SELECT *, 
        100.0 * amount / (SELECT SUM(amount) FROM sales) as percent
FROM sales s1
ORDER BY day,hour
```


another example:
```sql
SELECT *,
COUNT(amount) OVER () as count,
MIN(amount) OVER () as min,
AVG(amount) OVER () as avg,
MAX(amount) OVER () as max
FROM sales s1 
ORDER BY day, hour
```


![alt text](image-19.png)
results:
![alt text](image-20.png)


another example:
```sql
SELECT *,
GROUP_CONCAT(day) OVER () as gc_day,
GROUP_CONCAT(amount) OVER () as gc_amount
FROM sales s1 
ORDER BY day, hour
```
![alt text](image-21.png)

results:
![alt text](image-22.png)
group concat is also working.
but the general group by, doesnt work on the window functions, and also the window function does the concat, in any way he will do it. 



### PARTITION BY
```sql
SELECT *,
COUNT(amount) OVER (PARTITION BY day) as count_d,
MIN(amount) OVER (PARTITION BY day) as min_d,
AVG(amount) OVER (PARTITION BY day) as avg_d,
MAX(amount) OVER (PARTITION BY day) as max_d
FROM sales s1 
ORDER BY day, hou
```
![alt text](image-23.png)
results:
![alt text](image-23.png)
