import os
from enum import Enum

class FileExt(Enum):
    none = 0
    txt = 10
    torrent = 99
    
    zip = 100
    zip7 = 101
    rar = 102

    jpg = 200
    png = 201
    gif = 202

    mp4 = 300
    mp3 = 301
    avi = 302
    flv = 303
    ogg = 304
    swf = 305
    mkv = 306
    wmv = 307
    mov = 308
    ass = 309
    smi = 310
    ttf = 311

    @staticmethod
    def strExtension(fileExt):
        # etc
        if fileExt is FileExt.txt:          return ".txt"
        elif fileExt is FileExt.torrent:    return ".torrent"
        # compress
        elif fileExt is FileExt.zip:        return ".zip"
        elif fileExt is FileExt.zip7:       return ".7z"
        elif fileExt is FileExt.rar:        return ".rar"
        # image
        elif fileExt is FileExt.jpg:        return ".jpg"
        elif fileExt is FileExt.png:        return ".png"
        # video
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
    def enumExtension(fileName):
        ext = fileName
        if not "." == ext[0]:
            name, extension = os.path.splitext(ext)
            ext = extension
        
        # print( "split ext : " + ext )

        if "" == ext or None == ext:    return FileExt.none
        elif ".txt" == ext:             return FileExt.txt
        elif ".torrent" == ext:         return FileExt.torrent
            
        elif ".zip" == ext:             return FileExt.zip
        elif ".7z" == ext:              return FileExt.zip7
        elif ".rar" == ext:             return FileExt.rar

        elif ".jpg" == ext:             return FileExt.jpg
        elif ".png" == ext:             return FileExt.png

        elif ".avi" == ext:             return FileExt.avi
        elif ".mp4" == ext:             return FileExt.mp4
        elif ".mp3" == ext:              return FileExt.mp3
        elif ".flv" == ext:             return FileExt.flv
        elif ".ogg" == ext:             return FileExt.ogg
        elif ".swf" == ext:             return FileExt.swf
        elif ".wmv" == ext:             return FileExt.wmv
        elif ".mkv" == ext:             return FileExt.mkv
        elif ".mov" == ext:             return FileExt.mov
        elif ".ass" == ext:             return FileExt.ass
        elif ".smi" == ext:             return FileExt.smi
        elif ".ttf" == ext:             return FileExt.ttf
