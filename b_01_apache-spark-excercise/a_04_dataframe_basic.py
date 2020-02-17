from pyspark import SparkContext, SQLContext, SparkConf
from pyspark.sql import Row

def run():
  conf = SparkConf().setAppName("word count") \
    .setMaster("local[2]")

  context = SparkContext(conf = conf)
  sqlContext = SQLContext(context)
  context.setLogLevel('ERROR')

  data = [('Song',25),('Trump',22),('Yong',20),('Obama',26)]
  rdd = context.parallelize(data, 2).map(lambda x: Row(name=x[0], age=int(x[1])))
  people = sqlContext.createDataFrame(rdd).cache()

  people.printSchema()
  old_guy = people.orderBy('age', ascending = False).take(1)
  print(old_guy)

  same_old_guy = [Row(name=x['name'], age=x['age'], other=1) for x in old_guy]
  print(same_old_guy)

  total = people.groupBy().sum('age').collect()[0][0]
  print('Total age is {}'.format(total))

  people.createTempView('people_table')
  new_people = sqlContext.sql('select name, age from people_table order by age desc limit 1')
  new_people.show()
  
# Run the app
if __name__ == "__main__":
  run()