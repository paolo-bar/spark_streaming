from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery

# https://spark.apache.org/docs/3.5.1/structured-streaming-programming-guide.html#output-sinks


def write_console(df: DataFrame):
    query: StreamingQuery = (
        df
        .writeStream
        .outputMode("complete")  # append|complete - switch to "complete" when there are streaming aggregations
        .format("console")
        .start()
    )

    # query.awaitTermination()

    return query


def write_kafka(df: DataFrame, kafka_opts: dict = None):
    # https://spark.apache.org/docs/3.5.1/structured-streaming-kafka-integration.html#writing-data-to-kafka
    if "value" not in df.columns:
        raise Exception(
            f"The Dataframe being written to Kafka should have the following schema:\n"
            f"root\n"
            f" |-- key: string (nullable = true)\n"
            f" |-- value: string (nullable = false)\n"
            f" |-- headers: array (nullable = true)\n"
            f" |-- topic : string (nullable = true)\n"
            f" |-- partition : int (nullable = true)\n"
        )

    query: StreamingQuery = (
        df
        .writeStream
        .format("kafka")
        .outputMode("complete")  # append|complete - switch to "complete" when there are streaming aggregations
        .options(**(kafka_opts or {}))
        # .trigger(continuous="1 second")
        .start()
    )
    # query.awaitTermination()

    return query
