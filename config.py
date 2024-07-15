from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6762321126:AAFxD_C3N0wOPYjengR9piy1_DAkUqCfiH0")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://musicbot1221:123tecmusic@cluster0.geoo2vm.mongodb.net/?retryWrites=true&w=majority",
)
