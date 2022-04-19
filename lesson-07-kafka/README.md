# Learning Notes

OS: Windows 11

## Step-by-step
1. Start the container with `docker-compose up`
2. Open the control center on `localhost:9021`. Create a new topic, use `demo_1` as its name.
3. Start the Kafka producer by executing the Python script for producer.
```
python producer.py
```
4. Start the Kafka consumer by executing the Python script for consumer.
```
python consumer.py
```
5. To improve the use case, we can use Avro for data serialization system with separate schema. We are using `confluent_kafka` package for Kafka-Avro integration. In some python version, the DLL for `confluent_kafka` is not directly loaded (check https://github.com/confluentinc/confluent-kafka-python/issues/1221). To correctly load the DLL, explicitly state the DLL location before importing `confluent_kafka` by adding these lines:
```
from ctypes import *
CDLL("path_to_confluent_kafka_dll.dll")
```
6. Create a new topic in Kafka control center with the name `datatalkclub.yellow_taxi_rides`.
7. Execute the producer
```
python avro/producer.py
```
8. Execute the consumer
```
python avro/consumer.py
```

**Kafka Streaming, Kafka Connect, and KSQL**

***

## Kafka
1. Three basic components: broker, consumer, producer.

## Avro
1. Data serialization system.
2. Store schema separately.
3. In Kafka, schema are stored in schema registry.