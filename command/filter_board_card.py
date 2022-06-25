#!/usr/bin/env python3

import click as ck

from trellome import board as bd
from trellome import member as mb
from trellome import trello_list as tlist

from . import setup as st

@ck.command()
@ck.option('-t', '--token', required=True, help='Trello api token.')
@ck.option('-k', '--key', required=True, help='Trello api key.')
@ck.option('-n', '--name', help='Board list name regex.')
@ck.option('-f', '--list-filter', help='Board List filter.', default="closed",
   type=ck.Choice(['all', 'closed', 'none', 'open'], case_sensitive=False))
@ck.argument('board_name')
def filter_board_list(board_name, token, key, name, list_filter):
  st.global_setup(key, token)

  boards = mb.get_boards("me", board_name)
  if None == boards:
    print("No boards found")
    return

  for board in boards:
    trello_list = bd.get_boards_list(board["id"], list_filter, name)

    board_id = board["id"]
    board_name = board["name"]
    print(f"---- Start Board '{board_name}({board_id})' List -----")
    __print_trello_list(trello_list)
    print(f"---- End Board '{board_name}({board_id})' List -----")


def __print_trello_list(trello_list):
  if None == trello_list:
    print("No trello list found.")
    return

  for idx, val in enumerate(trello_list):
    print(f"No.{idx+1}\t(id,name)\t({val['id']} {val['name']})")

@ck.command()
@ck.option('-t', '--token', required=True, help='Trello api token.')
@ck.option('-k', '--key', required=True, help='Trello api key.')
@ck.option('-ln', '--list-name', help='Board list name regex.')
@ck.option('-n', '--name', help='Board card name regex.')
@ck.option('-f', '--list-filter', help='Board List filter.', default="closed",
   type=ck.Choice(['all', 'closed', 'none', 'open'], case_sensitive=False))
@ck.argument('board_name')
def filter_board_card(board_name, token, key, list_name, name, list_filter):
  st.global_setup(key, token)

  boards = mb.get_boards("me", board_name)
  if None == boards:
    print("No boards found")
    return

  for board in boards:
    trello_list = bd.get_boards_list(board["id"], list_filter, list_name)

    board_id = board["id"]
    board_name = board["name"]

    print(f"---- Start Board '{board_name}({board_id})' List -----")

    for idx, val in enumerate(trello_list):
      list_id = val["id"]
      list_name = val["name"]
      print(f"------ No.{idx+1} List '{list_name}({list_id})' List -------")
      card_list = tlist.get_card(list_id, name)
      __print_trello_card(card_list)
      print(f"------ End List '{list_name}({list_id})' List -------\n")

    print(f"---- End Board '{board_name}({board_id})' List -----")

def __print_trello_card(trello_card):
  if None == trello_card:
    print("No trello card found.")
    return

  for idx, val in enumerate(trello_card):
    print(f"""No.{idx+1}\t(id,name,desc,shortUrl,address)\t({val['id']} {val['name']} {val['desc']}
        {val['shortUrl']} {"address" in val and val['address']})""")

