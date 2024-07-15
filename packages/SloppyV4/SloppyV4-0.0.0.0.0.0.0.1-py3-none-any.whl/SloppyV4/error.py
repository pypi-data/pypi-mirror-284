#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: error.py
# Project: SloppyV4
# Created Date: 2024-07-15, 01:43:11
# Author: Chungman Kim(h2noda@unipark.kr)
# Last Modified: Mon Jul 15 2024
# Modified By: Chungman Kim
# Copyright (c) 2024 Unipark
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
'''

class EmptyValueError(Exception):
    """ Class : Empty Value Error

    Args:
        Exception (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return self.value


class ConfirmPasswordError(Exception):
    """ Class : Confirm Password Error

    Args:
        Exception (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return self.value


class ParameterCountError(Exception):
    """ Class : Parameter Count Error

    Args:
        Exception (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return self.value

class RemoteCommandError(Exception):
    """ Class : Remote Command Error

    Args:
        Exception (_type_): _description_

    Returns:
        _type_: _description_
    """
    # 생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return self.value