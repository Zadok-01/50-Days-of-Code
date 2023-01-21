# Challenge 49


from sqlite3 import connect, OperationalError


# data
column_names = 'year, title, genre'

movies_data = [
                ('2009', 'Brothers',   'Drama'), 
                ('2002', 'Spider Man', 'Sci-fi'), 
                ('2009', 'WatchMen',   'Drama'), 
                ('2010', 'Inception',  'Sci-fi'), 
                ('2009', 'Avatar',     'Fantasy'), 
               ]

# create table
con = connect(':memory:')
cur = con.cursor()
cur.execute(f'create table movies ({column_names})')
cur.executemany('insert into movies values (?, ?, ?)', movies_data)

# query 1 - all movies
cur.execute('select * from movies')
rows = cur.fetchall()
print(rows)
print('------')

# query 2 - movie called Brothers
cur.execute('select * from movies where title = "Brothers"')
rows = cur.fetchall()
print(rows)
print('------')

# query 3 - movies released in 2009
cur.execute('select * from movies where year = "2009"')
rows = cur.fetchall()
print(rows)
print('------')

# query 4 - movies in Fantasy and Drama genre
cur.execute('select * from movies where genre = "Fantasy" or genre = "Drama"')
rows = cur.fetchall()
print(rows)
print('------')

# query 5 - delete all contents
cur.execute('drop table movies')

try:
    cur.execute('select * from movies')
    rows = cur.fetchall()
    print(rows)
except OperationalError:
    print('table missing')



'''
Challenge #49:

Day 49: Create a Database

For this challenge, you are going to create a database using Python’s 
SQLite. You will import SQLite into your script. Create a database called 
movies.db. In that database, you are going to create a table called movies. 
In that table, you are going to save the following movies:

year title genre
2009 Brothers Drama
2002 Spider Man Sci-fi
2009 WatchMen Drama
2010 Inception Sci-fi
2009 Avatar Fantasy

Once you create a table, run a SQL query to see all the movies in your 
table. 
Run another SQL query to select only the movie Brothers from the list. 
Run another SQL query to select all movies that were released in 2009 from 
your table.
Run another query to select movies in the fantasy and drama genre. 
Run a query to delete all the contents of your table.
'''

