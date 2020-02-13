from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count") \
      .setMaster("local[2]")

    sc = SparkContext(conf = conf)
    sc.setLogLevel('ERROR')
    
    rdd = sc.parallelize(('This', 'is', 'is', 'cool'), 2)
    
    print('No of partitions - {}'.format(rdd.getNumPartitions()))
    wordCounts = rdd.countByValue()
    for word, count in wordCounts.items():
        print("{} : {}".format(word, count))
