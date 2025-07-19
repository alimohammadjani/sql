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
movie_data=[
    (1,"toy story","john lasseter",1995,81),
    (2, 'A Bug''s Life', 'John Lasseter', 1998, 95),
    (3, 'Toy Story 2', 'John Lasseter', 1999, 93),
    (4, 'Monsters, Inc.', 'Pete Docter', 2001, 92),
    (5, 'Finding Nemo', 'Andrew Stanton', 2003, 107)
]
cursor.executemany("INSERT INTO movie VALUES (?,?,?,?,?);", movie_data)
conn.commit()
conn.close()