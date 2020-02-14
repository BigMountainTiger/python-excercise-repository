from pyspark import SparkContext, SparkConf
import os

def getAList(id):
  return ['This', 'is', 'Item-{}-{}'.format(id, os.getpid())]

def a_03_flatamp_parallel():
  conf = SparkConf().setAppName("word count") \
    .setMaster("local[2]")

  context = SparkContext(conf = conf)
  context.setLogLevel('ERROR')
  
  rdd = context.parallelize([1, 2], 2) \
    .flatMap(lambda id: getAList(id)).cache()
  
  print()
  print('No of partitions - {}'.format(rdd.getNumPartitions()))
  print('Word count:')
  wordCounts = rdd.countByValue()
  for word, count in wordCounts.items():
      print("{} : {}".format(word, count))

  count = rdd.count()
  print('Total count - {}'.format(count))

if __name__ == "__main__":
  a_03_flatamp_parallel()
