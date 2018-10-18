import praw
import config
import random
from skimage import io
# import keyboard

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
    random.shuffle(memes)
    return memes

def displayMeme(url):
    io.imshow(io.imread(url))
    io.show()

memes = getMemes(subreddits)
print(memes)
# while True:
#     try: #used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed(' '):#if key 'q' is pressed
#             num = random.randint(0,len(memes))
#             displayMeme(memes[num])
#             break#finishing the loop
#         else:
#             pass
#     except:
#         break #if user pressed a key other than the given key the loop will break
num = input("How many memes? ")
for n in range(num):
    displayMeme(memes[n])
