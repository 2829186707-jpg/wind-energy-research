# -*- coding: utf-8 -*-
import re
t = open(r'D:\桌面\风电\风电\report\index.html', encoding='utf-8').read()
m = re.search(r'<script>(.*?)</script>', t, re.S)
js = m.group(1)
open(r'D:\桌面\风电\风电\report\_check.js', 'w', encoding='utf-8').write(js)
print('js extracted:', len(js))
