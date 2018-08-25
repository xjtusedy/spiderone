import urllib.request
import urllib.parse
if __name__ == "__main__":
    #response = urllib.request.urlopen('https://www.python.org')
    #print(response.read().decode('utf-8'))
    #print(response.status)
    #print(response.getheaders())
    #print(response.getheader('Server'))
    #data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
    #reponse = urllib.request.urlopen('http://httpbin.org/post',data=data)
    #print(reponse.read())
    #request = urllib.request.Request('https://python.org')
    #response = urllib.request.urlopen(request)
    #print(request.read().decode('utf-8'))
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host':'httpbin.org'
    }

    dict = {
        'name':'Germey'
    }

    data = bytes(urllib.parse.urlencode(dict),encoding='utf-8')
    req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
    reaponse = urllib.request.urlopen(req)
    print(reaponse.read().decode('utf-8'))