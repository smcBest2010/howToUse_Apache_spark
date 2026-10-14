from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("MyAwesomeSparkApp").getOrCreate()
try:
    data = [(1,2,"김철수"),
            (2,4,"엄준식"),
            (1,2,"노은현"),
            (1,3,"이재용"),
            (3,1,"김도환")]
    orders = spark.createDataFrame(data,["학년","반","이름"])

    # 학년으로 묶어서 몇명있는지 데이터 프레임 만들기
    result_df = orders.groupBy("학년").agg(F.count("이름").alias("학생수"))
    result_df.show()
    
finally:
    spark.stop