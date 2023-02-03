import urllib
import urllib.parse#urllib.parse屬性可以用來取得HTML資料
url_params = {'name':"張騏",'number':40841148}
print(urllib.parse.urlencode(url_params))#name=%E5%BC%B5%E9%A8%8F&number=40841148
