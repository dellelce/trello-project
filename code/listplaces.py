
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
  _body = body.splitlines()
  newbody = []
  state = 0
  changes = 0

  for line in _body:

   if state == 0:
    if 'Unsubscribe from this Google Alert:' in line:
     state = 1
     changes += 1
     continue

    if 'Create another Google Alert:' in line:
     state = 1
     changes += 1
     continue

    if 'Sign in to manage your alerts:' in line:
     state = 1
     changes += 1
     continue

    # keep all other lines (google urls to be modified though...)
    newbody.append(line)

   if state == 1:
    # empty lines = change of state
    if line == '':
     state = 0

    # all other lines are just!
    changes += 1

  return (changes, '\n'.join(newbody))


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

def process_cards(trello, list_id):

 for i in list_id:
   title = i['name']
   id_card = i['id']
   create_time = datetime.fromtimestamp(int(id_card[0:8],16))

   # only Google Alert cards are managed by this code
   if 'Google Alert' not in title:
     continue

   print("{} || {} || {}".format(id_card, create_time, title))

   newtime = mytimeformat(create_time)

   if newtime not in title:
     title = '{} {}'.format(title, newtime)
     print('New title: ' + title)

     up = trello.cards.update(id_card, name=title)

   body = i['desc']
   lchanges = 0

   lchanges, newbody = check_body(body)

   if lchanges != 0:
     print('Updating description to commit {} changes'.format(lchanges));
     up = trello.cards.update(id_card, desc=newbody)

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
 process_cards(trello, email_cards)


#
if __name__ == '__main__':
 import sys
 main(sys.argv)

## EOF ##
