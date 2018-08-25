import http.cookiejar,urllib.request

if __name__ == "__main__":
    filename = 'cookies.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    #cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    #request = urllib.request.Request()
    response = opener.open("https://www.baidu.com")
    for item in cookie:
        print(item.name+"="+item.value)
    cookie.save(ignore_discard=True,ignore_expires=True)