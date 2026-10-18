from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 미션: 배송비를 뺀 도시별 매출
# 완료된 판매마다 배송비가 3,000원 든다고 가정합니다.
# 1. net_amount 컬럼을 만드세요. 값은 amount - 상품*3000입니다.
# 2. 도시별로 net_amount의 합계를 구하세요.
# 3. 합계가 큰 도시부터 출력하세요. 


spark = SparkSession.builder.appName("myapp").getOrCreate()

try:
    df = spark.read.csv("../03Day/data/sales.csv",header=True,inferSchema=True)
    result_df = df.filter(F.col("status") == "완료").groupBy("city").agg(F.count("*").alias("총주문"),
                                                                       F.sum("amount").alias("총매출")
                                                                       ).withColumn("순매출",F.col("총매출") - (F.col("총주문")*3000)).select("city","총주문","순매출").orderBy(F.desc("순매출"))
    result_df.show()
finally:
    spark.stop()
