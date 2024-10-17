#!/bin/bash

# sudo apt-get install jq

jq -rc . messages.json | \
./bin/kafka_2.12-3.5.1/bin/kafka-console-producer.sh \
--topic topic_1 \
--bootstrap-server \
localhost:9092



