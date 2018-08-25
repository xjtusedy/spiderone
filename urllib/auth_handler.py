from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handle = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handle)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)