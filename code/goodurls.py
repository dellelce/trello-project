'''
 description for goodurls.py

 File:         goodurls.py
 Created:      220918
'''

from urllib.parse import unquote
import sqlite3

class domains(object):
  """Save those domains"""
  def __init__(self,name=None):
    pass

  def add(self, name):
    pass


def main(name):
  with open(name) as f:
    buf = f.read()
    lines = buf.splitlines()

  for line in lines:
    line_a = line.split()

    date = line_a[0]
    url = line_a[1]

    url_a = url.split('&')
    for url_slice in url_a:
      if 'url=http' not in url_slice: continue

      new_url = url_slice.replace("url=","")
      u_new_url = unquote(new_url)

      site = u_new_url.split('/')[2]

      print("{}".format(date))
      print("{}".format(new_url))
      print("-->{}".format(u_new_url))
      print("----->{}".format(site))

if __name__ == '__main__':
 file_name = 'all_urls.txt'
 main(file_name)

## EOF ##
