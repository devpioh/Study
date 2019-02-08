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
    print( "System terminal       : -sys (ls, ...)" )
    print( "Collecting File       : -col <dir>" )
    print( "Display info          : -view (file <dir>, dir, ext <dir>)" )
    print( "Copy Files            : -copy <src> <dst> <ext>" )
    print( "Collected File Clear  : -empty" )
    print( "Move Collected File   : -move <src> <dst> (ext)" )
    print( "Clear Terminal        : clear" )
    print( "Exit                  : quit(q)" )

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
        elif "-sys" == option[0]:
            argv = ""
            
            if "Windows" == platform.system():
                if "ls" == option[1]:
                    option[1] = "dir"
                elif "clear" == option[1]:
                    option[1] = "cls"
            
            for i in range( 1, len(option) ):
                argv = argv + " " + option[i]

            os.system( argv )

        elif "-col" == option[0]:
            ex.CollectFile( option[1] )

        elif "-view" == option[0]:
            if "file" == option[1]:
                if 2 < len(option):
                    ex.DisplayCollectFilesForPath( option[2] )
                else:
                    ex.DisplayCollectFiles()
            elif "dir" == option[1]:
                ex.DisplayCollectPath()
            elif "ext" == option[1]:
                if 2 < len(option):
                    ex.DisplayCollectExtension( option[2] )
                else:
                    ex.DisplayCollectExtension( None )
            elif "detail" == option[1]:
                ex.DisplayCollectDetail()

        elif "-copy" == option[0]:
            ex.CopyFilesForExt( option[1], option[2], option[3] )

        elif "-move" == option[0]:
            if 3 < len(option):
                ex.MoveFilesForExt( option[1], option[2], option[3] )
            else:
                ex.MoveFiles( option[1], option[2] )

        elif "-empty" == option[0]:
            ex.Clear()

        elif "clear" == option[0]:
            if "Windows" == platform.system():
                os.system( "cls" )
            else:
                os.system( "clear" )

        elif "quit" == option[0] or "q" == option[0]:
            ex.Clear()
            sys.exit()

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
    
