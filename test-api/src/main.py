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
