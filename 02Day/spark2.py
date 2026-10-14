from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Spark2Test").getOrCreate()

try:
    orders_data = [(1,"당근",2000),(2,"당근",2000),(3,"양파",3000),(4,"버섯",2100)]
    df = spark.createDataFrame(orders_data,["ID","상품명","가격"])
    
    result_df = df.groupBy("상품명").agg(F.sum("가격").alias("총가격"))
    result_df.show()
finally:
    spark.stop()