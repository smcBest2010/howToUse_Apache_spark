from pyspark.sql import SparkSession 
from pyspark.sql import functions as F 

spark = SparkSession.builder.appName("day05").getOrCreate() 

try: 
    df = spark.read.csv("../03Day/data/sales.csv", header=True, inferSchema=True) 
    
    result_df = df.groupBy("city").agg( 
        F.count("*").alias("총주문"), 
        F.sum(F.when(df["status"] == "취소", 1).otherwise(0)).alias("취소주문") 
    ) 
    
    result_df = ( 
        result_df 
        .withColumn("취소율", F.round(F.col("취소주문") / F.col("총주문") * 100, 2)) 
        .orderBy(F.desc("취소율"), "city") 
    ) 
    result_df.show() 

finally: 
    spark.stop()
