import os
import random
from mastodon import Mastodon


def tooter():
    try:
        # Read toots from file
        with open('output.txt', 'r') as infile:
            toots = infile.readlines()
        
        # Handle empty file
        if not toots:
            print("No toots found in output.txt")
            return
        
        # Remove empty lines and strip whitespace
        toots = [t.strip() for t in toots if t.strip()]
        
        # Handle case where all lines are empty
        if not toots:
            print("No valid toots found in output.txt")
            return
            
        # Connect to Mastodon
        mastodon = Mastodon(
            access_token=os.environ['PYTOOTERUSERCREDSECRET'],
            api_base_url='https://mastodon.ocert.at'
        )
        
        # Pick random toot and post it
        random_toot = random.randrange(0, len(toots))
        toot = toots[random_toot]
        
        if len(toot) <= 500:
            print(f"Posting: {toot}")
            mastodon.toot(toot)
            print("Toot posted successfully!")
        else:
            print(f"Skipping too long toot (length: {len(toot)}): {toot[:100]}...")
            
    except FileNotFoundError:
        print("Error: output.txt file not found")
    except KeyError:
        print("Error: PYTOOTERUSERCREDSECRET environment variable not set")
    except Exception as e:
        print(f"Error posting toot: {e}")


if __name__ == '__main__':
    tooter()
