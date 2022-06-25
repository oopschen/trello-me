#!/usr/bin/env python3

__vars={}

def set(key, value):
  __vars[key] = value

def get(key):
  if key in __vars:
    return __vars[key]

def mget(*args):
  if 1 > len(args):
    return None

  res = []
  for x in args:
    res.append(get(x))

  return res

set("TRELLO_PREFIX_URL", "https://api.trello.com")
