#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: security.py
# Project: SloppyV4
# Created Date: 2024-07-15, 01:47:39
# Author: Chungman Kim(h2noda@unipark.kr)
# Last Modified: Mon Jul 15 2024
# Modified By: Chungman Kim
# Copyright (c) 2024 Unipark
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
'''

from cryptography.fernet import Fernet


class Security:
    """ Class : Security
    """
    def __init__(self):
        self.key = b'saaBmbqfWWEi8__MqR6Ly3nDUstkI8iLpDst9b0rkpM='
        self.f = Fernet(self.key)

    @property
    def key(self):
        """ Security : Key

        Returns:
            _type_: _description_
        """
        return self._key

    @key.setter
    def key(self, key):
        """ Security : Setter

        Args:
            key (_type_): _description_
        """
        self._key = key

    def encrypt_string(self, data, is_out_string=True):
        """ Security : Encrypt string
            바이트 형태이면 암호화, 아니면 인코딩 후  암호화 수행
            출력이 문자열이면 디코딩 후 리턴

        Args:
            data (_type_): _description_
            is_out_string (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        if isinstance(data, bytes):
            retval = self.f.encrypt(data)
        else:
            retval = self.f.encrypt(data.encode('utf-8'))
        if is_out_string is True:
            return retval.decode('utf-8')
        else:
            return retval

    def decrypt_string(self, data, is_out_string=True):
        """ Security : Decrypt string
            - 바이트 형태이면 즉시 복호화
            - 문자열이면 인코딩 후 복호화
            - retval이 문자열이며 디코딩 후 반환

        Args:
            data (_type_): _description_
            is_out_string (bool, optional): _description_. Defaults to True.
        Returns:
            _type_: _description_
        """
        if isinstance(data, bytes):
            retval = self.f.decrypt(data)
        else:
            retval = self.f.decrypt(data.encode('utf-8'))
        if is_out_string is True:
            return retval.decode('utf-8')
        else:
            return retval
