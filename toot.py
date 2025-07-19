import os
import random
from mastodon import Mastodon


mastodon = Mastodon(access_token = os.environ['PYTOOTERUSERCREDSECRET'], api_base_url = 'https://mastodon.ocert.at')

with open('output.txt', 'r') as infile:
    toots = infile.readlines()

def tooter():
    random_toot = random.randrange(0, len(toots) - 1)
    toot = toots[random_toot]
    if len(toot) < 500:
        print(toot)
        mastodon.toot(toot)
    else:
        tooter()

tooter()
