#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习第三方模块之pillow'

__author__ = 'sergiojune'
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
# 对图像进行缩小
im = Image.open('test.jpg')
w, h = im.size  # 获取图片的宽高
print('origin image width is %d, height is %d' % (w, h))
# 进行缩小一倍
im.thumbnail((w//2, h//2))  # 参数是一个元组，对应的是宽高
im.save('suoxiao.png', 'png')
print('now width is %d, height is %d' % (im.size[0], im.size[1]))

# 还可以对图像进行模糊化
im2 = im.filter(ImageFilter.BLUR)
im2.save('muhu.png', 'png')


# 利用这个模块产生验证码
def rndchar():  # 产生随机字符
    return chr(random.randint(65, 90))


def rndcolor():  # 随机颜色
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 240
height = 40
# 创建图像对象
im = Image.new('RGB', (width, height), (255, 255, 255))
# 创建字体
font = ImageFont.truetype(r'E:\python_project\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmsy10.ttf', 36)
# 创建画笔
draw = ImageDraw.Draw(im)
# 填充图片
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndcolor2())
# 写文字
for x in range(4):
    draw.text((60*x+10, 10), rndchar(), font=font, fill=rndcolor())

# mohu
im.filter(ImageFilter.BLUR)
# 保存图片
im.save('yan.png', 'png')
