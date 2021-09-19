import subprocess
import os
import sys
import getopt
from utils import utils


def main():
    filename = "project.xml"
    path = ""
    rar = "C:\Program Files\WinRAR\WinRAR.exe"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hp:r:",["path=", "winrar="])
    except getopt.GetoptError:
        print('-p <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-p <path> path -r <winrar> winrar binary path eg. C:\Program Files\WinRAR\WinRAR.exe')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-r", "--winrar"):
            rar = arg
    os.chdir(path)
    print(path)
    current = os.path.abspath(os.getcwd())
    print(current)
    mapping = utils.GetModsName(filename, current)
    for name in mapping:
        obj = mapping[name]
        name = str(obj["name"]).replace('.\\', '') + ".zip"
        print("pack mod from {dir} to {name}".format(dir=obj["path"], name=name))
        os.chdir(obj["path"])
        print(os.path.abspath(os.getcwd()))
        print(name)
        subprocess.run([rar, "a", name, "*/*", "*"])
        os.chdir(current)
        print(os.path.abspath(os.getcwd()))

if __name__ == '__main__':
    main()