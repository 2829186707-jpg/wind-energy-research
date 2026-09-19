# -*- coding: utf-8 -*-
import os, urllib.request
base = r'D:\桌面\风电\风电\report\assets'
os.makedirs(os.path.join(base, 'parts'), exist_ok=True)
jobs = [
    ('https://aka.doubaocdn.com/s/iuhbi9yP6V', base + r'\sea.jpg'),
    ('https://aka.doubaocdn.com/s/53NvQ3VeZm', base + r'\parts\blade.jpg'),
    ('https://aka.doubaocdn.com/s/cNpGDkoxks', base + r'\parts\gearbox.jpg'),
    ('https://aka.doubaocdn.com/s/nbv62jaZyV', base + r'\parts\generator.jpg'),
    ('https://aka.doubaocdn.com/s/2FDM5SjDO9', base + r'\parts\bearing.jpg'),
    ('https://aka.doubaocdn.com/s/JJoBaCvuXF', base + r'\parts\converter.jpg'),
    ('https://aka.doubaocdn.com/s/eHFVvGYRRN', base + r'\parts\nacelle.jpg'),
    ('https://aka.doubaocdn.com/s/g3zhEYqLtc', base + r'\parts\tower.jpg'),
    ('https://aka.doubaocdn.com/s/TmOwG13hVy', base + r'\parts\flange.jpg'),
    ('https://aka.doubaocdn.com/s/RPQf4nv0HB', base + r'\parts\monopile.jpg'),
    ('https://aka.doubaocdn.com/s/QoPGFfntNY', base + r'\parts\jacket.jpg'),
    ('https://aka.doubaocdn.com/s/BAE2tanTC2', base + r'\parts\foundation.jpg'),
    ('https://aka.doubaocdn.com/s/dHijKE2yKl', base + r'\parts\cable.jpg'),
    ('https://aka.doubaocdn.com/s/ffbGXm1DC1', base + r'\parts\substation.jpg'),
    ('https://aka.doubaocdn.com/s/vAwxCd45xg', base + r'\parts\installation.jpg'),
]
for url, path in jobs:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req, timeout=60).read()
    with open(path, 'wb') as f:
        f.write(data)
    print(os.path.basename(path), len(data), 'bytes')
