import copy
import os

from wox import Wox, WoxAPI


RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': '',
    'IcoPath': 'Images/favicon.png',
}

ACTION_TEMPLATE = {
    'JsonRPCAction': {
        'method': '',
        'parameters': [],
    }
}


class Main(Wox):

    def query(self, param):
        """Wox dealing programm

        Arguments:
            param {str} -- Wox window key in parameter

        Returns:
            list -- Wox json list
        """

        result = []
        param = param.strip().lower()

        if param:
            if param in ('lock', 'lockscreen'):
                p = os.path.join(RAW_PATH, 'Lockscreen')
                result.extend(self.collect(p))

            elif param in ('desk', 'desktop'):
                p = os.path.join(RAW_PATH, 'Wallpaper')
                result.extend(self.collect(p))

            else:
                title = "Try to key in right command."
                subtitle = "Such as 'lock' or 'desk', try again."
                result.append(self.genformat(title, subtitle))
        else:
            title = "Auto collect your desktop wallpaper."
            subtitle = "For desktop wallpaper key in 'desk', for lock screen wallpaper key in 'lock'"
            result.append(self.genformat(title, subtitle))

        return result


if __name__ == '__main__':
    Main()
