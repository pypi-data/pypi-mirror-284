import sys
import Listener


class Xray():
    print("RUNNING PYTHON VERSION = " + sys.version)
    ROBOT_LIBRARY_LISTENER = Listener()
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
# sys.path.append(