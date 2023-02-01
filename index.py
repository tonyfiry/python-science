import requests

##學會GET請求
#r = requests.get("https://www.google.com/")
#print(r.status_code)#請求成功，是200，如果是400~599，表示有錯誤，例如400表示是網頁不存在

# url_params = {'name': '陳會安', 'score': 95}
# r = requests.get("https://www.google.com/",params = url_params)
# print(r.url)#這屬性可以取得完整URL網址字串。
# print(r.text)#這屬性可以用在URL網址自字串出來(JSON)

#學會POST請求
url_params = {'name':'張騏','math':'40841148'}
r = requests.post("http://httpbin.org/post",params=url_params)
print(r.text)