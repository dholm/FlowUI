VERSION = (0, 3, 0, 'dev')
__version__ = ''.join(['-.' [type(x) == int] + str(x) for x in VERSION])[1:]
