#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: message.py
# Project: SloppyV4
# Created Date: 2024-07-08, 06:11:05
# Author: Chungman Kim(h2noda@unipark.kr)
# Last Modified: Mon Jul 15 2024
# Modified By: Chungman Kim
# Copyright (c) 2024 Unipark
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
'''

from rich.console   import Console
from rich.table     import Table


class Msg:
    """" Class : Rich Message """
    def __init__(self):
        self.cs = Console()
        self.table = Table()

    def blank(self):
        """ Msg - Blank line insert
        """
        self.cs.print()

    def copyright(self):
        """ Msg - Copytight """
        self.printmsg(
            "Copyright 2022. Unipark. All right reserved.", 
            color="yellow", bold=True)

    def style_tag(self, color, bold=False):
        """ Msg - Style Tag

        Args:
            color (str): _description_
            bold (bool, optional): _description_. Defaults to False.

        Returns:
            str: _description_
        """
        if bold:
            retval = "bold " + color
        else:
            retval = color
        return retval

    def prefix(self, indent_char="-", indent=0):
        """ Msg - Prifix

        Args:
            indent_char (str, optional): _description_. Defaults to "-".
            indent (int, optional): _description_. Defaults to 0.

        Returns:
            String: _description_
        """
        if indent == 0:
            retval = ""
        else:
            retval = "  " * indent + indent_char + " "
        return retval

    # def printmsg(self, val, indent_char="-", indent=0, color="white", bold=False, end="\n"):
    def printmsg(self, val, indent_char="-", indent=0, color="white", bold=False):
        """ Msg - Print message

        Args:
            val (str): _description_
            indent_char (str, optional): _description_. Defaults to "-".
            indent (int, optional): _description_. Defaults to 0.
            color (str, optional): _description_. Defaults to "white".
            bold (bool, optional): _description_. Defaults to False.
        """
        retstyle = self.style_tag(color, bold)
        retval = self.prefix(indent_char, indent) + \
            "[" + retstyle + "]" + val + "[/" + retstyle + "]"

        self.cs.print(retval, style="white")
