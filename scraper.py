import praw
import config
from random import shuffle
import os

r = praw.Reddit(client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password)

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

def getMemes(subreddits):
    links = []
    for subreddit in subreddits:
        for submission in r.subreddit(subreddit).hot(limit=10):
            links.append(str(submission.url))
    memes = filter(lambda k: 'i.redd.it' in k, links)
    shuffle(memes)
    return memes


memes = getMemes(subreddits)
print(memes)

num = input("How many Memes? ")
for i in range(num):
    os.system("open " + memes[i])
