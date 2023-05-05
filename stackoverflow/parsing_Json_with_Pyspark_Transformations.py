from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import functions as F
import json

spark = SparkSession.builder \
    .master("local") \
    .appName("read_json_file_df") \
    .config("spark.some.config.option", "some-value").getOrCreate()
sc = spark.sparkContext
sqlContext = SQLContext(sc)

simple_json = {}

with open("test_2.json") as file:
    data = json.load(file)

lst = []
for k, v in data.items():
    lst.append(v)
simple_json["results"] = lst

rddjson = sc.parallelize([simple_json])
df = sqlContext.read.json(rddjson, multiLine=True)

df.select(F.explode(df.results).alias('results')).select('results.*').show(truncate=False)

# https://stackoverflow.com/questions/49399245/read-json-file-as-pyspark-dataframe-using-pyspark