import os
import sys
from file_explorer import FileExplorer

if __name__ == "__main__":
    try:
        explorer = FileExplorer()
        if "-sv" == sys.argv[1]:
            explorer.Search( sys.argv[2] )
            explorer.DisplaySearchFiles()
        elif "-sve" == sys.argv[1]:
            explorer.Search( sys.argv[2] )
            explorer.ExportSearchReport( sys.argv[3] )
            explorer.DisplaySearchFiles()
    except Exception as e:
        print(e)
    
