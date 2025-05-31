from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = SparkSession.builder.appName("FraudETL").getOrCreate()

df = spark.read.csv("data/transactions.csv", header=True, inferSchema=True)

df = df.withColumn("hour", hour("timestamp")) \
    .withColumn("day_of_week", dayofweek("timestamp")) \
        .withColumn("amount_log", log1p("amount"))
        
df = df.withColumn("rule_fraud", (
    (col("amount") > 10000) |
    (col("location") == "Unknown") |
    (col("is_foreign") == 1) |
    (col("is_high_risk_country") == 1)
).cast("int"))

df.write.mode("overwrite").parquet("data/output/fraud_flags")
print("ETL Pipeline executed and data saved to data/output/fraud_flags")