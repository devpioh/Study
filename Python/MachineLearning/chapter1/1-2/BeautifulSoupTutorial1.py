import sys
from bs4 import BeautifulSoup


# check HTML
html = """
<html><body>
    <h1 id="title">스크레이핑이란?</h1>
    <p id="body">웹 페이지를 분석하는 것</p>
    <p id="body2">원하는 부분을 추출하는 것</p>
</body></html>
"""

print( html )


# checking HTML
soup = BeautifulSoup( html, "html.parser" )

# # pick up, want point from html
# h1 = soup.html.body.h1
# p1 = soup.html.body.p
# p2 = p1.next_sibling.next_sibling

# # show piont text
# print( "h1 = ", h1.string )
# print( "p = ", p1.string )
# print( "p = ", p2.string )

# pick up, want id from hteml
title = soup.find(id="title")
body = soup.find(id="body")

# show text
print( "title = ", title.string )
print( "body = ", body.string )


