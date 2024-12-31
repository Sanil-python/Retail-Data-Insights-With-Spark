import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from src.main.utility.logging_config import *

def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("sanil_spark2")\
        .config("spark.driver.extraClassPath", "C:\\mysql-connector-j-9.0.0\\mysql-connector-j-9.0.0.jar") \
        .getOrCreate()
    logger.info("spark session %s", spark)
    return spark