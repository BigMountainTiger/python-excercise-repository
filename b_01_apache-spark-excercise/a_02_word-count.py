from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count") \
      .setMaster("local[2]")

    context = SparkContext(conf = conf)
    context.setLogLevel('ERROR')
    
    data = ('This', 'is', 'is', 'cool')
    rdd = context.parallelize(data, 2).cache()
    
    print('No of partitions - {}'.format(rdd.getNumPartitions()))
    wordCounts = rdd.countByValue()
    for word, count in wordCounts.items():
        print("{} : {}".format(word, count))

    print('\nReduce by key:')
    new_rdd = rdd.map(lambda x: (x,1), preservesPartitioning=True)
    result = new_rdd.reduceByKey(lambda a, b: a + b).collect()

    print(result)
    for word, count in result:
        print("{} : {}".format(word, count))