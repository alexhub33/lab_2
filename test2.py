#!/usr/bin/python
import requests
from urllib.request import urlopen       #grab the page
from bs4 import BeautifulSoup            #parse the text
import csv
import numpy as np 
from time import sleep
from random import randint

file_name = "yelp_reviews_new.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))
 # write a new row as a header
f.writerow(['Name', 'Location', 'Reviews'])


source=requests.get("https://www.yelp.com/biz/bar-karaoke-lounge-toronto")

# url_to_scrape = "https://www.yelp.com/biz/bar-karaoke-lounge-toronto"
#url_to_scrape.raise_for_status()

print(source)

soup = BeautifulSoup(source.text, 'html.parser')
# print(soup)

reviews=soup.find(class_="css-79elbk border-color--default__373c0__2oFDT")



my_review=reviews.find_all('li' ,class_="margin-b5__373c0__2ErL8 border-color--default__373c0__2oFDT") #li we will only get 10 classes not the additional empty class for the whole group
# print(my_review)
print(len(my_review))



# for reviews in my_review:
#     people_name=reviews.find('span', class_="fs-block css-m6anxm").get_text()  #span define because the name was in a span class
#     people_location=reviews.find('span', class_="css-n6i4z7").get_text()
#     people_reviews=reviews.find('span',class_="raw__373c0__3rcx7").get_text()
#     # print(people_name)
#     # print(people_location)
#     # print((people_reviews))
#     f.writerow([people_name,people_location, people_reviews])


#iterate all pages through webscaper + store into the csv file
#https://www.yelp.com/biz/bar-karaoke-lounge-toronto?start=30   #goes up by 10.

pages = np.arange(0,80,10) # 1 to 80 with a step of 10  (start, stop, step)



for page in pages: 
    page = requests.get("https://www.yelp.com/biz/bar-karaoke-lounge-toronto?start="+str(page)+"")
    soup = BeautifulSoup(source.text, 'html.parser')
    my_review=reviews.find_all('li' ,class_="margin-b5__373c0__2ErL8 border-color--default__373c0__2oFDT") #li we will only get 10 classes not the additional empty class for the whole group
    people_name=reviews.find('span', class_="fs-block css-m6anxm").get_text()  #span define because the name was in a span class
    people_location=reviews.find('span', class_="css-n6i4z7").get_text()
    people_reviews=reviews.find('span',class_="raw__373c0__3rcx7").get_text()
    # sleep(randint(2,8))  #this will prevent the loop from bombarding the website, good for large requests.  Not really necessary here. pass a request every 2 to 8 seconds.
    f.writerow([people_name,people_location, people_reviews])