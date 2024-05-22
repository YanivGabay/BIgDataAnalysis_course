# Lesson Notes

## Seventh lesson 8.5.24

## Author's 

This document was written by Yaniv Gabay. While every effort has been made to ensure the accuracy and completeness of this material, it is possible that it may contain errors or omissions. Readers are advised to use this material as a general guide and to verify information with appropriate professional sources.
in order to see the pictures taken from the presentation, please make sure you cloned the pictures themselves.

## Previous Lesson Recap


### Document Store - Graph DB
a graph databse stores nodes and relationships instead of tables or documents.
data is stores just like you might sketch ideas on a whiteboard. your data is stores without restircting to a pre defined model, allowing a ver flexiable way of thinking about and using it.

### Graph DB - why?
![alt text](image.png)

### Graph DB - Neo4j
![alt text](image-1.png)
![alt text](image-2.png)
Nodes are also referred to as vertices or points
Relationships are also referred to as edges or lines links.
There is additional information, inside the nodes, and inside the edges.
### Naming Conventions
![alt text](image-3.png)
Node label - Camel Case :VehicleOwner
Relationship type - upper case, using underscore to separate words :OWNS_VEHICLE
Property - lower case camel case :firstName

### GraphDB Neo4j
![alt text](image-4.png)

rich eco system:
![alt text](image-5.png)    

### GraphDB Cypher query languange
Cyper is an open data query language based on the openCypher initiative.
![alt text](image-6.png)    
![alt text](image-7.png)

so gql (graph query lang) will be a new databse query languange.

### Cypher query fundamentals
![alt text](image-8.png)

### Cypher editor
![alt text](image-9.png)

### Graph DB queries tabuler results
![alt text](image-10.png)

### Graph DB example queries
will help us see the visualiztion of the data
```cypher
CALL db.schema.visualization()
```

```cyper
MATCH (p:Person) // we can also do (persons:Person)// the first variables is the name of the atble (or types we want to be called) second variable after: is the actual type of the node
RETURN *
LIMIT 9
```
```cypher
MATCH (p:Person)
RETURN p.name, p.born as born
LIMIT 9
```

```cypher
MATCH (p:Person)
RETURN p //this will allow us to display a graph, cus we display all p
LIMIT 9
```



```cypher
MATCH (p:Person)
WHERE p.name = 'Tom Hanks' OR p.name = 'Rita Wilson'
RETURN p.name, p.born
```

```cypher
MATCH (p:Person)-[r]->(m:Movie) --any connection will be named r
WHERE p.name = 'Tom Hanks'
RETURN *
LIMIT 9
```

```cypher
MATCH (p:Person)-[r:DIRECTED]->(m:Movie) 
WHERE p.name = 'Tom Hanks'
RETURN p,m,r -- will return the person, the movie and the relationship
LIMIT 9
```
```cypher
MATCH (p:Person)-[r:DIRECTED]->(m:Movie) 
WHERE p.name = 'Tom Hanks'
RETURN p,m -- so we will not see the relationship,but in the graph we will see the relationship and all of them
LIMIT 9
```

```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.name = 'Tom Hanks'
RETURN m.title
```

```cypher
MATCH QQ = ((p:Person)-[:ACTED_IN]->(m:Movie))
WHERE p.name = 'Tom Hanks'
RETURN QQ
```
```cypher
MATCH QQ = ((p:Person WHERE p.name = 'Tom Hanks')-[:ACTED_IN]->(m:Movie))
RETURN QQ
```
also another way of syntax
```cypher
MATCH p-[:ACTED_IN]->m
WHERE p:Person AND m:Movie AND p.name = 'Tom Hanks'
RETURN m.title
```

if we dont mind what connection type
this query does NOT return the connections
```cyper
MATCH (p:Person)--(m:Movie)
WHERE p.name = 'Tom Hanks'
RETURN *
```
can or operator on the node label
```cyper
MATCH (p:Person|Actor) -- (p:Person|Actor|Director)
RETURN DISTINCT labels(p)
```


```cypher
MATCH (p)-[:ACTED_IN]->(m:Movie)
WHERE p:Person AND m:Movie AND m.title = 'The Matrix'
return p.name
```
helpfull to say which nodes we DONT want to see
```cypher
MATCH (p)-[:ACTED_IN]->(m:Movie)
WHERE p:Person AND NOT m:Movie AND m.title = 'The Matrix'
return p.name
```

```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE 2000 <= m.released <= 2003
RETURN p.name, m.title, m.released
```
to compare strings:
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE "2000" <= m.released <="2003"
RETURN p.name, m.title, m.released
```
    
    
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.name = 'Jack Nicholson' AND m.tagline IS NOT NULL
RETURN p.name, m.title, m.tagline
```

### Graph DB More example queries
```cypher
MATCH (p:Person)
WHERE p.born IN [1965, 1970, 1975]
RETURN p.name, p.born
```

```cypher
MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
WHERE 'Neo' IN r.roles AND m.title = 'The Matrix'
RETURN p.name, m.title,r
```
```cypher
MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
WHERE m.title = 'The Matrix'
RETURN p,r,m
```
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE  m.title = 'The Matrix'
RETURN keys(p), labels(p), p.name, p.born
```

```cypher
MATCH (p:Person)-[r]-(m:Movie)
WHERE  m.title = 'The Matrix'
RETURN DISTINCT type(r),r
```
dont care what nodes, return all distinct relationships
```cypher
MATCH ()-[r]-()
RETURN DISTINCT type(r)
```

```cypher
Proprties:
MATCH (p:Person)
RETURN p.name,keys(p)
```

```cypher
MATCH (p:Person)
WHERE p.born.year >1960
    AND p:Actor
    AND p:Director
RETURN p.name, p.born, labels(p)
```

### Graph DB More example queries (3)
```cypher
Schema:
CALL db.propertyKeys()
CALL db.schema.visualization()
CALL db.schema.nodeTypeProperties()
CALL db.schema.relTypeProperties()
```

in the next queriy, p is a person
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p)
WHERE p.born.year > 1960
RETURN p.name,p.born,labels(p),m.title
ORDER BY p.name
```
we can break those chains
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie),
(p)-[:DIRECTED]->(m)
WHERE p.born.year > 1960
RETURN p.name,p.born,labels(p),m.title
ORDER BY p.name
```

we can break those chains using two MATCH
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
MATCH (p)-[:DIRECTED]->(m)
WHERE p.born.year > 1960
RETURN p.name,p.born,labels(p),m.title
ORDER BY p.name
```
we can use EXPLAIN will return a plan of the query\
and will not actually execute the query
```cypher
EXPLAIN MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
MATCH (p)-[:DIRECTED]->(m)
WHERE p.born.year > 1960
RETURN p.name,p.born,labels(p),m.title
ORDER BY p.name
```
we can use PROFILE to see the query plan and the time it took
will actually execute the query
```cypher
PROFILE MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
MATCH (p)-[:DIRECTED]->(m)
WHERE p.born.year > 1960
RETURN p.name,p.born,labels(p),m.title
ORDER BY p.name
```


```cypher
MATCH (p:Person)-[r]->(m:Movie)
WHERE p.name = 'Tom Hanks'
RETURN m.title AS movie, type(r) AS reationship type

```

```cypher
MATCH (m:Movie)
WHERE "Israel" IN m.countries
RETURN m.title, m.language, m.countries
```

```cypher
MATCH (p:Actor | Person)
RETURN DISTINCT labels(p)
```

```cypher
MATCH (p:Person)
WHERE p:Actor and p:Person
RETURN DISTINCT labels(p)
```

### Graph DB More example queries (4) and strings
```cypher
MATCH (m:Movie)
WHERE m.title STARTS WITH 'Toy Story'
RETURN m.title, m.released
```
    
```cypher
MATCH (m:Movie)
WHERE m.title CONTAINS 'River' //if a bigger string contains a smaller string
RETURN m.title, m.released
```
```cypher
MATCH (p:Person)-[:ACTED_IN]->()
WHERE toLower(p.name) STARTS WITH 'michael'
RETURN p.name
```
```cypher
MATCH (p:Person)
WHERE toUpper(p.name) ENDS WITH 'DEMILLE'
RETURN p.name
```

### Query Patterns
```cypher
MATCH (p:Person)-[:WROTE]->(m:Movie)
//WHERE NOT exists( (p)-[:DIRECTED]->(m) )
RETURN p.name, m.title
```
```cypher
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.name = 'Tom Hanks'
AND exists {(p)-[:DIRECTED]->(m)}
RETURN p.name, labels(p), m.title
```
```cypher
Same - much more efficient:

MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p)
WHERE p.name = 'Tom Hanks'
RETURN m.title
```
```cypher
For NOT - must do this:
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.name = 'Tom Hanks'
AND NOT exists {(p)-[:DIRECTED]->(m)}
RETURN m.title
```

### aggregation
this is the same action as group by (insql)
```cypher
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)// WHERE a.name = 'Tom Hanks'
RETURN a.name AS actorName,
count(*) AS numMovies
```
// 
Aggregation in Cypher is different from aggregation in SQL. In Cypher, you need not specify a grouping key. As soon as an aggregation function like count() is used, all non-aggregated result columns become grouping keys.The grouping is implicitly done, based upon the fields in the RETURN clause.
Create list:
```cypher
MATCH (p:Person)
RETURN p.name, [p.born, p.died] AS lifeTime
LIMIT 10
```
```cypher
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)
RETURN a.name AS actor,count(*) AS total,collect(m.title) AS movies
ORDER BY total DESC
 LIMIT 10
 ```
```cypher
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)WHERE m.year = 1920
RETURN collect(DISTINCT m.title) AS movies,collect( a.name) AS actors
```