import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def open_session():
    session = Cluster(
        cloud={"secure_connect_bundle": "assets/secure-connect-video-bop.zip"},
        auth_provider=PlainTextAuthProvider("token", "AstraCS:pJddnCBFdFEzWKTJiPvAQgPu:dc08c258456bf1a4a99bbc878cd79b22621342a8ed0db8a818273f328f937dc2"),
    ).connect()

    return session

def create_table(session, keyspace, table):
    session.execute((f'CREATE TABLE IF NOT EXISTS {keyspace}.{table} (id INT PRIMARY KEY, url TEXT, start_time Text, start_word Text, end_word Text);'))

def write_to_table(session, keyspace, table, text_blocks):
    for block in text_blocks:
        id, url, start_time, start_word, end_word = block
        session.execute(
            f"INSERT INTO {keyspace}.{table} (id, url, start_time, start_word, end_word) VALUES (%s, %s, %s, %s, %s)",
            (id, url, start_time, start_word, end_word)
        )

def read_from_table(session, keyspace, table):
    ann_query = (
        f"SELECT id, url, start_time, start_word, end_word FROM {keyspace}.{table}"
    )
    res = []
    for row in session.execute(ann_query):
        res.append([row.id, row.url, row.start_time, row.start_word, row.end_word])
    return res

def delete_table_values(session, keyspace, table):
    session.execute(f"DELETE FROM {keyspace}.{table} WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);")

def delete_table(session, keyspace, table):
    session.execute(f"DROP TABLE {keyspace}.{table}")

def close_session(session):
    session.shutdown()

    
