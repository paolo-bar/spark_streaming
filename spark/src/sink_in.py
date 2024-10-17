# https://spark.apache.org/docs/3.5.1/structured-streaming-programming-guide.html

from pyspark.sql import SparkSession, DataFrame


def read_kafka(spark: SparkSession, kafka_opts: dict = None):
    kafka_stream: DataFrame = (
        spark
        .readStream
        .format("kafka")
        .options(**(kafka_opts or {}))
        .load()
    )

    return kafka_stream
