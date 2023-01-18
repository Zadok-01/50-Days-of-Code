# Challenge 46


import pandas as pd


text = '''year Title genre
2009 Brothers Drama
2002 Spider-Man Sci-fi
2009 WatchMen Drama
2010 Inception Sci-fi
2009 Avatar Fantasy
'''

text = text.split('\n')
cols = text[0].split()
table = [row.split() for row in text[1:]]
df = pd.DataFrame(columns=cols, data=table)
print(df)



print('------')

# Challenge 46  --  Extra


import pandas as pd


url = url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
attrs = {'class': 'wikitable'}
cols = ['Type', 'Mutability']
df = pd.read_html(url, attrs=attrs)[0][cols]
print(df)



'''
Challenge #46:

Day 46: Create a DataFrame

Create a Dataframe using pandas. You are going to create a code to put the 
following into a Dataframe. You will use the information in the table 
below. Basically, you are going to recreate this table using pandas. Use 
the information in the table to recreate the table.

year Title genre
2009 Brothers Drama
2002 Spider-Man Sci-fi
2009 WatchMen Drama
2010 Inception Sci-fi
2009 Avatar Fantasy

Extra Challenge: Website Data with Pandas

Create a code that extracts data from a website. You will extract a table 
from the website. And from that table you will extract columns about the 
data types in Python and their mutability. You will extract information 
from the following website:

https://en.wikipedia.org/wiki/Python_(programming_language)

The target table is "Summary of Python's Built in data types"
Once you extract this table, you will write a code that will extract the 
data types and their mutability (Two columns) into a Pandas Dataframe.
'''

