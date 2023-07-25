import psycopg2 as psy
DB_HOST = "127.0.0.1"
DB_NAME = "zhguti0.0"
DB_USER = "postgres"
DB_PASS = "12345"

def query_maker(cmd):
    conn = psy.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)
    cur = conn.cursor()
    cur.execute(cmd)
    try:
        rows = cur.fetchall()
    except:
        conn.commit()
        conn.close()
        return  True
    conn.commit()
    conn.close()
    cur.close()
    return  rows if rows else []