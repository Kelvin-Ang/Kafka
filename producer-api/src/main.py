import os

from functools import reduce
from typing import List
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from bson.objectid import ObjectId
import pymongo
from fastapi import Depends, FastAPI, HTTPException, status, Query
import datetime

ISDEV = True if os.getenv('ISDEV') else False

from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9092",
    client_id='test'
)

# topic_list = []
# topic_list.append(NewTopic(name="my_topic", num_partitions=3, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Create a Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'], # Kafka broker address
    key_serializer=lambda k: k.encode('utf-8'), # Serialize keys to UTF-8
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serialize values to JSON
)



app = FastAPI(
    title="Test API",
    description="SmartGym API for MHA related activities",
    root_path="" if ISDEV else "/rt/v1",
)

security = HTTPBasic()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test/")
def test_api(test):
   return test

@app.post("/producer/")
def post_kafka(test):
    key = f'key-{test}'
    value = {'number': test}

    # Send the record
    future = producer.send('my_topic', key=key, value=value)

    try:
        record_metadata = future.get(timeout=10)
        print(f"Produced record to topic {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}")
    except KafkaError as e:
        print(f"Failed to produce record: {e}")
