from bs4 import BeautifulSoup
fp = open( "fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup( fp, "html.parser" )

# extract use css selector
print(soup.select_one("li:nth-of-type(8)").string) # 이거 안먹힘 --
#print(soup.select_one("#main-goods > li:nth-of-type(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)


# extract find method
cond = {"data-lo":"us", "class":"black"}
print( soup.find(id="ve-list").find("li", cond).string )

