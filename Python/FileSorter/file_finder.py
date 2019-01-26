import os
import sys
import platform
from file_explorer import FileExplorer

def displayMenu():
    print("-------------- Menu --------------")
    print( "Collecting File       : cf <dir>\n" )
    print( "Collected File info   : cv\n" )
    print( "Collected File Clear  : cc\n" )
    print( "Move Collected File   : mvf <odir> <tdir>\n" )
    print( "Clear Display         : clear\n")
    print( "Exit                  : quit(q)\n" )


def selectMenu(ex, option):
    try:
        if "cf" == option[0]:
            ex.CollectFile( option[1] )
        elif "cv" == option[0]:
            ex.DisplayCollectFiles()
        elif "cc" == option[0]:
            ex.Clear()
        elif "mvf" == option[0]:
            print( "orgin path : " + option[1] + "\n" )
            print( "target path : " + option[2] + "\n" )
        elif "quit" == option[0] or "q" == option[0]:
            sys.exit()
        elif "clear" == option[0]:
            if "Windows" == platform.system():
                os.system("cls")
            else:
                os.system("clear")
        else:
            print("Check argument")
                        
    except Exception as e:
        print( e )




if __name__ == "__main__":
    try:
        finder = FileExplorer()
        while True:
            displayMenu()
            selectMenu( finder, input().split() )

    except Exception as e:
        print(e)
    
