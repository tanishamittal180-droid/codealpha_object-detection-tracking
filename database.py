import sqlite3

conn=sqlite3.connect("detections.db")

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS detections(
id INTEGER PRIMARY KEY AUTOINCREMENT,
time TEXT,
object_name TEXT,
tracking_id INTEGER
)
""")

conn.commit()

def save_detection(time,object_name,tracking_id):

    cursor.execute(
    '''
    INSERT INTO detections
    (time,object_name,tracking_id)
    VALUES(?,?,?)
    ''',
    (time,object_name,tracking_id)
    )

    conn.commit()