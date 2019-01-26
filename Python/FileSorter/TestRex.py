import sys
import os
import re



try:
    origin = open( sys.argv[1], "r", encoding="UTF-8")
    # origin = open( "D:/Study/Study/Python/FileSorter/SearchReport.txt", "r", encoding="UTF-8")
    origintxt = origin.read()
    origin.close()

    # print("-------------Start-------------")
    # print(origintxt)
    # print("-------------End-------------")

    #p = re.compile( r"^([.].+\s+:\s+\d+)$", re.MULTILINE )
    #test = p.findall( origintxt )
    test = re.sub( r"[.].+:\s+\d+", "", origintxt )
    print( test )

    convert = open( "D:/Study/Study/Python/FileSorter/CopySearchReport.txt", "w", encoding="UTF-8" )
    convert.write( test )
    convert.close()


except Exception as e:
    print(e)


