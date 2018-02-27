#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习内建模块之struct'

__author__ = 'sergiojune'
import struct,base64

# 这个模块是将bytes与其他二进制数据互相转换
# 将任意数据类型转为bytes
i = 10249999
b = struct.pack('>I', i)  # 第一个参数为处理指令
print(b)

s = 123.456
b = struct.pack('f', s)
print(b)


# 将bytes转为其他任意类型
s = struct.unpack('f', b)
print(s)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
un = struct.unpack('<cciiiiiihh', s)
print(un)


# 作业：编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


# 判断位图文件是根据他的前30个字节来判断的
def bmp_info(data):
    un = struct.unpack('<cciiiiiihh', data[:30])
    if un:
        if un[0] == b'B' and un[1] == b'M':
            return {'width': un[6],
                    'height': un[7],
                    'color': un[9]}
    return 'not bmp'


b = bmp_info(bmp_data)
print(b)
