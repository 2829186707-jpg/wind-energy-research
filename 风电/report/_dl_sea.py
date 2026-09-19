# -*- coding: utf-8 -*-
import urllib.request
url = 'https://aka.doubaocdn.com/s/fGTIvazyhO'
path = r'D:\桌面\风电\风电\report\assets\sea.jpg'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data = urllib.request.urlopen(req, timeout=60).read()
with open(path, 'wb') as f:
    f.write(data)
print('sea.jpg', len(data), 'bytes')
