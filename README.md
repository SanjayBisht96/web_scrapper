
TASK 
========================================================

Write a webscraper application in Python that solves the following tasks: 

Task 1: Download all PDF files from this webpage into a folder called “Math Problems.” 

Task 2: Go to the US Census publications website, sort by “Oldest to Newest” using the toggle, and download and organize all files less than 5 MB in size from the 20 oldest publications into separate folders inside a main folder called “Census Publications”. Name each separate folder containing the downloaded publications by the name of the publication. The output should have the following structure:   

=========================================================

SOLUTION TASK 1
=========================

- Fetch the html tree using Beautiful soup 
- Get all anchor tags with href ending with PDF
- Validate the url
- Download the final urls

==========================================================


SOLUTION TASK 2
===========================


- Used selenium to simulate user interaction
- Used driver to toggle to 'Oldest to Newest' Option
- Fetch Html tree for updated page using BeautifulSoup
- Use Soup to get all articles and their titles

- Use article links to fetch the respective pages

- For each article page:
  - Fetch html tree and get all anchor tags with href
  - Validate the href urls
  - Fetch header for url to be downloaded
  - Download url content if 'content-length' < 5MB or is 'content-length' is not present in header else move to next url
  - Download the url using chunks if at any point file size exceeds 5 MB delete file and stop current url download move to next url

- After parsing Delete all directories inside "Census Publications” which are empty
===========================================================


- Modules used:
  - web_driver: To create a driver of suitable browser
  - simulate_user_behavior: To do simulate user behavior on browser like selection 
  - driver_utils: Util functions for driver operations
  - soup_utils: Util functions for operation on soup
  - utils: General util functions 

