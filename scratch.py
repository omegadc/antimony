import sqlite3
import requests


# https://github.com/davemachado/public-api
url = 'https://api.publicapis.org/entries'

response = requests.get(url)
data = response.json()

# Make a table for 'API' and 'Link'
con = sqlite3.connect('apis.db')
cur = con.cursor()

cur.execute('''CREATE TABLE apis
               (API text, Link text)''')

for row in data['entries']:
    cur.execute(f"INSERT INTO apis VALUES (?, ?)", (row['API'], row['Link']))

con.commit()

for row in cur.execute('select * from apis limit 3'):
    print(row)

con.close()
