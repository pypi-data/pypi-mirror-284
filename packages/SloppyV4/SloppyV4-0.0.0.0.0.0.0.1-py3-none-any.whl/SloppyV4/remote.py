#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# File: remote.py
# Project: SloppyV4
# Created Date: 2024-07-15, 01:51:17
# Author: Chungman Kim(h2noda@unipark.kr)
# Last Modified: Mon Jul 15 2024
# Modified By: Chungman Kim
# Copyright (c) 2024 Unipark
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
'''

import paramiko

from message import Msg
from error import RemoteCommandError


class Remote:
    """ Class : Remote
    """
    # def __init__(self):
    #     """ Remote : __init__
    #     """
    #     pass

    def ssh_command(self, p_id, p_pw, p_remote, p_cmd):
        """Excute - SSH Command 

        Args:
            p_id (String): User id
            p_pw (String): User Password
            p_remote (String): Remoter Server Hostname OR IP
            p_cmd (String): Command
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(hostname=p_remote, port=22,
                        username=p_id, password=p_pw)

            Msg.printmsg("Connected Remote Server(ID : " +
                         p_id, 1, "-", "red", True)

            (stdin, stdout, stderr) = ssh.exec_command(p_cmd)
            #output = stdout.readlines()
            return stdin, stdout, stderr

        except RemoteCommandError as err:
            print(err)
        finally:
            ssh.close()
