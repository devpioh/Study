import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

user_id = sys.argv[1]
user_pass = sys.argv[2]

url = "https://nid.naver.com/nidlogin.login"

# initilaize webdriver
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)


# connect login
browser.get(url)
print("connect naver login page")

# try login
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(user_id)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(user_pass)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print( "login naver" )

# get shopping list
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# print shopping list
#products = browser.find_elements_by_css_selector(".p_info span")
products = browser.find_elements_by_css_selector(".name span")

print(products)
for product in products:
    print( "-", product.text )


