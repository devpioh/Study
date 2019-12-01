import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

## 1. direct download save
# urllib.request.urlretrieve( url, savename )
# print( "saved" )

## 2. load on memory and save
# mem = urllib.request.urlopen( url ).read()

# with open( "test2.png", mode="wb") as f:
#     f.write( mem )
#     print( "saved two" )


## 3. connect client info view
# url = "https://naver.com"
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen( url )
data = res.read()

text = data.decode( "utf-8" )
print( text )

