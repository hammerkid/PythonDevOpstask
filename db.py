import MySQLdb

def connection():
"""connector to mysql  db"""
    conn = MySQLdb.connect(host="192.168.33.13",
                           user = "user",
                           passwd = "password",
                           db = "test")
    c = conn.cursor()

    return c, conn

if __name__ == '__main__':
    connection()
