"""
This starter code scrapes the url of the Project Gutenberg's Top 100 ebooks for identifying the ebook links
It uses BeautifulSoup4 for parsing the HTML and regular expression code for identifying the Top 100 ebook file numbers
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read the HTML from the URL and pass on to BeautifulSoup
url = "https://www.gutenberg.org/browse/scores/top"
print("Opening the file connection...")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Empty list to hold all the http links in the HTML page
lst_links = []

# Find all the href tags and store them in the list of links
for link in soup.find_all("a"):
    # print(link.get('href'))
    lst_links.append(link.get("href"))

# Use regular expression to find the numeric digits in these links. These are the file number for the Top 100 books.
import re

# Initialize empty list to hold the file numbers
booknum = []

# Number 19 to 119 in the original list of links have the Top 100 books' number.
for i in range(19, 119):
    link = lst_links[i]
    link = link.strip()
    # Regular expression to find the numeric digits in the link (href) string
    n = re.findall("[0-9]+", link)
    if len(n) == 1:
        # Append the filenumber casted as integer
        booknum.append(int(n[0]))

print(
    "\nThe file numbers for the top 100 ebooks on Gutenberg are shown below\n"
    + "-" * 70
)
print(booknum)
