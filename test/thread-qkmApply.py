# -*-coding:UTF-8-*- 
import struct
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
from server import reqPacket,rcPacket,ackPacket
from server import qkmApply
from server import qkmGet
from commonUntils import adminPacket
from commonUntils import ExcelUntil
#import tools
import datetime,time
#import adminPacket
from commonUntils import adminPacket
import threading
import unicodedata

global Akm_HOST
global Qkm_HOST
#Qkm_HOST='192.168.91.84'
Qkm_HOST='10.64.117.1'
#Qkm_HOST='192.168.126.132'
remote_user_id=100259
Akm_HOST='192.168.91.183'
BUFSIZE = 1024 
PORT = 5530

k=0
d=0


def setUserInfo():
    userinfo = ExcelUntil.excel_read_all("D:\\workplace\\PyTest-frame\\data\\userinfo9.xls",index_name='Sheet1',startrow = 1,startcol =0) #读取Excel用户信息，读取起始位置startrow = 1,startcol =0
    lists=[[] for i in range(len(userinfo))]
    for i in range(0,len(userinfo)):
        userinfo[i][0] = int(userinfo[i][0])
        userinfo[i][1] = str(userinfo[i][1])
        userinfo[i][2] = int(userinfo[i][2])
        userinfo[i][3]=ExcelUntil.excel_data_to_list(userinfo[i][3])
        userinfo[i][4]=ExcelUntil.excel_data_to_list(userinfo[i][4])   
    return userinfo

def admin_thread():
    clientList=setUserInfo()      
    print 'starting at:', time.ctime() 

    threads = [] 
    for i in range(0,len(clientList)):  # create all threads 
       
        t = threading.Thread(target=clientRun,args=(Qkm_HOST,clientList[i][1],clientList[i][2],clientList[i][3],clientList[i][4]))

        threads.append(t) 
       
    for i in range(0,len(clientList)):  # start all threads 
        threads[i].start() 
  
    for i in range(0,len(clientList)):  # wait for completion 
        threads[i].join() 
  
    print 'all DONE at:', time.ctime()   
#
##�ͻ��˽����ȴ��������������ͱ���    
def clientRun(host_ip,user_name,user_typ,key_id,authid):
#    print '---clientRun----key_id:',key_id
#    print '---clientRun----authid:',authid
    print 'start loop', user_name, 'at:', time.ctime() 
    host = host_ip
    port = PORT
    global k
    global d
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print '---line 110---Failed to create socket.Error code: '+ str(msg[0]) + ', Error message: ' + msg[1]
        sys.exit()
    print '---line 112--- Socket create'
    s.connect((host, port))    
    #����������֤ʵ������Ҫ�����û������û����ͺ�key_id
    admin_packet=adminPacket.AdminPacket(user_name,user_typ,key_id)
    #����socket������֤
    if admin_packet.admin(s,authid)==1:
       k=k+1
        
    ack_key=admin_packet.get_sess_key()
    ack_key_id=admin_packet.get_sess_key_id()
    time.sleep(10)
#    qkmApply.qkmapply(s,ack_key,ack_key_id,user_name) 
    if qkmGet.qkmget(s,ack_key,ack_key_id,user_name)==1:
       d=d+1   
    
if __name__ == '__main__':
#    attend_num=UserNum
    clientList=setUserInfo() 
    admin_thread()
    print '----totalclient----',k
    print '----totalget----',d




    
        