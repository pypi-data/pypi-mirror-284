import sys
from pprint import pprint

import openbrush.tilt

if __name__ == '__main__':
    path = " ".join(sys.argv[1:])
    try:
        tilt = openbrush.tilt.Tilt(path)
        pprint(tilt.metadata['CameraPaths'])
    except Exception as e:
        print("ERROR: %s" % e)
