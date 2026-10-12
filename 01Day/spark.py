from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()  # Spark 시작

data = [(1, "사과"), (2, "바나나")]
df = spark.createDataFrame(data, ["번호", "과일"])  # 표 만들기

df.show()  # 표 보기

spark.stop()  # Spark 종료