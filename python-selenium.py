from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)#隱含等待10秒
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)#取得HTML的title標籤
html = driver.page_source#取得HTML的原始碼
print(html)
driver.quit()#最後關閉瀏覽器視窗





