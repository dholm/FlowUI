VERSION = (0, 2, 0)
__version__ = ''.join(['-.' [type(x) == int] + str(x) for x in VERSION])[1:]
