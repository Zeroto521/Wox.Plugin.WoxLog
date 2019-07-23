# -*- coding: utf-8 -*-

import time

from wox import Wox, WoxAPI

from .constants import *


class Main(Wox):

    def query(self, param):
        """Wox dealing programm

        Arguments:
            param {str} -- Wox window key in parameter

        Returns:
            list -- Wox json list
        """

        param = param.strip()
        message = "{}, {}\n"
        with open(logFilePath, 'a+', encoding='utf-8') as f:
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            message = message.format(date, param)
            f.write(message)
