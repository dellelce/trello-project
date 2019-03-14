"""
Clean up tool for all Google Alerts cards

File:         googlealerts.py
Created:      210918
"""

import os
import json
'''
https://help.trello.com/article/759-getting-the-time-a-card-or-board-was-created
'''
from datetime import datetime

from trello import TrelloApi


def mytimeformat(ds):
  '''Format datetime in "my standard format"'''
  return '{:0>2}{:0>2}{}'.format(ds.day, ds.month, str(ds.year)[2:4])


def trello_auth():
 """Collect trello auth details & configuration"""

 confRoot = os.environ.get('TRELLO', None)

 if confRoot is not None:
  fn = confRoot + os.sep + 'conf' + os.sep + 'default.json'
 else:
  print('Environment is not set correctly')
  return None

 with open(fn) as f:
  conf = json.load(f)
  key = conf['key']
  user = conf['user']
  token = conf['token']

 return (key, user, token)


def read_cards(trello, list_id):
 """Cards for given list.
    TODO: return dictionary
          pass filter as a function/callable
 """

 for i in list_id:
   title = i['name']
   id_card = i['id']
   create_time = datetime.fromtimestamp(int(id_card[0:8], 16))

   # only Google Alert cards are managed by this code
   if 'Google Alert' not in title:
     continue

   newtime = mytimeformat(create_time)
   body = i['desc']
   body_a = body.splitlines()

   for line in body_a:
     if '://' in line:
       print ('{} {}'.format(newtime, line))


# main function
def main(args):
 """This is main!"""
 try:
   key, user, token = trello_auth()
 except:
   return 1

 trello = TrelloApi(key, token)
 me = trello.members.get(user)
 user_id = me.get('id')
 boards = trello.members.get_board(user_id)

 for board in boards:
   board_id = board['id']

   trello_list = trello.boards.get_list(board_id)

   for tl_item in trello_list:
     if 'email' in tl_item['name']:
       read_cards(trello, trello.lists.get_card(tl_item['id']))


#
if __name__ == '__main__':
  import sys
  main(sys.argv)

## EOF ##
