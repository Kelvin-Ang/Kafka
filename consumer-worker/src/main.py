import os

from functools import reduce
from typing import List
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from bson.objectid import ObjectId
import pymongo
from fastapi import Depends, FastAPI, HTTPException, status, Query
import datetime
from kafka import KafkaConsumer
import json
ISDEV = True if os.getenv('ISDEV') else False
from kafka.admin import KafkaAdminClient, NewTopic
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9092",
    client_id='test'
)

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    'my_topic', # Topic name
    bootstrap_servers=['kafka:9092'], # Kafka broker address
    auto_offset_reset='earliest', # Start reading at the earliest available message
    enable_auto_commit=True, # Auto commit offsets
    group_id='my-group', # Consumer group id
    key_deserializer=lambda k: k.decode('utf-8'), # Deserialize keys from UTF-8
    value_deserializer=lambda v: json.loads(v.decode('utf-8')) # Deserialize values from JSON
)


# app = FastAPI(
#     title="Test API",
#     description="SmartGym API for MHA related activities",
#     root_path="" if ISDEV else "/rt/v1",
# )

# security = HTTPBasic()



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# Consume messages
for message in consumer:
    logging.info(f"Consumed message: key={message.key}, value={message.value}")

