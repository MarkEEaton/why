import os
import random
from mastodon import Mastodon

app = Mastodon.create_app(
    'pytooterapp',
    api_base_url = 'https://mastodon.ocert.at',
)

mastodon = Mastodon(client_id = app[0],)
token = mastodon.log_in(
    os.environ['WHY_EMAIL'],
    os.environ['WHY_PWD'],
)

mastodon = Mastodon(access_token = token)


with open('output.txt', 'r') as infile:
    toots = infile.readlines()

random_toot = random.randrange(0, len(toots) - 1)

print(toots[random_toot])
mastodon.toot(toots[random_toot])
