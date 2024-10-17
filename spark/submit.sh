#!/bin/bash

ROOT_PATH="/home/paolobar/work/repo/it-data-model/tests/streaming/spark"
VENV="${ROOT_PATH}/.venv"
JARS_PATH="${ROOT_PATH}/jars"


# SPARK
# *************
export SPARK_LOCAL_IP=127.0.0.1
export SPARK_MASTER_HOST=127.0.0.1
export SPARK_HOME="${VENV}/lib/python3.9/site-packages/pyspark"
export PYSPARK_PYTHON=python3
export PATH=$PATH:${SPARK_HOME}/bin:${SPARK_HOME}/sbin
export PYTHONPATH=$(ZIPS=("${SPARK_HOME}"/python/lib/*.zip); IFS=:; echo "${ZIPS[*]}"):${PYTHONPATH}


# CUSTOM
# *************

SINK_OUT=${1:-"console"}

${VENV}/bin/spark-submit \
  --name "test_submit" \
  --master local[4] \
  --deploy-mode client \
  --jars \
"${JARS_PATH}/spark-sql-kafka-0-10_2.12-3.5.1.jar",\
"${JARS_PATH}/spark-streaming-kafka-0-10-assembly_2.12-3.2.1.jar",\
"${JARS_PATH}/commons-pool2-2.11.1.jar" \
  src/main.py \
  "--sink-out" "${SINK_OUT}"

#   --conf spark.eventLog.enabled=false \
