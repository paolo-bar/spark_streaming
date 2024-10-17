# https://spark.apache.org/docs/3.5.1/structured-streaming-programming-guide.html
import argparse

import pyspark.sql.functions as f
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import *

from sink_in import read_kafka
from sink_out import write_kafka, write_console

kafka_opts_in = {
    "kafka.bootstrap.servers": "localhost:9092",
    "subscribe": "topic_1",
    "includeHeaders": "true",
    "startingOffsets": "latest",  # earliest|latest
    "failOnDataLoss": "false",
}
json_schema_in = StructType([
    StructField("user_id", StringType()),
    StructField("content", StringType()),
    StructField("watched_at", TimestampType()),
    StructField("rating", IntegerType()),
])


kafka_opts_out = {
    "kafka.bootstrap.servers": "localhost:9092",
    "topic": "topic_2",
    "checkpointLocation": f"/tmp/spark/app__test/checkpoint",
}


def parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument("-o", "--sink-out", type=str, required=True, default=None)

    return _parser


def process_json(spark: SparkSession, df: DataFrame):
    # df is our DataFrame reading from Kafka above
    try:
        # value_df = stream_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
        struct_df = df.select(f.from_json(f.col("value").cast("string"), json_schema_in).alias("value"))
        struct_df.printSchema()

        # AGGREGATED
        struct_df.select("value.*").createOrReplaceTempView("netflix_view")
        res_df = spark.sql(
            f"SELECT content, CAST(AVG(rating) AS STRING) AS avg "
            f"FROM netflix_view "
            f"GROUP BY content"
        )
        res_df.printSchema()

        res_df = res_df.select(f.to_json(f.struct(*res_df.columns)).alias("value"))  # !!! USE 'value' as field name
        # json_schema_ou't = StructType([
        #     StructField("content", StringType()),
        #     StructField("avg", StringType()),
        # ])

    except Exception as e:
        raise e
        # print(e)
        # res_df = spark.createDataFrame(spark.sparkContext.emptyRDD(), json_schema_out)

    return res_df


def main():
    parser_ = parser()
    args_ = parser_.parse_args()
    sink_out = args_.sink_out

    # Initialize Spark session
    spark: SparkSession = (
        SparkSession
        .builder
        # .appName("test_kafka")  # already passed in submit
        # .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1')  # already passed in submit
        .getOrCreate()
    )
    try:
        # read
        stream_df: DataFrame = read_kafka(spark=spark, kafka_opts=kafka_opts_in)

        # process
        processed_df: DataFrame = process_json(spark=spark, df=stream_df)
        processed_df.printSchema()

        # write
        if sink_out == "kafka":
            query = write_kafka(df=processed_df, kafka_opts=kafka_opts_out)
        else:
            query = write_console(df=processed_df)

        query.awaitTermination()

    except Exception as e:
        print(e)
        # raise e


if __name__ == "__main__":
    main()
