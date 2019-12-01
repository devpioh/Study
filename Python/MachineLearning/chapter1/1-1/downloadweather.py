import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# set variable
value = {
    #'stnId': '108'
    'stnId' : '184'
}


params = urllib.parse.urlencode(value)

# create request url
url = API + "?" + params
print( "url = ", url )


#download weather info
data = urllib.request.urlopen( url ).read()
text = data.decode( "utf-8" )
print(text)

