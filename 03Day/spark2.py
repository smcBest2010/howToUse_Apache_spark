from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("myapps").getOrCreate()

try:
    df = spark.read.csv("./data/sales.csv",header=True,inferSchema=True)

    result_df = df.filter((df["status"] == "취소") & (df["amount"] >= 10000)).select("sale_id","category","city","amount").orderBy(F.desc("amount")).limit(3)
    result_df.show()
finally:
    spark.stop()