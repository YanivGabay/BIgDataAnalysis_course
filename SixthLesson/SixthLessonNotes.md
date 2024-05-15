# Lesson Notes

## sixth lesson 15.5

## Author's Note

This document was written by Yaniv Gabay. While every effort has been made to ensure the accuracy and completeness of this material, it is possible that it may contain errors or omissions. Readers are advised to use this material as a general guide and to verify information with appropriate professional sources.
in order to see the pictures taken from the presentation, please make sure you cloned the pictures themselves.





### NO SQL

#### Document store document oritented database

most of the times, these dont support SQL languange

abit less usefull in big data worlds, and more oriented to small data (apps webs etc)

documents stores also called document oriented databases, are characterized by their schema-less design. This means that unlike traditional relational databases, there is no need to define the structure of the data before storing it. Instead, the data is stored in a format similar to JSON, which allows for nested data structures and flexible schemas. This makes document stores ideal for applications that require a high degree of flexibility and scalability, such as content management systems, e-commerce platforms, and social media applications.

That means:
- Records do not need to have uniform structure
- The types of values can be different for each record
- Columns can have more than one value (arrays etc)
- Records can have nested structures (objects etc)
- Documents stores often se internal notation like JSON, BSON, XML etc

#### Documents
- also have CRUD operations create, read, update, delete (create, retrieval(query find read), update,deletion)
##### Keys
documents are addressed in the database via a unique key that represent that document, this key is a simple identifier, typically a string, URL or a path, that is used to retrieve the document from the database. The key is unique within the database, and is used to ensure that each document is stored in a unique location.

5 keys features of a document database include
- Documents at the heart of this type of document lies the document itself, which is a self-contained unit of data that contains all the information needed to represent a single entity. This document can be stored in a variety of formats, such as JSON, BSON, XML, or YAML, and can contain nested structures, arrays, and other complex data types.

- Collections - documents are typically organized into collections, which are groups of related documents that share a common structure or purpose. Collections can be thought of as tables in a relational database, and are used to group together documents that are related to each other in some way.

- Flexible schema - document databases are schema-less, which means that there is no need to define the structure of the data before storing it. This allows for a high degree of flexibility and scalability, as new fields can be added to documents on the fly, and documents with different structures can be stored in the same collection.

- Scalability - document databases are designed to be highly scalable, and can easily handle large amounts of data and high traffic loads. This makes them ideal for applications that require a high degree of flexibility and scalability, such as content management systems, e-commerce platforms, and social media applications.

- Integrated data retrival - document databases typically provide integrated data retrieval capabilities, which allow developers to query and retrieve data from the database using a simple and intuitive API. This makes it easy to build applications that require complex data retrieval operations, such as search engines, recommendation systems, and analytics platforms.

#### most popular document stores
- MongoDB
- Amazon dynamodb
- databricks
- mirosoft azure cosmos db
- couchbase

we showed a slide that show the different between relational database and document databse, and we showed the difference between the two, and how they are different in the way they store data, and how they are different in the way they are queried.

example, banks will use relational databases, and evolving database, content managent systems will use document databases.

#### Scaling
- vertical scaling - adding more power to the machine, more CPU, more memory, more disk etc, (or bigger machine stronger etc)

- horizontal scaling - adding more machines, more servers, more nodes etc. 

we talked a little about json. attribute-value pairs and arrays. 

example json:
```json
{
    "name": "John Doe",
    "age": 30,
    "email": "aaaa",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "NY",
        "zip": "12345"
    },
    "children": [
        {
            "name": "Jane Doe",
            "age": 5
        },
        {
            "name": "Jack Doe",
            "age": 3
        }
    ]
}
```
not each value has to have each field.

### Amazon DynamoDb
Serverless,nosql,fully managed database service, that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.

you only pay for what you use.

DynamoDb offers a broad set of security features and capabilities that allow you to control who can access your data. DynamoDb is a fully managed, multi-region, multi-master database that provides consistent single-digit millisecond latency, and offers built-in security, backup and restore, and in-memory caching.
With DynamoDb streams, you can build serverless applications that react in real-time to changes in your data. DynamoDb global tables replicate your Amazon DynamoDb tables automatically across your choice of AWS regions. DynamoDb global tables provide a fully managed solution for deploying a multi-region, multi-master database, without having to build and maintain your own replication solution.

### pricing
- pay for what you use
- Provisioned capacity mode - you specify the number of reads and writes per second that you require for your application, and DynamoDb provisions the necessary resources to meet your needs. You are billed based on the capacity that you provision, regardless of how much you use.

### MongoDB

one of the most popular document stores, and it is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.

you can run Mondodb in the following enviroments:

- MongoDB Atlas - a fully managed cloud database service that provides all the features of MongoDB without the operational heavy lifting required for any new application.

- MongoDB Enterprise Server - the commercial edition of MongoDB, available as part of the MongoDB Enterprise Advanced subscription.

- MongoDB Community - the open-source edition of MongoDB, available under the GNU Affero General Public License.

so enterprise is good for ones for dont want the cloud. and prefer local installation.

#### Main features of MongoDB

- CRUD operations - MongoDB provides a rich set of CRUD operations, including insert, update, delete, and find, that allow you to interact with your data in a flexible and powerful way.

- Ad hoc queries - MongoDB supports ad hoc queries, which allow you to query your data in a flexible and dynamic way, without the need to define a schema or structure beforehand.

- indexing - MongoDB supports indexing, which allows you to create indexes on your data to improve query performance and reduce latency.

- Replication - MongoDB supports replication, which allows you to create multiple copies of your data across different servers to ensure high availability and fault tolerance. replicas set consist of two or more copies of the data, each stored on a different server.

- Load balancing - MongoDB supports load balancing, which allows you to distribute read and write operations across multiple servers to improve performance and scalability. it uses sharding to distribute data across multiple servers, and to balance the load on each server.

- file storage - MongoDB supports file storage, which allows you to store and retrieve large files, such as images, videos, and other binary data, directly in the database. called GridFS.

- Aggregation - aggregation framework allows you to perform complex data processing operations on your data, such as filtering, grouping, sorting, and transforming, using a simple and expressive syntax. similar to sql group be etc.

- Serverside javascript execution - MongoDB supports serverside javascript execution, which allows you to run javascript code directly on the server, to perform complex data processing operations, such as data validation, transformation, and aggregation.

- atlas charts - MongoDB atlas provides a built-in charts feature that allows you to create and share visualizations of your data, using a simple and intuitive interface. you can create a variety of charts, such as bar charts, line charts, pie charts, and scatter plots, to visualize your data in a meaningful way.

#### Schema 1
unlike sql that require you to define schema efore inserting data, mongodb allows you to insert data without defining a schema beforehand. this means that you can insert data into a collection without specifying the structure of the data, and mongodb will automatically create a schema for you based on the data that you insert.

Advantages:
- intuitive data model - build with a model that fast and easy to use

- flexible schema - no need to define a schema before inserting data

- scalable platform - grow with your application

#### Schema 2

- embedding 
- advantages - you can retrive all relevant information in a single query.
- advantages - avoid implemnting join in application code or using lookup

- limitations 
- large documents mean more overhead if most fields are not relevant. you can increase query performance by limiting size of the documents that you are sending over the wire for each query.
- limit of 16 documents size limit in MongoDB , if you are embdding too much data inside a single you can potentially hit this limit.

Concepts:
- database - a container for collections
- collection - a container for documents
- document - a set of key-value pairs
- field - a key-value pair in a document
- field path - path to a field in a document. to specify a field path, use a string that prefix the field name with the $ character. for example, the field path for the field name in the document {name: "John Doe"} is $name.
- json - a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. json is based on a subset of the javascript programming language, standard ECMA-262 3rd edition - december 1999.
- bson - binary json. a binary-encoded serialization of json-like documents. bson is designed to be lightweight, traversable, and efficient. bson is used by mongodb to store documents in collections.
- _id - a unique identifier for a document in a collection. the _id field is automatically added to a document when it is inserted into a collection, if the document does not already contain an _id field. the _id field is indexed by default, and is used to uniquely identify a document in a collection.
- objectId - a 12 byte bson type that is used as a unique identifier for a document in a collection. the objectId is generated by mongodb when a document is inserted into a collection, and is used to uniquely identify the document in the collection. the objectId is composed of a 4 byte timestamp, a 5 byte random value, a 3 byte incrementing counter, and a 4 byte machine identifier.
- primary key - a field in a document that uniquely identifies the document in a collection. the primary key is used to uniquely identify a document in a collection, and is typically indexed for fast retrieval. the primary key is often the _id field in a document, but can be any field that uniquely identifies the document in the collection.
- query - a request for data from a collection. a query is used to retrieve data from a collection that matches a set of criteria. a query is specified using a query language that is similar to the javascript programming language, and is used to filter, sort, and limit the data that is returned from the collection.
- index - a data structure that is used to optimize the performance of queries on a collection. an index is created on one or more fields in a collection, and is used to quickly locate and retrieve documents that match a set of criteria. an index is typically created on fields that are frequently queried, and is used to speed up the retrieval of data from the collection.
- opeartor - a symbol or keyword that is used to perform a specific operation on a field in a document. an operator is used in a query to filter, sort, and limit the data that is returned from a collection. an operator is typically used in conjunction with a field path to specify the field that the operation should be performed on.
- pipeline - a sequence of stages that are used to process data in a collection. a pipeline is used in an aggregation operation to transform, filter, and group the data that is returned from a collection. a pipeline is composed of one or more stages, each of which performs a specific operation on the data that is passed through the pipeline.

#### MongoDb Find
##### Find Data
to  select data from a collection in mongo db, we can use find() method.
posts name of the collection
db.posts.find()

##### Query
to query data from a collection in mongo db, we can use find() method. or findOne() method.
db.posts.find({name: "John Doe"})
db.posts.find({category: "news"})

example json: 
```json
{
    "name": "John Doe",
    "age": 30,
    "email": "aaaa",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "NY",
        "zip": "12345"
    },
    "children": [
        {
            "name": "Jane Doe",
            "age": 5
        },
        {
            "name": "Jack Doe",
            "age": 3
        }
    ]
}
```

##### Projection
the find methods accept a second parameter called projection
this paramter is an object that describes hich fields to include in the results
the paramter isoptional, if omitted all fields will be included in the results
example:
```MongoDB
db.posts.find({}, {name: 1, email: 1}) 
// so find me all, but return only name and email for each object
```

##### Operators
- $eq - equal
- $ne - not equal
- $gt - greater than
- $gte - greater than or equal
- $lt - less than
- $lte - less than or equal
- $in - in
- $nin - not in
- $and - and
- $or - or
- $not - not
- $nor - nor
- $regex - regex
- $exists - exists
- $text - text

example:
```MongoDB
db.posts.find({age: {$gt: 25}})
```

##### dot notation
to query fields in nested documents, use dot notation
arrays to speicfiy or access an elemtn of an array by the zero based index position, concatenate the array field with the dot (.) and zero-based index position, and enclose in quotes
example:
```MongoDB
db.posts.find({"address.city": "Anytown"})
```
another example with multiply searched in the find:
```MongoDB
db.posts.find({ [{age: {$gt: 25}}, {category: "news"}]})
```

##### Aggregation pipeline
the aggregation pipeline is a framework for performing aggregation operations on a collection in mongo db. the pipeline is composed of one or more stages, each of which performs a specific operation on the data that is passed through the pipeline. the pipeline stages are executed in sequence, with the output of each stage serving as the input to the next stage. the aggregation pipeline is used to transform, filter, and group the data that is returned from a collection, and is used to perform complex data processing operations on the data.

the aggregation pipeline is composed of the following stages:
- $match - filters the documents in the collection that match the specified criteria
- $project - reshapes the documents in the collection by including, excluding, or renaming fields
- $group - groups the documents in the collection by a specified field and calculates aggregate values for each group
- $sort - sorts the documents in the collection by a specified field
- $limit - limits the number of documents in the collection that are returned by the pipeline
- $skip - skips a specified number of documents in the collection before returning the remaining documents
- $unwind - deconstructs an array field in the documents in the collection into separate documents
- $lookup - performs a left outer join on two collections in the database
- $addFields - adds new fields to the documents in the collection
- $replaceRoot - replaces the root document with a specified document
- $facet - performs multiple aggregation operations on the documents in the collection
- $out - writes the output of the aggregation pipeline to a new collection in the database

##### Group
the $group stage groups the documents in the collection by a specified field and calculates aggregate values for each group. the $group stage is used to perform group by operations on the data that is returned from the collection, and is used to calculate aggregate values, such as counts, sums, averages, and maximums, for each group.

example:
```MongoDB
db.listingAndReviews.aggregate([
    {$group: {_id: "$address.country"}}
])
```
so this will return all the countries fields in the collection.

##### limit
the $limit stage limits the number of documents in the collection that are returned by the pipeline. the $limit stage is used to restrict the number of documents that are returned from the collection, and is used to limit the amount of data that is processed by the pipeline.

example:
```MongoDB
db.movies.aggregate([
    {$limit: 5}
])
``` 

// so this will return only 5 documents from the collection.


##### project
the $project stage reshapes the documents in the collection by including, excluding, or renaming fields. the $project stage is used to transform the data that is returned from the collection, and is used to include, exclude, or rename fields in the documents.

example:
```MongoDB
db.restaurants.aggregate([
    {$project: {name: 1, cuisine: 1}}
    $limit: 5
])
```
this is in the pipeline, first aggregate the data, then project the data, then limit the data.

##### sort
this aggregation stage sorts the documents in the collection by a specified field. the $sort stage is used to order the data that is returned from the collection, and is used to sort the documents in ascending or descending order.

example:
```MongoDB
db.listingAndReview.aggregate([
    {$sort: {name: 1}}
    {$project: {name: 1, cuisine: 1}}
    {$limit: 5}
])
```

##### match
the $match stage filters the documents in the collection that match the specified criteria. the $match stage is used to filter the data that is returned from the collection, and is used to select only the documents that match the specified criteria.

example:
```MongoDB
db.listingAndReview.aggregate([
    {$match: {cuisine: "Italian"}}
    {$project: {name: 1, cuisine: 1}}
    {$limit: 5}
])
```
the order of the stages is important, the match stage is the first stage in the pipeline, so it will filter the data first, then the project stage will reshape the data, and the limit stage will limit the data.
better to use match at the start of the pipeline. so you filter rows before doing more actions on them

##### addFields
the $addFields stage adds new fields to the documents in the collection. the $addFields stage is used to add new fields to the data that is returned from the collection, and is used to calculate new values, concatenate strings, or perform other operations on the data.

example:
```MongoDB
db.restaurants.aggregate([
    {$addFields: {fullAddress: {$concat: ["$address.building", " ", "$address.street"]}}}
    {$project: {name: 1, cuisine: 1, fullAddress: 1}}
    {$limit: 5}
])
```
another example with average gradE:
```MongoDB
db.restaurants.aggregate([
    {$addFields: {averageGrade: {$avg: "$grades.score"}}}
    {$project: {name: 1, cuisine: 1, averageGrade: 1}}
    {$limit: 5}
])
```

##### count
the $count stage counts the number of documents in the collection that are returned by the pipeline. the $count stage is used to calculate the total number of documents that are returned from the collection, and is used to count the number of documents that match the specified criteria.

example:
```MongoDB
db.restaurants.aggregate([
    {$match: {cuisine: "Italian"}}
    {$count: "total"}
])
```
first match, than count, will return the total number of documents that match the criteria. (single line)

##### unwind