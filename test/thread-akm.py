# -*-coding:UTF-8-*- 
import struct
import sys
import binascii
import ctypes
import socket
import time

from commonUntils import ExcelUntil
from commonUntils import adminPacket
#from commonUntils import adminPacket
import threading
#import unicodedata
from ApplicationKey import akm
from ApplicationKey import qkm

global Akm_HOST
global Qkm_HOST
#Qkm_HOST='192.168.91.84'
#Qkm_HOST='192.168.94.201'
Akm_HOST='192.168.94.220'

Qkm_HOST='192.168.91.112'
#Akm_HOST='192.168.91.113'
#Qkm_HOST='192.168.126.132'
remote_user_id=7000002
BUFSIZE = 1024 
PORT = 5530


k=0
d=0


def setUserInfo1():
    userinfo = ExcelUntil.excel_read_all("D:\\workplace\\PyTest-frame\\data\\userinfo1.xls",index_name='Sheet1',startrow = 1,startcol =0) #读取Excel用户信息，读取起始位置startrow = 1,startcol =0
    lists=[[] for i in range(len(userinfo))]
    for i in range(0,len(userinfo)):
        userinfo[i][0] = int(userinfo[i][0])
        userinfo[i][1] = str(userinfo[i][1])
        userinfo[i][2] = int(userinfo[i][2])
        userinfo[i][3]=ExcelUntil.excel_data_to_list(userinfo[i][3])
        userinfo[i][4]=ExcelUntil.excel_data_to_list(userinfo[i][4])
    return userinfo
    
def admin_thread():

    clientList1=setUserInfo1()
           
    print 'starting at:', time.ctime() 

    threads = [] 
  
    for i in range(0,len(clientList1)):  # create all threads 
       
        t = threading.Thread(target=clientRun,args=(Akm_HOST,clientList1[i][1],clientList1[i][2],clientList1[i][3],clientList1[i][4]))        
#        t = threading.Thread(target=clientRun,args=(Qkm_HOST,UserName,UserTyp,KeyID))
        threads.append(t) 
          
    for i in range(0,len(clientList1)):  # start all threads 
        threads[i].start() 
  
    for i in range(0,len(clientList1)):  # wait for completion 
        threads[i].join() 
  
    print 'all DONE at:', time.ctime()   
#
##�ͻ��˽����ȴ��������������ͱ���    
def clientRun(host_ip,user_name1,user_typ1,key_id1,authid1):
#    print '---clientRun----key_id:',key_id
#    print '---clientRun----authid:',authid
    print 'start loop', user_name1, 'at:', time.ctime() 
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
    admin_packet=adminPacket.AdminPacket(user_name1,user_typ1,key_id1)
    #����socket������֤
    if admin_packet.admin(s,authid1)==1:
       k=k+1
        
    ack_key=admin_packet.get_sess_key()
    ack_key_id=admin_packet.get_sess_key_id()
    
#    qkm.getQkmKey(Qkm_HOST,user_name1,user_typ1,key_id1,authid1)#接入认证、获取量子密钥

#    time.sleep(50)
#    qkmApply.qkmapply(s,ack_key,ack_key_id,user_name) 
#    if qkmGet.qkmget(s,ack_key,ack_key_id,user_name)==1:
#       d=d+1   
#   ' akm.obtAkmKey(Akm_HOST,user_name1, user_typ1,key_id1,akm.getAkmKey(Akm_HOST,user_name2,user_typ2,key_id2))'
    
#    key_id_list = akm.getAkmKey(Akm_HOST,user_name1,user_typ1,key_id1,authid1)
    key_id_list = akm.getAkmKey(s,ack_key,ack_key_id,user_name1)
#    key_id_list = [5, 151, 53, 42, 206, 212, 74, 56, 159, 126, 178, 159, 212, 46, 10, 33]
    
    
#    if akm.obtAkmKey(s,ack_key,ack_key_id,user_name1,key_id_list)==1:
#        d=d+1
#    akm.obtAkmKey(s,ack_key,ack_key_id,user_name1,akm.getAkmKey(s,ack_key,ack_key_id,user_name1))
    
if __name__ == '__main__':
#    attend_num=UserNum 
#    clientList=setUserInfo() 
    admin_thread()
    print '----totalclient----',k
#    print '----totalget----',d


    
        