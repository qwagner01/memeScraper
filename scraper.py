from bs4 import BeautifulSoup
import requests

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
    images = []
    for img in soup.findAll('img'):
        print(img)
    print(soup)

getMemes(subreddits[1])
