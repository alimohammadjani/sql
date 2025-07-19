# SQLite Movie Database

A simple Python script to create an SQLite database for storing movie information.

## Features

- Creates a SQLite database named `movie.db`
- Defines a table structure for movie data
- Populates the database with sample movie entries
- Includes basic movie information (ID, Title, Director, Year, Duration)

## Database Schema

The `movie` table has the following structure:

| Column         | Type    | Description               |
|----------------|---------|---------------------------|
| Id             | INTEGER | Unique movie identifier   |
| Title          | TEXT    | Movie title               |
| Director       | TEXT    | Movie director            |
| Year           | INTEGER | Release year              |
| Length_minutes | INTEGER | Movie duration in minutes |

## Sample Data

The database is pre-populated with these Pixar movies:

1. Toy Story (1995) - 81 minutes
2. A Bug's Life (1998) - 95 minutes  
3. Toy Story 2 (1999) - 93 minutes
4. Monsters, Inc. (2001) - 92 minutes
5. Finding Nemo (2003) - 107 minutes

## Requirements

- Python 3.x
- sqlite3 module (included in Python standard library)

## Usage

1. Clone the repository
2. Run the script:
   ```bash
   python movie_database.py