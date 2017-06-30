# run this in cmd line python terminal_escrape.py 2014 5 2017 6

import sys # so we can access cmd line args
import requests
from bs4 import BeautifulSoup

# print cmd line arguments - it's a list
print(sys.argv)
# sys.argv[0] is the name of the script and sys.argv[1], sys.argv[2], ... sys.argv[n] get the args
beginYear = int(sys.argv[1])
beginMonth = int(sys.argv[2])
endYear = int(sys.argv[3])
endMonth = int(sys.argv[4])

base_url = 'http://terminalescape.blogspot.com/'
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

dates = []
for year in range(beginYear, endYear+1):
    for month in range(1,12+1):
        if year == beginYear and month < beginMonth:
            pass
        elif year == endYear and month > endMonth:
            pass 
        else: 
            dates.append([str(year), months[month-1]])

urls = []
for post in dates:
        url = base_url + post[0] + '/' + post[1]
        urls.append(url)

links = []
for url in urls:
    print (url)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    a_tag_matches = soup.select('h3.post-title.entry-title > a[href]')
    links += [a['href'] for a in a_tag_matches]

print (links)
