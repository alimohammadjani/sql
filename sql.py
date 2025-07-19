import sqlite3

conn=sqlite3.connect("movie.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS movie(
    Id INTEGER,
    Title TEXT,
    Director TEXT,
    Year INTEGER,
    Length_minutes INTEGER
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS BoxOffice (
    Movie_id INTEGER,
    Rating REAL,
    International_sales INTEGER
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
BoxOffice_data=[
    (1, 8.3, 373600000),
    (2, 7.2, 363300000),
    (3, 7.9, 497300000),
    (4, 8.1, 577400000),
    (5, 8.2, 940300000) 
]
cursor.executemany("INSERT INTO BoxOffice VALUES (?,?,?);", BoxOffice_data)

conn.commit()
conn.close()