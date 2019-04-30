import os

from file_extension import FileExt
from file_regex import NationCode
from file_regex import StringConverter

class FileInfo:

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.ext = FileExt.enumExtension( name )
        self.fullPath = os.path.join( path, name )
        self.localeCode = NationCode.getNationValue( name )

    def toStr(self):
        print("{ \npath : %s\nname : %s\next : %s\nfullpath : %s\n}\n"%(self.path, self.name, self.ext, self.fullPath))

    

