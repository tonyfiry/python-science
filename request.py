#如何設requests
import requests#匯入requests模組


#送出GET請求
# r = requests.get("http://www.google.com")
# print(r.status_code)#測試出是200，代表是請求成功，如果是400~599，代表是請求失敗。

#判斷是GET是不是成功的
# r = requests.get("http://www.google.com")

# if r.status_code == 200:
#     print("請求成功")
# else:
#     print("請求失敗")

#URL參數
# http://www.google.com?value1=name&value2=number#[?]是參數後面，[&]是符號分隔

#URL傳遞參數，然後送出GET請求
# url_params = {'name':"陳萬安",'score':95}
# r = requests.get("http://httpbin.org/get",params=url_params)
# #print(r.url)#url屬性是取得URL網址完整的字串
# print(r.text)

#送出POST請求
#post_data = {'name':"陳萬安",'score':95}#用字典來傳出資料
#r = requests.post("http://httpbin.org/post",data="post_data")#post請求出來
# print(r.text)#讀取JSON資料進來

#取得HTTP回應內容(Respons centents)
# url_params = {'name':"陳萬安",'score':95}
# r = requests.get("http://httpbin.org/get",params=url_params)
# print(r.text)#讀取JSON資料進來
# print(r.content)#取得沒有編碼的位元組資料
# print(r.encoding)#取得html的編碼
# print(r.raw)#利用HTTPRespons物件

#檢查回應狀態碼
# r = requests.get("https://www.youtube.com/")
# print(r.status_code)#取得回應狀態碼是200
# print(r.status_code == requests.codes.ok)#TRUE
# r = requests.get("https://www.youtube.com/404")
# print(r.status_code)#取得回應狀態碼是404
# print(r.status_code == requests.codes.ok)#FALSE

#取得回應狀態碼進一步資訊
# r = requests.get("https://www.flag.com.tw/")
# print(r.status_code)
# print(r.raise_for_status())#取得進一步的資訊

#取得標頭資訊
# r = requests.get("https://www.flag.com.tw/")
# print(r.headers['content-type'])#取得標頭資訊:content-type
# print(r.headers['date'])#取得標頭資訊:date
# print(r.headers['server'])#取得標頭資訊:server
# print(r.headers.get('server'))#取得標頭資訊:server

#存取Cookie的HTTP請求
# url = "http://httpbin.org/cookies"
# cookies = {'name':'tony','source':'89'}
# r = requests.get(url,cookies=cookies)
# print(r.text)

#取得回應內容的Cookie資料
seeion = requests.session()
reponse = seeion.get("https://www.google.com/")
v = seeion.cookies.get_dict()
print(v)


