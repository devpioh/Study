from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#url = "https://www.naver.com"
url = "https://www.ruliweb.com"

# extract PhantomJS driver
#browser = webdriver.PhantomJS()
options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)

# wating 3 seconds
browser.implicitly_wait(3)

# read URL
browser.get(url)

# screen capture
browser.save_screenshot("Website.png")

#quit browser
browser.quit()
