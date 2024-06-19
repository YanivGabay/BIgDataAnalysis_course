

##Apache Spark

### Resilient Distributed Datasets (RDDs)
the main abstraction in Spark. An RDD is a distributed collection of elements. RDDs are created by starting with a file in the Hadoop file system (or any other Hadoop-supported file system), or an existing Scala collection in the driver program, and transforming it. Users may also ask Spark to persist an RDD in memory, allowing it to be reused efficiently across parallel operations. Finally, RDDs automatically recover from node failures.

a second abstraction in Spark is shared variables that can be used in parallel operations. By default, when Spark runs a function in parallel as a set of tasks on different nodes, it ships a copy of each variable used in the function to each task. Sometimes, a variable needs to be shared across tasks, or between tasks and the driver program. Spark supports two types of shared variables: broadcast variables, which can be used to cache a value in memory on all nodes, and accumulators, which are variables that are only “added” to, such as counters and sums.

### RDDs
parallelized collections of objects. RDDs can be created from Hadoop InputFormats (such as HDFS files) or by transforming other RDDs can also s3, cassandra, HBase, etc.

external datasets can be stored in HDFS, HBase, or any data source offering a Hadoop InputFormat.

sparkContext is the main entry point for Spark functionality. A sparkContext represents the connection to a Spark cluster, and can be used to create RDDs, accumulators, and broadcast variables on that cluster.

we will work probaly with google colab, so we will not need to install spark, we will just need to import it.
and we will work on local mode.

```python
from pyspark import SparkContext
sc = SparkContext()
```

### spark version 3.5.0
using python, on windows the installation is a bit tricky, but it can be done.

### Rdd operations
- lazy evaluation
  lazy evaluation means that the execution will not start until an action is called.

- transformations
    - map
    - filter
    - flatMap
    - mapPartitions
    - mapPartitionsWithIndex
    - sample
    - union
    - intersection
    - distinct
    - groupByKey
    - reduceByKey
    - aggregateByKey
    - sortByKey
    - join
    - cogroup
    - cartesian
    - pipe
    - coalesce
    - repartition
    - repartitionAndSortWithinPartitions
- actions
    - reduce
    - collect
    - count
    - first
    - take
    - takeSample
    - takeOrdered
    - saveAsTextFile
    - saveAsSequenceFile
    - saveAsObjectFile
    - countByKey
    - foreach
- passing functions to spark
    passing functions to spark can be done in two ways:
    - lambda functions
    - named functions

- understanding closures
    understanding closures is important when working with spark. A closure is a function that captures the variables in its scope. When a function is passed to spark, it is serialized and sent to the workers. The variables that are used in the function are also sent to the workers. This is called a closure.

- working with key/value pairs
    key/value pairs are a common data structure in spark. They are used in many operations such as groupByKey, reduceByKey, and join. Key/value pairs are represented as tuples in spark.