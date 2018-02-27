#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习内建模块之HTMLParser'

__author__ = 'sergiojune'
from html.parser import HTMLParser
import requests


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):  # 这个是处理开始标签
        print('<%s>' % tag, list(attrs))

    def handle_endtag(self, tag):  # 这个是处理结束标签
        print('</%s>' % tag)

    def handle_data(self, data):  # 这个是处理标签里的内容
        print(data)

    def handle_comment(self, data):  # 这个是处理注释
        print('<!--', data, '-->')

    def handle_entityref(self, name):  # 这个是处理特殊字符，比如&nbsp;
        print('&%s;' % name)

    def handle_charref(self, name):  # 这个是处理特殊字符，比如&#1234;
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


# 作业：找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
class DealHTML(HTMLParser):
    def __init__(self):
        super(DealHTML, self).__init__()
        self.thing = 0
        self.time = 0
        self.address = 0

    def handle_starttag(self, tag, attrs):
        if len(attrs) == 1:
            if 'python-events' in list(attrs)[0][1]:  # 获取工作事件
                print('<href=%s>' % list(attrs)[0][1], end='')
                self.thing = 1
            if 'datetime' in list(attrs)[0][0]:  # 获取工作时间
                print('<%s>' % list(attrs)[0][0], end='')
                self.time = 1
            if 'location' in list(attrs)[0][1]:  # 获取工作地点
                print('<%s>' % list(attrs)[0][1], end='')
                self.address = 1

    def handle_data(self, data):
        if self.thing:
            print(data, end='')
        if self.time:
            print(data, end='')
        if self.address:
            print(data, end='')

    def handle_endtag(self, tag):
        if self.thing:
            print('</%s>' % tag)
            self.thing = 0
        if self.time:
            print('</%s>' % tag)
            self.time = 0
        if self.address:
            print('</%s>' % tag)
            print('')
            self.address = 0


response = requests.get('https://www.python.org/events/python-events/').text
dh = DealHTML()
dh.feed(response)
