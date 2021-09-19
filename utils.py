from xmltodict import parse, unparse
import os
import sys
class utils(object):
    """description of class"""
    @staticmethod
    def GetModsName(filename, path):
        max_size = 1024*1024
        mapping = {}
        for _root, dirs, _files in os.walk(path):
          #print("  dir：", dirs)
          for dir in dirs: 
              for root, _dirs, files in os.walk(dir):
                #print("  files：", files)
                if filename in files:
                    print("  file found：", root)
                    file = root + "\\" + filename
                    with open(file, "r",encoding="utf-8") as reader:
                    
                        byte = reader.read(max_size)
                        xml_data = str(byte)
                        data = parse(xml_data)
                        title = data['project']['Title']
                        obj = {}
                        name = str(root).replace('.\\', '')
                        obj["path"] = name
                        obj["name"] = str(title).replace(':', '-')
                        mapping[name] = obj
        return mapping


