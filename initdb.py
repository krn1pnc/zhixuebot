from plugins.utils.db import DB

DB.execute("CREATE TABLE users(qqid INT PRIMARY KEY, username TEXT, password TEXT)")
