from .api import Myob  # noqa

VERSION = (1, 2, 19, 'olaunch', 2)

__version__ = '.'.join(str(x) for x in VERSION[:(2 if VERSION[2] == 0 else 3)])  # noqa
