https://medium.com/@tarekeesa7/how-to-install-apache-kafka-on-macos-linux-and-ubuntu-cc9af06d77c8

### Step 0: INIT Working directory
```bash
# TERMINAL 0
ROOT_KAFKA="/<path_to_project_streaming>/kafka/bin"
mkdir -p ${ROOT_KAFKA}
cd ${ROOT_KAFKA}
```

### Step 1: Download Kafka Binary
```bash
# TERMINAL 0
ROOT_KAFKA="/<path_to_project_streaming>/kafka/bin"
cd ${ROOT_KAFKA}

# Download the Kafka binary.
wget https://archive.apache.org/dist/kafka/3.5.1/kafka_2.12-3.5.1.tgz

# Extract the downloaded tar file:
tar -xzf kafka_2.12-3.5.1.tgz
cd kafka_2.12-3.5.1

exit
```

### Step 2: Start Zookeeper and Kafka Services
Kafka uses Zookeeper to manage distributed brokers.

#### 1.Start Zookeeper
Open a new terminal window or tab and start the Zookeeper service:
```bash
# TERMINAL 1
ROOT_KAFKA="/<path_to_project_streaming>/kafka/bin"
cd "${ROOT_KAFKA}/bin/kafka_2.12-3.5.1"

./bin/zookeeper-server-start.sh config/zookeeper.properties
```

#### 2.Start Kafka Server
Open a new terminal window or tab and start the Kafka broker service:
```bash
# TERMINAL 2
ROOT_KAFKA="/<path_to_project_streaming>/kafka/bin"
cd "${ROOT_KAFKA}/bin/kafka_2.12-3.5.1"

./bin/kafka-server-start.sh config/server.properties
```

### Step 3: Create Kafka Topics and Produce Data
Open a new terminal window or tab.

```bash
# TERMINAL 3
ROOT_KAFKA="/<path_to_project_streaming>/kafka/bin"
cd "${ROOT_KAFKA}/bin/kafka_2.12-3.5.1"

# # DELETE TOPIC
# ./bin/kafka-topics.sh --delete --topic topic_1 --bootstrap-server localhost:9092

# CREATE TOPICS
# Create a topic in Kafka to publish and consume messages
./bin/kafka-topics.sh --create --topic topic_1 --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
./bin/kafka-topics.sh --create --topic topic_2 --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

# PRODUCE DATA
# Use Kafka's producer to send data to your topic
# Start Producer
# ./bin/kafka-console-producer.sh --topic topic_1 --bootstrap-server localhost:9092
cd "${ROOT_KAFKA}"
bash producer.sh
```

You can now type messages into the console to send to the topic.

### Step 4: Consume Data

Open a new terminal window or tab.

```bash
# TERMINAL 4
ROOT_KAFKA="/<path_to_project_streaming>/kafka/bin"
cd "${ROOT_KAFKA}/bin/kafka_2.12-3.5.1"

# CONSUME DATA
# Use Kafka’s consumer to read data from your topic:
./bin/kafka-console-consumer.sh --topic topic_1 --from-beginning --bootstrap-server localhost:9092
```

This command consumes messages from the specified topic and prints them to the console.
