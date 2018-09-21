
"""
Test program to test api.

File:         getboards.py
Created:      181016
"""

from trello import TrelloApi
import os
import json
from pprint import pprint as p

'''
https://help.trello.com/article/759-getting-the-time-a-card-or-board-was-created
'''
from datetime import datetime

def mytimeformat(ds):
  '''format datetime in "my standard format"'''
  return '{:0>2}{:0>2}{}'.format(ds.day,ds.month,str(ds.year)[2:4])

def check_body(body):
  '''check if body needs reformatting'''
  return None

def trello_auth():
 confRoot = os.environ.get('TRELLO', None)

 if confRoot is not None:
  fn = confRoot + os.sep + 'conf' + os.sep + 'default.json'
 else:
  print('Environment is not set correctly')
  sys.exit(1)

 with open(fn) as f:
  conf = json.load(f)
  key = conf['key']
  user = conf['user']
  token = conf['token']

 return (key, user, token)


#
# main function
#
def main(args):
 """Does the main function need a docstring?!!?!"""

 key, user, token = trello_auth()
 trello = TrelloApi(key, token)
 #me = trello.members.get(user)
 #id = me.get('id')
 #b = trello.members.get_board(id)

 places_id ='5b73504305869468a980efe2'
 #places = trello.boards.get_list(places_id)

 places_email='5b73504cefcdbf883ec4bb94'

 email_cards = trello.lists.get_card(places_email)

 for i in email_cards:
  title = i['name']
  id_card = i['id']
  create_time = datetime.fromtimestamp(int(id_card[0:8],16))

  if 'Google Alert' not in title:
    continue

  print("{} || {} || {}".format(id_card, create_time, title)) 

  newtime = mytimeformat(create_time)

  if newtime not in title:
    title = '{} {}'.format(title, newtime)
    print('New title: ' + title)

    up = trello.cards.update(id_card, name=title)

'''
  if 'Google Alert' in title:
   body = i['desc']

   body_a = body.splitlines()
   p(body_a)
'''


#
if __name__ == '__main__':
 import sys
 main(sys.argv)

## EOF ##
