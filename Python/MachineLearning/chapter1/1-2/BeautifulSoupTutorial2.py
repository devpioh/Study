from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="https://naver.com">naver</a></li>
        <li><a href="https://www.ruliweb.com">ruliweb</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup( html, "html.parser" )

# all extract
link = soup.find_all("a")


# show links
for l in link:
    href = l.attrs['href']
    txt = l.string
    print( txt, ">", href)
