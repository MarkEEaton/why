import os
import random
from mastodon import Mastodon

sec = os.environ['WHY_USERCRED_SECRET']

# Create actual API instance
mastodon = Mastodon(
    access_token = sec,
    api_base_url = 'https://mastodon.ocert.at'
)

with open('output.txt', 'r') as infile:
    toots = infile.readlines()

random_toot = random.randrange(0, len(toots) - 1)

print(toots[random_toot])
mastodon.toot(toots[random_toot])
