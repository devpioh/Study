import os
import sys
import platform
import re
from file_explorer import FileExplorer


def displayMain():
    print("-------------- File Finder --------------")
    print("(menu) ->")

def displayMenu():
    print("-------------- Menu --------------")
    print( "Collecting File       : cf <dir>\n" )
    print( "Display info          : (vf, vd, ve)\n" )
    print( "Copy Files            : fc <src> <dst> <ext>\n" )
    print( "Collected File Clear  : cc\n" )
    print( "Move Collected File   : mvf <odir> <tdir> (ext)\n" )
    print( "Clear Display         : clear\n")
    print( "Exit                  : quit(q)\n" )

def combinOption( options, *p ):
    argv = list()
    fix = None
    combineCount = 0
    for option in options:
        if p[0].match( option ):
            fix = None
            fix = option
            print( "[%d] start combin : %s" % (combineCount, fix) )
        elif p[1].match( option ):
            combineCount += 1
            fix = fix + " " + option
            print( "[%d] combin : %s" % (combineCount, fix) )
            if p[2].match( fix ):
                fix = fix[1:]
                fix = fix[:len(fix)-1]
                print( "[%d] end combin : %s" % (combineCount, fix) )
                argv.append(fix)
                fix = None
        else:
            if None == fix:
                argv.append(option)
            else:
                print( "[%d] combin : %s" % (combineCount, fix) )
                combineCount += 1
                fix = fix + " " + option
                print( "[%d] combin : %s" % (combineCount, fix) )

    print( "combind option : " )
    print( argv )

    return argv


def selectMenu(ex, option):
    try:
        if "menu" == option[0]:
            displayMenu()
        elif "cf" == option[0]:
            ex.CollectFile( option[1] )
        elif "vf" == option[0]:
            if 1 < len(option):
                ex.DisplayCollectFilesForPath( option[1] )
            else:
                ex.DisplayCollectFiles()
        elif "vfd" == option[0]:
            ex.DisplayCollectDetail()
        elif "vd" == option[0]:
            ex.DisplayCollectPath()
        elif "ve" == option[0]:
            if 1 < len(option):
                ex.DisplayCollectExtension( option[1] )
            else:
                ex.DisplayCollectExtension( None )
        elif "fc" == option[0]:
            ex.CopyFilesForExt( option[1], option[2], option[3] )
        elif "cc" == option[0]:
            ex.Clear()
        elif "mvf" == option[0]:
            if 3 < len(option):
                ex.MoveFilesForExt( option[1], option[2], option[3] )
            else:
                ex.MoveFiles( option[1], option[2] )
        elif "quit" == option[0] or "q" == option[0]:
            ex.Clear()
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
        p1 = re.compile( "^\"" )
        p2 = re.compile( ".+\"$")
        p3 = re.compile( "^\".+\"$")
        while True:
            if finder.isBusy():
                pass
            else:
                displayMain()
                argv = combinOption( input().split(), p1, p2, p3 )
                selectMenu( finder, argv )
    except Exception as e:
        print(e)
    
