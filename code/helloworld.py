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
  fn = confRoot + os.sep + 'conf' + os.sep + 'default.json'
 else:
  print('Environment is not set correctly')
  sys.exit(1)

 f = open(fn)

 conf = json.load(f)
 key = conf.get('key')
 user = conf.get('user')
 token = conf.get('token')

 trello = TrelloApi(key, token)

 me = trello.members.get(user)
 print("Full name: " + me.get('fullName'))
 print("Boards: " + str(me.get('idBoards')))
 print("Organizations: " + str(me.get('idOrganizations')))

 s = json.dumps(me, indent=4, sort_keys=True)
 print(s)


if __name__ == '__main__':
 import sys
 main(sys.argv)

## EOF ##
