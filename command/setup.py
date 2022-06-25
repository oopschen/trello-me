#!/usr/bin/env python3

from trellome import settings as ss

def global_setup(trello_key, trello_token):
  ss.set("TRELLO_KEY", trello_key)
  ss.set("TRELLO_TOKEN", trello_token)

