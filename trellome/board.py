#!/usr/bin/env python3

import requests as rts
import logging as lg
import re

from trellome.util import chain_or
from trellome.util import regex_match_with_prop
from . import settings as ss

def get_boards_list(board_id: str, filter="all", list_name_filter: str=None):
  turl, tkey, ttoken = ss.mget("TRELLO_PREFIX_URL", "TRELLO_KEY", "TRELLO_TOKEN")
  res = rts.get(f'{turl}/1/boards/{board_id}/lists/{filter}?key={tkey}&token={ttoken}')
  if 200 != res.status_code:
    lg.error(f'boards_list: id={board_id}, filter={filter}', res.content)
    raise Exception(f'boards_list: id={board_id}, filter={filter}')

  if None == list_name_filter:
    return res.json()

  rgx = re.compile(list_name_filter, re.X | re.M | re.S)

  return [
    item for item in res.json()
    if chain_or(
        regex_match_with_prop("name", rgx, item),
        regex_match_with_prop("id", rgx, item),
        )
  ]

