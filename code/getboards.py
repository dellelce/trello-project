
"""
Test program to test api.

File:         getboards.py
Created:      181016
"""

from trello import TrelloApi
import os
import json


#
# main function
#
def main(args):
 """Does the main function need a docstring?!!?!"""
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

 trello = TrelloApi(key, token)

 me = trello.members.get(user)

 id = me.get('id')
 b = trello.members.get_board(id)

 print(type(b))
 '''s = json.dumps(b, indent=4, sort_keys=True)
 print(s)'''

 for i in b:
  print(i['id'] + ' || ' + i['name'])


#
if __name__ == '__main__':
 import sys
 main(sys.argv)

## EOF ##
