#!/usr/bin/env python
#coding=utf-8

lines = '''
<table>
    <tr>
        <td>序列号</td><td>DEIN3-39CD3-2093J3</td>
        <td>日期</td><td>2013年1月22日</td>
        <td>售价</td><td>392.70 元</td>
        <td>说明</td><td>仅限5用户使用</td>
    </tr>
</table>
'''

import re
m = re.findall(r'<td>(.*?)</td>', lines, re.I|re.M)
if m:
    for x in m:
        print x