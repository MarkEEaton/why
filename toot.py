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
            raise Exception("No toots found in output.txt")
        
        # Remove empty lines and strip whitespace
        toots = [t.strip() for t in toots if t.strip()]
        
        # Handle case where all lines are empty
        if not toots:
            print("No valid toots found in output.txt")
            raise Exception("No valid toots found in output.txt")
            
        # Connect to Mastodon
        mastodon = Mastodon(
            access_token=os.environ['PYTOOTERUSERCREDSECRET'],
            api_base_url='https://mastodon.ocert.at'
        )
        
        max_attempts = 10  # Maximum number of retries
        attempts = 0
        
        while attempts < max_attempts:
            # Pick random toot
            random_toot = random.randrange(0, len(toots))
            toot = toots[random_toot]
            
            if len(toot) <= 500:
                print(f"Posting: {toot}")
                mastodon.toot(toot)
                print("Toot posted successfully!")
                return
            else:
                print(f"Skipping too long toot (length: {len(toot)}): {toot[:100]}...")
                attempts += 1
        
        print(f"Failed to find a suitable toot after {max_attempts} attempts")
        raise Exception(f"Failed to find a suitable toot after {max_attempts} attempts")
            
    except FileNotFoundError:
        print("Error: output.txt file not found")
        raise Exception("output.txt file not found")
    except KeyError:
        print("Error: PYTOOTERUSERCREDSECRET environment variable not set")
        raise Exception("PYTOOTERUSERCREDSECRET environment variable not set")
    except Exception as e:
        print(f"Error posting toot: {e}")
        raise  # Re-raise the exception to ensure GitHub Actions detects it


if __name__ == '__main__':
    tooter()
