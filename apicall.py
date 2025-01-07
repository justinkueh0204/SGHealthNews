import requests
import json
import sqlite3

# ToDo
# Run a cron job

# Call API OR webscrape
from apikey import api

#Setting API key, see apikey.py
headers = {'x-api-key':'{}'.format(api),}
# printf('{headers}')
# Set parameters
params = {
    'q': 'Health',
    'countries': 'SG',
    'lang': 'en',
    'page_size': '100',
}

# Call API
response = requests.get('https://api.newscatcherapi.com/v2/search', params=params, headers=headers)
response.json()
response_str = json.dumps(response.json())
response_formatted_str = json.dumps(response.json(), indent=2)
print(response_formatted_str)

f = open('/workspaces/54875946/project/formattedapioutput.txt', 'w')
f.write(response_formatted_str)
f.close



f = open('/workspaces/54875946/project/apioutput.txt', 'w')
f.write(response_str)
f.close

formatted_apioutput_json_dict = json.dumps(response.json(), indent = 4)
with open('/workspaces/54875946/project/apioutput.json', 'w') as outfile:
    outfile.write(formatted_apioutput_json_dict)

# Use this section
f = open("/workspaces/54875946/project/apioutput.txt", 'r')
f.seek(0)
print (f.read())
f.close

"""
# Checker to find out where the files are being written to:
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'apioutput.txt')
print(f'The file is located at: {file_path}')
"""


for x in response.json()['articles']:
    print(f'{x}. ' + x["title"] + "-")

"""
# Database
con = sqlite3.connect("articlerecord.db")
cur = con.cursor()
cur.close()
con.close()
"""
"""
Important items to include in table:
title
author
link
summary
date_published
date_circulated (0 if not circulated in telegram, >0 if circulated in telegram)
"""
"""
cur.execute("CREATE TABLE article_table(title, author, link, summary, date_published, date_circulated)")
"""
"""
# Check if table has been created
check = cur.execute("SELECT name FROM sqlite_master")
check.fetchone()
"""

"""
# Print a message
message = "Message from Newscraper.py"
print (message)
"""
