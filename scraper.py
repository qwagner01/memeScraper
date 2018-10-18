from bs4 import BeautifulSoup
import requests
# wvNg1MtuMnscZb_7XM_OkiEPmro
import praw

reddit = praw.Reddit(client_id='hI4Fwgeo1ghtMA', client_secret='wvNg1MtuMnscZb_7XM_OkiEPmro', user_agent='memeScraper')
the_memes = []

subreddits = [
    "dankmemes",
    "PrequelMemes",
    "blackpeopletwitter",
    "BikiniBottomTwitter",
    "wholesomememes",
    "Me_irl",
    "AdviceAnimals",
    "memes"
]
url = "http://new.reddit.com/r/"
headers = {'Accept-Encoding': 'identity'}
# content = [requests.get(url + r, headers=headers) for r in subreddits]
# soup = [BeautifulSoup(h.text, features="html5lib") for h in content]
# print(soup)

def getMemes(subreddit):
    html = requests.get(url+subreddit, headers=headers)
    soup = BeautifulSoup(html.content, features="html5lib")
    memes = []
    for img in soup.findAll('img'):
        memes.extend(img['src'])
        print(img['src'])
    # print(memes)
    if len(memes) == 0:
        print(soup)
getMemes(subreddits[1])
