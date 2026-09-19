# -*- coding: utf-8 -*-
import re
t = open(r'D:\桌面\风电\风电\report\index.html', encoding='utf-8').read()
m = re.search(r'<h2>核心结论摘要</h2>(.*?)<div class="conclusion">', t, re.S)
s = m.group(1)
print('summary cards:', s.count('card metric'))
print('label 2025 gone:', '东方电缆海缆毛利率（2025）' not in s)
print('lu:', '陆风年新增中枢' in s)
print('hai:', '海上风电新增' in s)
print('yq:', '海风年新增目标' in s)
