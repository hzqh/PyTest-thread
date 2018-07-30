#!/usr/bin/python
# -*-coding:UTF-8-*- 
import struct
import base64
import sys
import binascii
import ctypes
import socket
import time
import hashlib
import hmac
import random
import array
from email.base64mime import body_decode
from Crypto.Cipher import AES
import ConfigParser
import MySQLdb
import datetime,time
from commonUntils import DBConnection
from MySQLdb.constants import FIELD_TYPE
from binascii import b2a_hex, a2b_hex  
import sys
def longToInt(value):
    if value > 2147483647 :
        return (value & (2 ** 31 - 1))
    else :
        return value
    
# 16进制字符串转10进制数组
def hex2arr(hex):
    list = []
    while len(hex) > 1:
        list.append(int(hex[0:2],16))
        hex = hex[2:len(hex)]
    return list


def unpack_list(str):
    return list(struct.unpack('%dB'%len(str), str))
def pack_bin(arr):
    return struct.pack('%dB'%len(arr), *arr)

# 10进制数组转普通字符串
def int_list_str(arr):
    return ''.join(chr(x) for x in arr)

# 普通字符串转16进制字符串
def str2hex(str):
    return binascii.hexlify(str)

# 把10进制数组转为16进制字符串
def arr2hex(arr):
    return binascii.hexlify(int_list_str(arr))
    
def encry_keyValue(keyValue):
    j = 0
    newKeyValue = []
    str1 = "g?ol0d!en@s7ec.1u8r$ityf*e#rr3*yw&a^y"
    str2 = "3g!#d34&fddf*d4adfd8)de+^dad*d57#daTga"
    str3 = "*dne71#dc&ia?yad>lad,ad3h*aducat3~da3)d"
    str4 = "-vdg9e*dqa1cF?Ka3,d3emca*^1p)u5i]ag2r*de"
    for i in range(len(keyValue)):
        # print 'i:',i
        if (i % 2) == 0:
            if (i % 5) == 0:
                newKeyValue.append(keyValue[i] ^ ord(str1[j]))
            else:
                newKeyValue.append(keyValue[i] ^ ord(str2[j]))
        else:
            if (i % 3) == 0:
                newKeyValue.append(keyValue[i] ^ ord(str3[j]))
            else:
                newKeyValue.append(keyValue[i] ^ ord(str4[j]))
        j+=1
        if j > 36:
            j = 0
    return newKeyValue




def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return data
    unpad = lambda s : s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return data

class prpcrypt():  
    def __init__(self, key):  
        self.key = key  
        self.mode = AES.MODE_CBC  
       
    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数  
    def encrypt(self, text):  
        cryptor = AES.new(self.key, self.mode, self.key)  
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用  
        length = 32  
        count = len(text)  
        if(count % length != 0) :  
            add = length - (count % length)  
        else:  
            add = 0  
            text = text + ('\0' * add)  
            self.ciphertext = cryptor.encrypt(text)  
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题  
        #所以这里统一把加密后的字符串转化为16进制字符串  
        return b2a_hex(self.ciphertext)  
       
    #解密后，去掉补足的空格用strip() 去掉  
    def decrypt(self, text):  
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')  
        plain_text = cryptor.decrypt(a2b_hex(text))  
        return plain_text.rstrip('\0')  

if __name__ == '__main__': 
        cf = ConfigParser.ConfigParser()
        cf.read('D:/workplace/PyTest-frame/qtec.conf')  
        conn = MySQLdb.connect(host=eval(cf.get('db6', 'host')),user=eval(cf.get('db6', 'user')),passwd=eval(cf.get('db6', 'passwd')),db=eval(cf.get('db6', 'db')),port=eval(cf.get('db6', 'port')),charset='utf8')
        cur = conn.cursor()
        hero = DBConnection.DBConn(eval(cf.get('db6', 'db')),conn,cur)
#        count1 = hero.select("select count(*) from raw_key_1")
#        firstid1 = hero.select("select id from raw_key_1 limit 1")
#        print count1
        
        file1= open("user.txt",'w')
       # file2 = open('test1.dat','wb')
#        ik = 5385
#        im = str(ik)raw_key
      
    #    for j in range(11398,12184):
        for j in range(13398,15398):
           
            result = hero.select("select  hex(rawpassword),hex(root_key_id),hex(root_key_value) from client_authen_info where user_id ="+str(j)+" " )
            
    
            print "\""+str(result[0])+"\""+','
            
                #print type(result[1])
                
    #            a = str2hex(pack_bin(encry_keyValue(hex2arr(result1[0]))))
              #  a = result[0],result[1]
          #  print >> file1,result[1]
                
           
        file1.close()
        