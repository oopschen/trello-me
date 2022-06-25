#!/usr/bin/env python3

import click as ck

from trellome import board as bd
from trellome import member as mb

from . import setup as st

@ck.command()
@ck.option('-t', '--token', required=True, help='Trello api token.')
@ck.option('-k', '--key', required=True, help='Trello api key.')
@ck.option('-n', '--name', help='Board list name regex.')
@ck.argument('board_name')
def filter_archived_board_list(board_name, token, key, name):
  st.global_setup(key, token)

  boards = mb.get_boards("me", board_name)
  if None == boards:
    print("No boards found")
    return

  for board in boards:
    trello_list = bd.get_boards_list(board["id"], "closed", name)

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
