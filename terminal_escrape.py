import argparse
import requests
from bs4 import BeautifulSoup
import urllib
import re
import os

def downloadIt(url, path):
    print('downloading: ' + url)
    data = urllib.request.urlretrieve(url, path)
    print('saved to: ' + path)

month_choices = ("01","02","03","04","05","06","07","08","09","10","11","12")

parser = argparse.ArgumentParser()
parser.add_argument("b_y", type = int, choices = [2014, 2015, 2016, 2017], help = "Year to begin search")
parser.add_argument("b_m", type = str, choices = month_choices, help = "Month to begin search")
parser.add_argument("e_y", type = int, choices =  [2014, 2015, 2016, 2017], help = "Year to end search")
parser.add_argument("e_m", type = str, choices = month_choices, help = "Month to end search")

args = parser.parse_args()

base_url = "http://terminalescape.blogspot.com/"
pwd = os.getcwd()
print ("Working Directory: " + pwd)

dates = []
for year in range(args.b_y, args.e_y+1):
    for month in month_choices:
        if year == args.b_y and month < args.b_m:
            pass
        elif year == args.e_y and month > args.e_m:
            pass
        else:
            dates.append([str(year), month])

urls = []
for post in dates:
        url =  base_url + post[0] + '/' + post[1]
        urls.append(url)

print('\ngetting links to blog posts...')
links = []
for url in urls:
    print (url)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    a_tag_matches = soup.select('h3.post-title.entry-title > a[href]')
    links += [a['href'] for a in a_tag_matches]

print('\nscraping blog posts...')
for link in links:
    print (link)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    dl_links = soup.select('div.post-body.entry-content > div.separator > a[href*=/od.lk/f/]')
    if len(dl_links) > 0:
        dl_link = dl_links[0]['href']
        zip_link = dl_link.replace('/f/', '/download/') + '?'
        path = pwd + '/' + re.search(r'/[0-9][0-9]/(.+)\.html', link).group(1)
        downloadIt(zip_link, path)

print (links)
