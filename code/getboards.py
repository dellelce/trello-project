#!/usr/bin/env python3

'''
 File:         helloworld.py
 Created:      181016
 Description:  
'''

from trello import TrelloApi
import os
import json

#
# main function
#

def main(args):
 confRoot=os.environ.get('TRELLO', None)

 if confRoot is not None:
  fn = confRoot + os.sep + 'keys' + os.sep + 'default.json'
 else:
  print('Environment is not set correctly')
  sys.exit(1)

 f = open(fn)
 conf = json.load(f)
 key = conf['key']
 user = conf['user']

 trello = TrelloApi(key)

 me = trello.members.get(user)

 id = me.get('id')
 b = trello.members.get_board(id) 

 s = json.dumps(b, indent=4, sort_keys=True)
 print(s)

 


if __name__ == '__main__':
 import sys
 main(sys.argv)

## EOF ##
