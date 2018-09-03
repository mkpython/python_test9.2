# -*- coding:utf-8 -*-

import socket
import binascii
from FrameStarter_Discriminate import framestarter
from Concentrator_logical_address import *
from slicing_data import slicing
from MSTA_SEQ import *
from Control_code import *
from data_len import *
from CS import *
from Terminator import *


#与服务器连接导入数据
target_host = '219.128.125.98'
target_port = 9804
addr=(target_host, target_port)

# 建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send():
    # data = input('输入登陆报文:')
    data = '68 96 00 20 00 60 00 68 A1 03 00 11 11 11 BD 16'
    print('登陆报文：68 96 00 20 00 60 00 68 A1 03 00 11 11 11 BD 16')
    print('Data transmission...')
    send_data = bytearray.fromhex(data)
    client.send(send_data)

send()

# 将服务器传输过来的数据转换成字串
def re():
    get_data = binascii.b2a_hex(client.recv(1024))           # 转换成16进制
    data_str = get_data.decode('utf-8',errors="strict")      # 转换成字符串
    # print('接收到的报文内容为：{0}'.format(data_str))
    return data_str

# 各类解析功能函数
while True:
    tag = slicing(re())
    framestarter(tag)
    rtua(tag)
    MSTA(tag)
    Cc(tag)
    L(tag)
    cs(re())
    terminator(tag)


client.close()




