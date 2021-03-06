# -*- coding: utf-8 -*-
"""Web Scraping with Beautiful Soup.ipynb

### Step 1: Import Libraries
"""
#pip install beautifulsoup4
#pip install pandas
#pip install requests
#pip install openpyxl
from bs4 import BeautifulSoup # For extracting the data from the HTML page
import pandas as pd # Data Manipulation and export
from requests import get # Request URL to access content

"""### Step 2: Create a variable url which contains the link"""

print("Enter any year:")
year = input()
url = 'http://www.imdb.com/search/title?release_date='+year+'&sort=num_votes,desc&page=1'
response = get(url)

""" ### Step 3: Print the response"""

print(response.text[:500])

""" ### Step 3: Use Beautiful Soup to parse the data"""

html_soup = BeautifulSoup(response.text, 'html.parser')

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

"""### Step 4: Initiliaze the lists"""

names = []
imdb_ratings = []
votes = []
runtimes = []
genres = []

"""### Step 5: Start storing the data"""

for countainer in movie_containers:
    name = countainer.h3.a.text
    names.append(name)
    imdb_rating = float(countainer.strong.text)
    imdb_ratings.append(imdb_rating)
    vote = int(countainer.find('span', attrs = {'name':'nv'})['data-value'])
    votes.append(vote)
    runtime = countainer.find('span', attrs = {'class':'runtime'}).text
    runtimes.append(runtime)
    genre = (countainer.find('span', attrs = {'class':'genre'})).text.strip()
    genres.append(genre)
    

"""### Step 6: Verify the stored data"""

print(names)
print(imdb_ratings)
print(votes)
print(runtimes)
print(genres)

"""### Step 7: Store the data"""
df = pd.DataFrame({'Name':names, 'Rating':imdb_ratings, 'Runtime':runtimes, 'Vote':votes, 'Genre':genres})
df.to_excel('Watchlist of '+year+'.xlsx', index=False, encoding='utf-8')

"""### Step 8: Check the final output"""

df.head()

