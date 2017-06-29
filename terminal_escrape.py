import requests
from bs4 import BeautifulSoup

base_url = 'http://terminalescape.blogspot.com/'
years = ['2015', '2016']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
beginYear = 2013
beginMonth = 5
endYear = 2017
endMonth = 6

dates = []
for year in range(2013, 2017+1):
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
