import tweepy
import keys

auth = tweepy.OAuthHandler(*keys.tokens['APP'])
auth.set_access_token(*keys.tokens['SwagMoneyBot'])

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="Fierce_NE").pages():
    ids.extend(page)

print ids