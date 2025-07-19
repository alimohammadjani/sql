import sqlite3
import pandas as pd

conn=sqlite3.connect("movie.db")

query="""
SELECT *
FROM movie;
WHERE CONDITITION
"""
df=pd.read_sql_query(query,conn)
conn.close()
print(df)