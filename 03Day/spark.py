
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("myApp").getOrCreate()

try:
    df = spark.read.csv("./data/orders.csv", inferSchema=True, header=True)
    result_df = df.filter(df["status"] == "완료").groupBy("city").agg(F.count("*").alias("주문횟수"), F.sum("amount").alias("총액")).orderBy(F.desc("총액"))
    result_df.show()
finally:
    spark.stop()