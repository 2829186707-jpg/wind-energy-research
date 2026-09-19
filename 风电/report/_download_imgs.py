# -*- coding: utf-8 -*-
import os, urllib.request
os.makedirs(r'D:\桌面\风电\风电\report\assets', exist_ok=True)
jobs = [
    ('https://aka.doubaocdn.com/s/ygsGjTYvrn', r'D:\桌面\风电\风电\report\assets\land.jpg'),
    ('https://aka.doubaocdn.com/s/aOYdWCs3cF', r'D:\桌面\风电\风电\report\assets\sea.jpg'),
]
for url, path in jobs:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req, timeout=60).read()
    with open(path, 'wb') as f:
        f.write(data)
    print(path, len(data), 'bytes')
