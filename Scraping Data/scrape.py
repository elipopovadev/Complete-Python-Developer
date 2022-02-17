import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')

res_page2 = requests.get("https://news.ycombinator.com/news?p=2")
soup2 = BeautifulSoup(res_page2.text, 'html.parser')

links = soup.select('.titlelink')
subtext = soup.select('.subtext')

links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sorted_function(hn_list):
    return sorted(hn_list, key=lambda x: -x['points'])


def create_custom_hn(links, subtext):
    hn_list = []

    for index, item in enumerate(links):
        title = item.getText()
        link = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 100:
                hn_list.append(
                    {'title': title, 'link': link, 'points': points})
    return sorted_function(hn_list)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
