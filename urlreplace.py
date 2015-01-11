#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 将网页里面的相对链接转换成绝对链接
import re
from urlparse import urljoin

s = """
    <a href="/abc">abc</a><a href="/123">123</a>
    <a href="http://www.google.com">google</a>
    <a href="test">test</a>
    """
p = re.compile(r'(<a.*?href=")(.*?)(".*?/a>)', re.I)    # ? 最小匹配,保证同一行多个链接能被匹配到


def replm(m):
    site = "http://hdq.me"
    match_url = m.group(2)
    if "://" not in match_url:  # 不含://来的链接是相对路径
        new_url = urljoin(site, match_url)
    return m.group(1) + new_url + m.group(3)
print p.sub(replm, s)
