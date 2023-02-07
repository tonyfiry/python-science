from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



# driver.get("https://fchart.github.io/test.html")#到測試網頁抓資料
# print("-----------------------------")
# print(driver.title)#取得HTML的title標籤
# html = driver.page_source#取得HTML的原始碼
# print(html)
# driver.quit()#最後關閉瀏覽器視窗
# cookie = {'name':'over18' , "value":"1"}#網址的Application的cookie
# driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")#看板Gossiping 文章列表- 批踢踢實業坊
# driver.add_cookie(cookie)#新增cookie
# print("-----------------------------")
# print(driver.title)#抓取批踢踢實業坊的網址
# driver.quit()#最後關閉瀏覽器視窗
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.implicitly_wait(10)#隱含等待10秒
html = driver.page_source#取得HTML的原始碼
print(html)
driver.quit()


