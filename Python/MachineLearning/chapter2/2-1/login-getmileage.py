import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

if len(sys.argv) <= 2:
    print( "USGE : login hanbit.co.kr <ID> <PASSWARD>")
    sys.exit()

USER = sys.argv[1]
PASS = sys.argv[2]

#start session
session = requests.session()

#login
login_info = {
    "m_id": USER,
    "m_passwd": PASS
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() #exception from error

#go to mypage
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html" 
res = session.get(url_mypage)
res.raise_for_status()

#get mileage and ecoin
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()

print( "Mileage : " + mileage )
print( "ecoin : " + ecoin )