#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: config.py
# Project: SloppyV4
# Created Date: 2024-07-15, 01:33:54
# Author: Chungman Kim(h2noda@unipark.kr)
# Last Modified: Mon Jul 15 2024
# Modified By: Chungman Kim
# Copyright (c) 2024 Unipark
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
'''

from configparser import ConfigParser

class Config:
    """Class : Config
    """
    def __init__(self, cfg_file="config.ini"):
        self.cfg_file = cfg_file
        self.cfg_data = ConfigParser()
        self.cfg_data.read(cfg_file, encoding="utf-8")

    def write_config(self):
        """ Config : Write Config file ( config.ini )
        """
        with open(self.cfg_file, "w", encoding="utf-8") as self.cfg_file:
            self.cfg_data.write(self.cfg_file)

    def find_data(self, section, key):
        """ Config : Find data in config file

        Args:
            section (str): _description_
            key (str): _description_

        Returns:
            _type_: _description_
        """
        retval = self.cfg_data[section][key]
        return retval
