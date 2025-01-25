# SGHealthNews
#### Video Demo:  <https://youtu.be/C7ywx2y7bzA>
### Telegram News Channel: <https://t.me/+xPSlsadJxf5lNzBl>
#### Description:

Overview
This project is designed to fetch health-related news articles in Singapore using the Newscatcher API, store the data in a SQLite database, and circulate the latest articles via a Telegram bot while simultaenously updating the database. The code is written in Python and involves fetching, processing, and managing news data efficiently. The new

Table of Contents
1. Dependencies
2. How It Works
3. Database Schema
4. Telegram Integration

===
1. Dependencies
requests
python-telegram-bot
Install the dependencies using the following:

bash
Copy code
pip install requests
pip install python-telegram-bot

2. How It Works
Fetching News Data:

- The code uses the Newscatcher API to fetch health-related news articles within Singapore.
- The API key is stored in a separate file named apikey.py for security reasons, and is called when I am calling the API.
- The fetched data is then formatted and saved in three different files: apioutput.txt, formattedapioutput.txt, and apioutput.json.
- While apioutput.json is the main folder used for this project, I experimented with other formats for future reference so that I can eventually expand SGHealthNews to other web sources (whether via web scraping or via APIs).

Database Management:
- A SQLite database (articlerecord.db) is used to store the article data.
- The schema of the article_table includes fields for title, author, link, summary, excerpt, date_published, and date_circulated. Date_circulated is set to 0 until the article is published in which case a datetime is set explicitly.
- By separating apicall.py and datasorter.py, I can run the NewsCatcher API (which has limited calls) once, and persist the data within my database. This enables me to further manipulate the data such as by checking whether apiout.json has any duplicate links with database and ensuring that my database only has unique entries, and checking if an article has been previously posted.
- This also sets up an opportunity in the future to have other sources of data that can plug into datasorter.py.


3. Database Schema
The article_table schema includes the following columns:

title - Title of the news article.
author - Author of the article.
link - Link to the article.
summary - Summary of the article.
excerpt - An excerpt from the article.
date_published - Date when the article was published.
date_circulated - Date when the article was circulated via Telegram.

Removing Duplicates:
- The code identifies and removes duplicate articles based on their links. This ensures I will always post a unique link that users can read.

4. Telegram Integration:
- The latest article which has date_circulated = 0 is selected from the database, and its details are formatted into a message. I send the title, excerpt, and link.
- I have set up a Telegram bot and channel. Using POST, my app interacts with the Telegram server to then send the message through the telegram bot. My app then checks for a successful response and upon success, it updates the database to set the date_circulated to today's time. This enables me to keep track of when messages were sent while also preventing me from sending messages I've sent before.


