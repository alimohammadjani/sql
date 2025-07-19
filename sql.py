import sqlite3

conn=sqlite3.connect("movie.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS movie(
    Id INTEGER
    Title TEXT
    Director TEXT
    Year INTEGER
    Length_minutes INTEGER
);
""")