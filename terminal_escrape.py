import requests
from bs4 import BeautifulSoup

base_url = 'http://terminalescape.blogspot.com/'
years = ['2015', '2016']
months = ['01', '02', '03', '04', '05', '06', '07', '09', '10', '11', '12']

urls = []
for year in years:
    for month in months:
        url = base_url + year + '/' + month
        urls.append(url)

links = []
for url in urls:
    print url
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    a_tag_matches = soup.select('h3.post-title.entry-title > a[href]')
    links += [a['href'] for a in a_tag_matches]

print links
