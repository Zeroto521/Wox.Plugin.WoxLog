import os
import time

from wox import Wox, WoxAPI


PATH = '.'
fileName = os.path.join(PATH, '单词收藏.csv')


class Main(Wox):

    def query(self, param):
        """Wox dealing programm

        Arguments:
            param {str} -- Wox window key in parameter

        Returns:
            list -- Wox json list
        """

        result = []
        param = param.strip()
        message = "{}, {}\n"
        with open(fileName, 'a+', encoding='utf-8') as f:
            if os.path.exists(fileName):
                date = time.strftime("%Y-%m-%d %", time.localtime())
                message = message.format(ke, translation, date)
            else:
                message = message.format("query", "translation", "date")
            f.write(message)

        return result


if __name__ == '__main__':
    Main()
