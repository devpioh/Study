import os
import sys
import io
import shutil
from file_structure import FileInfo

class FileExplorer:
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
            if not self.fileDirectory in keyPath:
                print("none collect path : " + keyPath )
                return
             
            if not os.path.exists( targetPath ):
                print( "make directory : " + targetPath )
                os.mkdir( targetPath )
        
            moveFiles = self.fileDirectory[keyPath]
            
        except Exception as e:
            print(e)
    
    def MoveDirectory(self):
        pass

        
    def DisplayCollectFiles(self):
        print( "------------------ show ------------------")

        print( "<<<< Extension Type And Count >>>>")
        for ext in self.fileTypes:
            print("%s : %d" % (ext, self.fileTypes[ext]))

        print( "<<<< Path Detail >>>>")
        for key, values in self.fileDirectory.items():
            print( "path : " + key )

            for value in values:
                print( " - " + value )
        
        print( "------------------ end ------------------")

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