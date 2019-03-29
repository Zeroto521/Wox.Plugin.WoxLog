import copy
import os

from wox import Wox, WoxAPI


RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': '',
    'IcoPath': 'Images/favicon.png',
}


class Main(Wox):

    def query(self, param):
        """Wox dealing programm

        Arguments:
            param {str} -- Wox window key in parameter

        Returns:
            list -- Wox json list
        """

        param = param.strip()
        result = []

        return result


if __name__ == '__main__':
    Main()
