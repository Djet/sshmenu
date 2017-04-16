#!/usr/bin/env python
# -*- coding: utf-8 -*-
from raven import Client
from time import sleep

import curses, os
import json
import logging
client = Client('http://413c6240283b405e8bb356b7fa94bfed:336e485eed974c45a51808f3e7e638a0@str.blaq.ru/6')
try:
    logging.basicConfig(format=u'[%(asctime)s] %(levelname)-8s %(message)s', level=logging.DEBUG, filename=u'sshmenu.log')
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad(1)
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_GREEN)
    h = curses.color_pair(1)
    n = curses.A_NORMAL


    with open('sshmenu.json') as data_file:
        menu_data = json.load(data_file)



    logging.debug(menu_data['title'])

    def runmenu(menu_data, parent):
      if parent is None:
        lastoption = "Exit"
      else:
        lastoption = "Return to %s menu" % parent['title']

      optioncount = len(menu_data['options'])
      pos=0
      oldpos=None
      x = None

      while x != ord('\n'):
        if pos != oldpos:
          oldpos = pos
          screen.border(1,1,1,1)
          screen.addstr(2, 2, menu_data['title'], curses.A_STANDOUT)
          screen.addstr(4, 2, menu_data['subtitle'], curses.A_BOLD)

          for index in range(optioncount):
            textstyle = n
            if pos == index:
              textstyle = h
            screen.addstr(7 + index, 4, "%d - %s" % (index + 1, menu_data['options'][index]['title']), textstyle)
          textstyle = n
          if pos == optioncount:
            textstyle = h
          screen.addstr(7+optioncount,4, "%d - %s" % (optioncount+1, lastoption), textstyle)
          screen.refresh()

        x = screen.getch()

        if x >= ord('1') and x <= ord(str(optioncount+1)):
          pos = x - ord('0') - 1
        elif x == 258:
          if pos < optioncount:
            pos += 1
          else: pos = 0
        elif x == 259:
          if pos > 0:
            pos += -1
          else: pos = optioncount

      return pos

    def processmenu(menu_data, parent = None):
      optioncount = len(menu_data['options'])
      exitmenu = False

      while not exitmenu:
        getin = runmenu(menu_data, parent)

        if getin == optioncount:
            exitmenu = True
        elif menu_data['options'][getin]['type'] == "command":
          curses.def_prog_mode()
          os.system('reset')
          screen.clear()
          os.system(menu_data['options'][getin]['command'])
          screen.clear()
          curses.reset_prog_mode()
          curses.curs_set(1)
          curses.curs_set(0)
        elif menu_data['options'][getin]['type'] == "menu":
              screen.clear()
              processmenu(menu_data['options'][getin], menu_data)
              screen.clear()
        elif menu_data['options'][getin]['type'] == "exitmenu":
              exitmenu = True

    processmenu(menu_data)
    curses.endwin()
    os.system('clear')
except BaseException:
    client.captureException()
