import os
import json
import sqlite3
from datetime import date, datetime

with open('/workspaces/54875946/project/apioutput.json', 'r') as openfile:
    # Reading from json file
    apioutput = json.load(openfile)
    openfile.close()
    # To be continued here
# For debugging
# os.getcwd()

print(apioutput)
## I can't use executemany because it is a list of dictionaries

"""
# Checker to find out where the files are being written to:
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'apioutput.txt')
print(f'The file is located at: {file_path}')
"""
"""
Important variables:
title
author
link
summary
"""

# Table

con = sqlite3.connect("/workspaces/54875946/project/articlerecord.db")
cur = con.cursor()

"""
# Creating a table code
cur.execute("DROP TABLE article_table")
cur.execute("CREATE TABLE article_table \
            (title, \
            author, \
            link, \
            summary, \
            excerpt, \
            date_published, \
            date_circulated)")
con.commit()
cur.close()
con.close()
"""
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

res = cur.execute("SELECT * FROM article_table")
res.fetchall()

"""
# Test code
n = 0
for titlekey in apioutput['articles']:
    n += 1
    titlevalue = titlekey['title']
    print(f'{n}. ' + f'{titlevalue}' )
"""
# Extract all the data and put it into the table
n = 0
for key in apioutput['articles']:
    n += 1
    title_value = key['title']
    author_value = key['author']
    link_value = key['link']
    summary_value = key['summary']
    date_published_value = key['published_date']
    date_circulated_value = 0
    excerpt_value = key['excerpt']
    data = (title_value, author_value, link_value, summary_value, excerpt_value, date_published_value, date_circulated_value)
    cur.execute("INSERT INTO article_table VALUES(?, ?, ?, ?, ?, ?, ?)", data)
    print(f'Row {n} of new data successfully inserted - pending commit')
    # Check
    # print(f'{n}. Title: {title_value} Author: {author_value} Link: {link_value} Date Published: {date_published_value} Date Circulated: {date_circulated_value}')
con.commit()

res = cur.execute("SELECT title, author, date_published FROM article_table")
res.fetchall()

# Duplicate checker duplicates
res = cur.execute("SELECT rowid, title FROM article_table \
                  where rowid in ( \
                  SELECT MIN(rowid) \
                  FROM article_table \
                  GROUP BY link \
                  HAVING COUNT(*) > 1)")

# Creating a list of duplicates because once you use fetchall,
# the results are exhausted and you can't call it again

list_of_duplicates = res.fetchall()
print(list_of_duplicates)
# If list is empty, it'll return as false and hence "no duplicates"
if list_of_duplicates == []:
    print("No duplicates")
else:
    print("Duplicates found")
    # Delete duplicates

res = cur.execute("DELETE FROM article_table where rowid not in \
                    (SELECT MIN(rowid) \
                    FROM article_table \
                    GROUP BY link \
                    HAVING COUNT(*) > 1)")

print("Purged duplicates")

con.commit()

# I need to create a database and check back against all the messages I've created
# The heads should include:
# Title, author, link, summary
# I need to check against the link...?

# Print a message
cur.execute("SELECT * \
            FROM article_table \
            WHERE date_circulated = 0 \
            ORDER BY date_published DESC")
res = cur.fetchall()
latest_article = res[0]
print (latest_article)

"""
res = cur.execute("SELECT MIN(rowid) \
                  FROM article_table \
                  GROUP BY link \
                  HAVING COUNT(*) > 1")
res = cur.execute("SELECT title \
                  FROM article_table \
                  WHERE date_circulated <> 0 \
                  ORDER BY date_published DESC")
res.fetchall()
"""
"""
0 title
1 author
2 link
3 summary
4 excerpt
5 date_published
6 date_circulated
"""
excerpt = latest_article[4]
link = latest_article[2]
print(f'{link}')
message = f'{excerpt} \n {link}'
print(message)

# Dependencies:
# pip install requests
# pip install python-telegram-bot
from typing import Final
import requests

TOKEN: Final = "6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4"
BOT_USERNAME: Final = "@SGHealthNewsBot"
BASE_URL: Final = "https://api.telegram.org/bot6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4/"
BOT_CHECK: Final = "https://api.telegram.org/bot6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4/getUpdates"
CHANNEL_ID: Final = "chat_id=+xPSlsadJxf5lNzBl"

print(message)
send_message = f'https://api.telegram.org/bot6379665692:AAFK5UOFqbwKKGJQGDT-6XPkLbezlF6zzQ4/sendMessage?chat_id=-1002129489446&text={message}'

today = date.today()
now = datetime.now()
print("Today's datetime:", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# print(send_message)
resp = requests.get(send_message)
if resp.ok:
    cur.execute("UPDATE article_table \
                SET date_circulated = (?) \
                WHERE link = (?)", (dt_string, link,))
    print("success")
else:
    print("error")

# Check results
# TODO: Debug the below line
res = cur.execute("SELECT title, date_circulated, link FROM article_table WHERE link = (?)", (link,))
res.fetchall()
con.commit()

cur.close()
con.close()


