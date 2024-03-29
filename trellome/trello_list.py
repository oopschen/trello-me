#!/usr/bin/env python3

import requests as rts
import logging as lg
import re

from trellome.util import chain_or
from trellome.util import regex_match_with_prop
from . import settings as ss

def get_card(list_id, name_filter:str =None):
  turl, tkey, ttoken = ss.mget("TRELLO_PREFIX_URL", "TRELLO_KEY", "TRELLO_TOKEN")
  res = rts.get(f'{turl}/1/lists/{list_id}/cards?key={tkey}&token={ttoken}')

  if 200 != res.status_code:
    lg.error(f'get_card: list_id={list_id}, filter={name_filter}', res.content)
    raise Exception(f'get_card: list_id={list_id}, filter={name_filter}')

  if None == name_filter:
    return res.json()

  rgx = re.compile(name_filter, re.X | re.M | re.S)

  return [
    item for item in res.json()
    if chain_or(
        regex_match_with_prop("name", rgx, item),
        regex_match_with_prop("id", rgx, item),
        regex_match_with_prop("desc", rgx, item),
        regex_match_with_prop("address", rgx, item),
        )
  ]

