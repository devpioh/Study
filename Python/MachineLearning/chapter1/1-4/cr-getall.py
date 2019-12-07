#파이썬 매뉴얼을 재귀적으로 다운로드
from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

#이미 처리한 파일인지 확인 하기 위한 컨테이너
proc_files = {}

#HTML 내부에 있는 링크를 추출
def enum_links(html, base):
    soup = BeautifulSoup( html, "html.parser")

    if soup is None:
        return []

    links = soup.select("link[rel='stylesheet']") #CSS
    links += soup.selct("a[href]")  #link
    result = []

    #href 속성을 추출하고, 링크를 절대 경로로 변환.
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)

    return result


#파일을 다운로드 받고 저장
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    
    if re.search( r"/$", savepath): #폴더라면 index.html
        savepath += "index.html"

    savedir = os.path.dirname(savepath)

    #모두 다운로드 받았는지 확인
    if os.path.exists(savepath):
        return savepath
    
    #다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)

    #파일 다운로드
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1) # 1초 딜레이
        return savepath
    except:
        print("failed download : ", url)
        return None


#HTML을 분석하고 다운
def analyze_html(url, root_url):
    savepath = download_file(url)

    if savepath is None: return
    if savepath in proc_files: return

    proc_files[savepath] = True

    print("analyze_html=", url)

    #링크 추출
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)


    for link_url in links:
        #링크가 루트 이외의 경로를 나타낸다면 무시
        if 0 != link_url.find(root_url):
            if not re.search(r".css$", link_url): continue
        
        #HTML 이라면
        if re.search( r".(html|htm)$", link_url):
            #재귀적으로 HTML 파일 분석
            analyze_html(link_url, root_url)
            continue

        #기타 파일
        download_file(link_url)


if __name__ == "__main__":
    #URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)

    