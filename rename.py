import os
import sys
import getopt
from utils import utils


def main():
    filename = "project.xml"
    path = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hp:",["path="])
    except getopt.GetoptError:
        print('-p <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg

    mapping = utils.GetModsName(filename, path)
    for name in mapping:
        obj = mapping[name]
        print("rename {dir} to {name}".format(dir=obj["path"], name=obj["name"]))
        os.rename(obj["path"], obj["name"])

if __name__ == '__main__':
    main()