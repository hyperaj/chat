from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7069105732:AAH5EQKXgovDDJHRVqa5KJJCYqnBWFAUAAg")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://musicheysiri:musicsiri123@cluster0.gozblfn.mongodb.net/?appName=Cluster0",
)
