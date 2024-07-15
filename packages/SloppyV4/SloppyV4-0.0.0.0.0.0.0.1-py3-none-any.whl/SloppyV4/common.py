#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: common.py
# Project: SloppyV4
# Created Date: 2024-07-15, 10:56:37
# Author: Chungman Kim(h2noda@unipark.kr)
# Last Modified: Mon Jul 15 2024
# Modified By: Chungman Kim
# Copyright (c) 2024 Unipark
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
'''

from datetime import date, timedelta, datetime
from dateutil import relativedelta


class Datetime:
    """ Class - DateTime"""
    def __init__(self):
        pass

    def get_today(self, strformat="%Y%m%d"):
        """ DateTime : Get Today ( yyyymmdd )

        Args:
            strformat (str, optional): _description_. Defaults to "%Y%m%d".

        Returns:
            _type_: _description_
        """
        retval = date.today().strftime(strformat)

        return retval

    def get_now(self, strformat="%Y-%m-%d %H:%M:%S"):
        """ DateTime : Get Now ( yyyy-mm-dd HH-MM-SS )

        Args:
            strformat (str, optional): _description_. Defaults to "%Y-%m-%d %H:%M:%S".

        Returns:
            _type_: _description_
        """
        retval = datetime.now().strftime(strformat)

        return retval

    def get_thismonth(self, strformat="%Y%m"):
        """지정된 형식으로 현재 년월을 리턴

        Args:
            strformat (str, optional): _description_. Defaults to "%Y%m".

        Returns:
            _type_: _description_
        """
        retval = date.today().strftime(strformat)

        return retval

    def get_yesterday(self, strformat="%Y%m%d"):
        """지정된 형식으로 전일을 리턴

        Args:
            strformat (str, optional): _description_. Defaults to "%Y%m".

        Returns:
            _type_: _description_
        """
        retval = date.today() - timedelta(1)
        retval = retval.strftime(strformat)

        return retval

    def get_previousmonth(self, strformat="%Y%m"):
        """지정된 형식으로 전월을 리턴

        Args:
            strformat (str, optional): _description_. Defaults to "%Y%m".

        Returns:
            _type_: _description_
        """
        retval = datetime.today() + relativedelta.relativedelta(months=-1)
        retval = retval.strftime(strformat)

        return retval
