from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("HousePricesAnalysis") \
    .config("spark.jars", "spark/app/jars/postgresql-42.7.1.jar") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/house_prices") \
    .option("dbtable", "public.house_prices") \
    .option("user", "evgen200rom") \
    .option("password", "12345") \
    .load()


df.createOrReplaceTempView("house_prices")

spark.sql("""SELECT AVG(price) AS avg_price,
                    location, 
                    bedrooms
             FROM house_prices
             GROUP BY location, bedrooms""").show()

