from bs4 import BeautifulSoup

# use CSS Selection

html = """
<html><body>
    <div id="meigen">
    <h1>위키 북스 도서</h1>
    <ul class="item">
        <li>유니티 게임 이펙트 입문</li>
        <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
        <li>모던 웹 사이트 디자인의 정석</li>
    </ul>
    </div>
</body></html>
"""

soup = BeautifulSoup( html, "html.parser" )

# extract use CSS Query, need contents
# get title 
h1 = soup.select_one("div#meigen > h1").string
print( "h1=", h1 )

# get items
li_items = soup.select( "div#meigen > ul.item > li" )
for li in li_items:
    print( "li = ", li.string ) 

