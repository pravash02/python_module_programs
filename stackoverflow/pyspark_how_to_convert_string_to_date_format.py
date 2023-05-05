from pyspark.sql import SparkSession
from pyspark.sql.functions import substring
from pyspark.sql.functions import to_date
from pyspark.sql.types import DateType

spark = SparkSession.builder \
    .master("local") \
    .appName("read_json_file_df") \
    .config("spark.some.config.option", "some-value").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

x = [(1, "Mon, 01 Mar 2021 13:23:06 +0000")]
df = spark.createDataFrame(x, schema=["id", "test_started_at"])

df = df.withColumn('new_date', to_date('test_started_at', 'EEE, dd MMM yyyy HH:mm:ss Z').cast(DateType()))

print(df.show())
