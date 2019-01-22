import os
from enum import Enum

class FileExt(Enum):
    none = 0
    zip = 1
    jpg = 2
    png = 3
    zip7 = 4

class FileInfo:
    @staticmethod
    def strExtension(fileExt):
        if fileExt is FileExt.zip:
            return ".zip"
        elif fileExt is FileExt.jpg:
            return ".jpg"
        elif fileExt is FileExt.png:
            return ".png"
        return ""

    @staticmethod
    def enumExtension(path):
        name, ext = os.path.splitext(path)

        if not ("" == ext or None == ext):
            if ".zip" == ext:
                return FileExt.zip
            elif ".jpg" == ext:
                return FileExt.jpg
            elif ".png" == ext:
                return FileExt.png

        return FileExt.none


    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.ext = FileInfo.enumExtension( name )
        self.fullPath = os.path.join( path, name )

    

