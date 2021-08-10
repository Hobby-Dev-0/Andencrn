import os
ai = os.environ.get("AIBOT", None)
if ai == "True":
  import asyncio
  import sys
  from motor import motor_asyncio
  from pymongo import MongoClient
  from pymongo.errors import ServerSelectionTimeoutError
  MONGO_URI = os.environ.get("MONGO_URI")
  MONGO_PORT = "27017"
  MONGO_DB = "Andencento"
  mongodb = MongoClient(MONGO_URI, MONGO_PORT)[MONGO_DB]
else:
  return
