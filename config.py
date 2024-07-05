from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7336764515:AAE86QqzfI6-fWw7vn0aQ5SCnEj3ZXBquB4")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://musicbot1221:123tecmusic@cluster0.geoo2vm.mongodb.net/?retryWrites=true&w=majority",
)
