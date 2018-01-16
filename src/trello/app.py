import requests
from pprint import pprint as pp
from trello import TrelloClient
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import os

client_key = os.environ['TRELLO_KEY']
client_secret = os.environ['TRELLO_SECRET']
board = '4d5ea62fd76aa1136000000c'
uri = 'https://api.trello.com/1/board/{0}?key={1}'.format(board, client_key)

r = requests.get(uri).json()
pp(r)


#import bcrypt
#from getpass import getpass
#master_key = getpass('Enter Password:')
#salt = bcrypt.gensalt()
#combo_key = client_key + salt + master_key
#hashed_pass = bcrypt.hashpw(combo_key, salt)
#print(hashed_pass)

#oauth = OAuth1Session(client_key, client_secret=client_secret)
#request_token_url = 'https://trello.com/1/OAuthGetRequestToken'
#fr = oauth.fetch_request_token(request_token_url)

#print(fr)
#token = fr['oauth_token']
#token_secret = fr['oauth_token_secret']
# Token, secret - OK

#client = TrelloClient(
#    api_key=client_key,
#    api_secret=client_secret,
#    token=token,
#    token_secret=token_secret
#)
#print(client)
#boards = client.list_boards()
#print(boards)



