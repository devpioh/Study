import os
import sys
import io
from file_structure import FileInfo

class FileExplorer:
    def __init__(self):
        self.fileDirectory = dict()
        self.fileTypes = dict()
        self.files = dict()
        self.reportName = "SearchReport.txt"
        self.statingDir = ""

    def Search(self, dirname):
        print("Start Serarch : " + dirname)
        try:
            self.statingDir = dirname
            for(path, folders, files) in os.walk(dirname):
                if folders in files:
                    files.remove(folders)

                if None == files or 0 == len(files) : continue
                    
                self.fileDirectory[path] = files
                self.fileTypes[path] = dict()

                for filename in files:
                    name, ext = os.path.splitext( filename )
                    if not ext in self.fileTypes[path]:
                        self.fileTypes[path][ext] = list()
                    if not ext in self.files:
                        self.files[ext] = list()
                    
                    self.fileTypes[path][ext].append( name )
                    self.files[ext].append( FileInfo( path, name ) )

        except Exception as e:
            print(e)
        
    def DisplaySearchFiles(self):
        print( "------------------ show ------------------")

        print( "<<<< Extension Type And Count >>>>")
        for ext in self.files.keys():
            print("%s : %d" % (ext, len(self.files[ext])))

        print( "<<<< Path Detail >>>>")
        for key, values in self.fileDirectory.items():
            print( "path : " + key )

            for extKey, extValue in self.fileTypes[key].items():
                print( ("%s : %d" % (extKey, len(extValue))) )

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
                for ext in self.files.keys():
                    f.writelines( "%s : %d\n"% (ext, len(self.files[ext])) )

                f.writelines( "[ File Path Info ]\n")
                for key, values in self.fileDirectory.items():
                    # print( "path : " + key )
                    f.writelines( "path : " + key + "\n" )
                    
                    for extKey, extValue in self.fileTypes[key].items():
                        # print( ("%s : %d" % (extKey, len(extValue))) )
                        f.writelines( ("%s : %d \n" % (extKey, len(extValue))) )
                        
                    for value in values:
                        # print( " - " + value )
                        f.writelines( " - " + value + "\n" )
        except Exception as e:
            print( e )