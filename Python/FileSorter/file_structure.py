import os

from file_extension import FileExt

class FileInfo:
    @staticmethod
    def strExtension(fileExt):
        # etc
        if fileExt is FileExt.txt:          return ".txt"
        elif fileExt is FileExt.torrent:    return ".torrent"
        # comp
        elif fileExt is FileExt.zip:        return ".zip"
        elif fileExt is FileExt.zip7:       return ".7z"
        elif fileExt is FileExt.rar:        return ".rar"
        # i
        elif fileExt is FileExt.jpg:        return ".jpg"
        elif fileExt is FileExt.png:        return ".png"
        # vi
        elif fileExt is FileExt.avi:        return ".avi"
        elif fileExt is FileExt.mp4:        return ".mp4"
        elif fileExt is FileExt.mp3:        return ".mp3"
        elif fileExt is FileExt.flv:        return ".flv"
        elif fileExt is FileExt.ogg:        return ".ogg"
        elif fileExt is FileExt.swf:        return ".swf"
        elif fileExt is FileExt.mkv:        return ".wmv"
        elif fileExt is FileExt.mkv:        return ".mkv"
        elif fileExt is FileExt.wmv:        return ".wmv"
        elif fileExt is FileExt.mov:        return ".mov"
        elif fileExt is FileExt.ass:        return ".ass"
        elif fileExt is FileExt.smi:        return ".smi"
        elif fileExt is FileExt.ttf:        return ".ttf"
        
        return ""

    @staticmethod
    def enumExtension(path):
        name, ext = os.path.splitext(path)

        if not ("" == ext or None == ext):
            if ".txt" == ext:           return FileExt.txt
            elif ".torrent" == ext:     return FileExt.torrent
                
            elif ".zip" == ext:         return FileExt.zip
            elif ".7z" == ext:          return FileExt.zip7
            elif ".rar" == ext:         return FileExt.rar
                
            elif ".jpg" == ext:         return FileExt.jpg
            elif ".png" == ext:         return FileExt.png
                
            elif ".avi" == ext:         return FileExt.avi
            elif ".mp4" == ext:         return FileExt.mp4
            elif "mp3" == ext:          return FileExt.mp3
            elif ".flv" == ext:         return FileExt.flv
            elif ".ogg" == ext:         return FileExt.ogg
            elif ".swf" == ext:         return FileExt.swf
            elif ".wmv" == ext:         return FileExt.wmv
            elif ".mkv" == ext:         return FileExt.mkv
            elif ".mov" == ext:         return FileExt.mov
            elif ".ass" == ext:         return FileExt.ass
            elif ".smi" == ext:         return FileExt.smi
            elif ".ttf" == ext:         return FileExt.ttf

        return FileExt.none


    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.ext = FileInfo.enumExtension( name )
        self.fullPath = os.path.join( path, name )

    

