#!/usr/bin/env python

import sys
import urllib.request as req
import urllib.parse as parse

# command line variable
if len(sys.argv) <= 1:
    print( "USAGE : downloadweather-argv <Region Number>" )
    sys.exit()
regionNumber = sys.argv[1]

# set input variable and set URL
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
value = {
    'stnId' : regionNumber
}

params = parse.urlencode( value )
url = API + "?" + params
print( "url = ", url )

# download
data = req.urlopen( url ).read()
txt = data.decode( "utf-8" )
print( txt )
