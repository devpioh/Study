import os
import sys
import io
import shutil
from file_structure import *

class FileExplorer:
    @staticmethod
    def replaceDirSlash(dir):
        if not None == dir:
            dir = dir.replace( "\\", "/" )
        
        return dir


    def __init__(self):
        self.fileDirectory = dict()
        self.fileTypes = dict()
        self.files = dict()
        self.reportName = "SearchReport.txt"
        self.statingDir = ""
    
    def Clear(self):
        self.fileDirectory.clear()
        self.fileTypes.clear()
        self.files.clear()
        self.statingDir = ""

    def CollectFile(self, dirname):
        dirname = FileExplorer.replaceDirSlash( dirname )
        print("Start Collect : " + dirname)
        if not os.path.exists( dirname ):
           print( "Chek path or permission" ) 
        else:
            try:
                self.statingDir = dirname
                for(path, folders, files) in os.walk(dirname):
                    if folders in files:
                        files.remove(folders)

                    if None == files or 0 == len(files) : continue
                        
                    self.fileDirectory[path] = files
                    self.files[path] = list()

                    for filename in files:
                        name, ext = os.path.splitext( filename )
                        if not ext in self.fileTypes:
                            self.fileTypes[ext] = int()

                        self.fileTypes[ext] += 1
                        self.files[path].append( FileInfo( path, filename ) )

            except Exception as e:
                print(e)
    
    def DeleteFiles(self):
        pass

    def DeleteDirectory(self):
        pass

    def MoveFiles(self, keyPath, targetPath):
        try:
            keyPath = FileExplorer.replaceDirSlash(keyPath)
            targetPath = FileExplorer.replaceDirSlash(targetPath)
            print( "move file : %s, %s" %(keyPath, targetPath) )
            if not keyPath in self.fileDirectory:
                print("none collect path : " + keyPath )
                return
             
            if not os.path.exists( targetPath ):
                print( "make directory : " + targetPath )
                os.mkdir( targetPath )
        
            moveFiles = self.fileDirectory[keyPath]
            moveInfos = self.files[keyPath]

            for mt in moveInfos:
                dist = os.path.join( targetPath, mt.name )
                shutil.move( mt.fullPath, dist )

                mt.fullPath = dist
                mt.path = targetPath

            del self.fileDirectory[keyPath]
            del self.files[keyPath]

            self.fileDirectory[targetPath] = moveFiles
            self.files[targetPath] = moveInfos

            os.rmdir(keyPath)
            
        except Exception as e:
            print(e)
    
    def MoveFilesForExt(self, keyPath, targetPath, ext):
        try:
            keyPath = FileExplorer.replaceDirSlash(keyPath)
            targetPath = FileExplorer.replaceDirSlash(targetPath)
            print( "move file : %s, %s, %s" %(keyPath, targetPath, ext) )
            
            if not keyPath in self.fileDirectory:
                print("none collect path : " + keyPath )
                return
            elif FileExt.none == FileInfo.enumExtension(ext.lower()):
                print("none collect ext : %s" %  FileInfo.enumExtension(ext.lower()) )
                return
             
            if not os.path.exists( targetPath ):
                print( "make directory : " + targetPath )
                os.mkdir( targetPath )

            moveExt = FileInfo.enumExtension(ext.lower())

            if not targetPath in self.fileDirectory:
                self.fileDirectory[targetPath] = list()

            if not targetPath in self.files:
                self.files[targetPath] = list()
            
            moveInfos = self.files[targetPath]
            moveFiles = self.fileDirectory[targetPath]

            for mt in self.files[keyPath]:
                if mt.ext == moveExt:
                    dist = os.path.join( targetPath, mt.name )
                    shutil.move( mt.fullPath, dist )

                    mt.fullPath = dist
                    mt.path = targetPath
                    
                    moveInfos.append( mt )
                    moveFiles.append( mt.name )
                    self.files[keyPath].remove( mt )
                    self.fileDirectory[keyPath].remove( mt.name )

        except Exception as e:
            print(e)

    def copyFileObj( self, src, dst, callback_done, length=8*1024 ):
        with open(src, "r") as fsrc:
            with open(dst, "w") as fdst:
                copied = 0
                while True:
                    buf = fsrc.read(length)
                    if not buf:
                        break
                    fdst.write(buf)
                    copied += len(buf)
                callback_done(fsrc=fsrc, fdst=fdst, copied=copied)

    
    def MoveDirectory(self):
        pass

        
    def DisplayCollectFiles(self):
        print( "------------------ Collected Files ------------------" )

        print( "<<<< Extension Type And Count >>>>")
        for ext in self.fileTypes:
            print("%s : %d" % (ext, self.fileTypes[ext]))

        print( "<<<< Path Detail >>>>")
        for key, values in self.fileDirectory.items():
            print( "path : " + key )

            for value in values:
                print( " - " + value )
        
        print( "------------------ Collected Files ------------------" )

    def DisplayCollectPath(self):
        print( "------------------ Collected Path ------------------" )
        for path in self.fileDirectory:
            print( path )
        print( "------------------ Collected Path ------------------" )

    def DisplayCollectExtension(self, path):
        print( "------------------ Collected Extension ------------------" )    
        if None == path or not path in self.fileDirectory:
            print( "< All Extenstions >")
            for ext in self.fileTypes:
                print( "%s : %d" % (ext, self.fileTypes[ext]))
        else:
            print( "< Collect Extension Path : " + path + " >" )

            types = dict()
            for info in self.files[path]:
                if not info.ext in types:
                    types[info.ext] = 1
                else:
                    types[info.ext] += 1
            
            for ext in types:
                print( "%s : %d" % (FileInfo.strExtension(ext), types[ext]))
        print( "------------------ Collected Extension ------------------" )
    
    def DisplayCollectDetail(self):
        print( "------------------ Collected Detail ------------------" )
        for k, v in self.files.items():
            print( "[ key path : " + k + " ]" )
            for item in v:
                print( item.toStr() )
        print( "------------------ Collected Detail ------------------" )
        
    def ExportSearchReport(self, exportPath):
        try:
            if not os.path.exists( exportPath ):
                os.makedirs( exportPath )
                
            reportDist = os.path.join( exportPath, self.reportName )

            print( "MAKE REPORT PATH : " + reportDist )
            
            with open( reportDist, "w", encoding="UTF-8", newline="" ) as f:
                f.writelines( "Explore Directory : " + self.statingDir + "\n" )
                f.writelines( "[ File Extension Count ]\n")
                for ext in self.fileTypes:
                    f.writelines( "%s : %d\n"% (ext, self.fileTypes[ext]) )

                f.writelines( "[ File Path Info ]\n")
                for key, values in self.fileDirectory.items():
                    f.writelines( "path : " + key + "\n" )

                    for value in values:
                        f.writelines( " - " + value + "\n" )
        except Exception as e:
            print( e )