#!/usr/bin/python
# -*- coding: utf8 -*-
'''
Created on 2017-7-24
@author: qih
Project:sql数据批量导入
'''
import random
import unittest
#from clientTest import ClientAES1

#from gensysATest import main
#from ApplicationKey import main1

#import ClientAES1
import MySQLdb
from commonUntils import ExcelUntil
from commonUntils import DBConnection

#from clientTest import ClientAES2
#from clientTest import akmAccess

import ConfigParser


import os,os.path    
import string,base64  
def main():  
#    f=open("inserData.sql",'w')  
    cf = ConfigParser.ConfigParser()
    cf.read('D:/workplace/PyTest-frame/qtec.conf')  
    conn = MySQLdb.connect(host=eval(cf.get('db2', 'host')),user=eval(cf.get('db2', 'user')),passwd=eval(cf.get('db2', 'passwd')),db=eval(cf.get('db2', 'db')),port=eval(cf.get('db2', 'port')),charset='utf8')
    cur = conn.cursor()
    hero = DBConnection.DBConn(eval(cf.get('db2', 'db')),conn,cur)
    i=67101
    while i<67178:
        str1 = str(i)
       # strI2 = strI[4:]
        #sql = "INSERT INTO `qkey_authentication_info` VALUES ('" + str1 + "', “ + ” '333133373706“ + str1 + ”' , " + " 0xCF998982A53D5CB98C34D02A32AE9E16305256D4BDD843DE0181EE8266CC17FA, " + " 0x6A42FA2A53547E0157640E7D305726688BB32516E495185A73F05F3BC67C1846, " + " '2', " + " '1', " + " 'w', " + " '', " + " '1.0', " + " 0x9B892C3C1198CA3F1672E64B0156CC632504380202FD063623D508162EB3FA67, " + " '18814809235', " + " '18814809235', " + " 0x7C97073376960B537EC5D965332C " + str1 + ", " + " '1', " + " '0', " + " '0');"
        sql = "INSERT INTO `qkey_authentication_info` VALUES ('" + str1 + "', " + " '33313337370" + str1 + "' , " + "  0x20A8961D6687D6B6F4576CFE84DA426E5BA015B5135FE0D273470B14D91FEE71, " + " 0xD9FC5A10B5B388600286A27166011F402C879332B3373241C32FB45440373651, " + " '2', " + " '1', " + " 'w', " + " '', " + " '1.0', " + " 0x6451955DE04E89401AAB3B07FD51587BE0D035098974FF5C23C0682280F0216E, " + " '18814809235', " + " '18814809235', " + " 0x5D478713F2E7C71CA5AF1723AFA" + str1 + ", " + " '1', " + " '0', " + " '0');"
        #sql = "INSERT INTO `qkey_authentication_info` VALUES ('" + str1 + "', " + " '5a313538300" + str1 + "' , " + " 0x90E39D52F01511F790D5A8F416EF1456A9B517A62F5F0649711C7295055F2260, " + " 0x9B65360C2E28766BF30633354B809F15D2F4FF65AA0FAD02991DDE6D2D10573B, " + " '2', " + " '1', " + " 'w', " + " '', " + " '1.0', " + " 0x844CBF0B0113BA37523FD7251185824E4554AC2B11D40A6CEC7C45421EE7351B, " + " '18814809235', " + " '18814809235', " + " 0x667698498A507E4BCC9D160580C" + str1 + ", " + " '1', " + " '0', " + " '0');"
       # sql = "INSERT INTO `qkey_authentication_info` VALUES ('" + str1 + "', " + " '5a313538300" + str1 + "' , " + " 0x90E39D52F01511F790D5A8F416EF1456A9B517A62F5F0649711C7295055F2260, " + " 0x9B65360C2E28766BF30633354B809F15D2F4FF65AA0FAD02991DDE6D2D10573B, " + " '2', " + " '1', " + " 'w', " + " '', " + " '1.0', " + " 0xFCFF0D5975FDFE5B705495282B69F80741285C316B9C63577D8B697204C6D00E, " + " '18814809235', " + " '18814809235', " + " 0x667698498A507E4BCC9D160580C" + str1 + ", " + " '1', " + " '0', " + " '0');"

        #sql = "INSERT INTO `authentication_info` VALUES (''3331333737062635'+"'," + "0xCF998982A53D5CB98C34D02A32AE9E16305256D4BDD843DE0181EE8266CC17FA" +  "'," + "'0x6A42FA2A53547E0157640E7D305726688BB32516E495185A73F05F3BC67C1846"  + "'," + "'2" +  "','" + "1','" + "w'," + " " +  "," + '1.0,' + '0x9B892C3C1198CA3F1672E64B0156CC632504380202FD063623D508162EB3FA67' +  "," + '18814809235,' + '18814809235' +  "," + '0x7C97073376960B537EC5D965332C4'+ strI + ","+'1'+"," + '0'+ "," +'0);"
        #sql = "INSERT INTO `authentication_info` VALUES ('" + strI + "'," + "'client_test4" + strI2 + "'," + "'client_qh" + strI2 + "'," + "'client_qh" + strI2 + "','" + "1','" + "091945003b065c0d0a42'," + "0x0101010101010101010101010" + strI + "," + "0x6677206465643565672772622B3E3565652D6532686064605F5F60652B742B68," + "0x0101010101010101010101010" + strI + "," + "0x6677206465643565672772622B3E3565652D6532686064605F5F60652B742B68," + "0x0101010101010101010101010" + strI + "," + "0x6677206465643565672772622B3E3565652D6532686064605F5F60652B742B68"+ "," +"0);"
#        sql = "INSERT INTO `authentication_info` VALUES ('" + strI + "'," + "'client_ligg" + strI2 + "'," + "'client_ligg" + strI2 + "'," + "'client_ligg" + strI2 + "','" + "1','" + "091945003b065c0d0a42'," + "0x3665353933306632646538313" + strI + "," + "0x3032613763383238653738323432623439306662383762383031346130383438," + "0x3665353933306632646538313" + strI + "," + "0x3032613763383238653738323432623439306662383762383031346130383438," + "0x3665353933306632646538313" + strI + "," + "0x3032613763383238653738323432623439306662383762383031346130383438"+ "," +"0);"
      #  hero.insert(sql)
        print sql
        i=i+1
      
if __name__=='__main__':    
    main()
        
#cf = ConfigParser.ConfigParser()
#cf.read('D:/workplace/PyTest-frame/qtec.conf')  
#conn = MySQLdb.connect(host=eval(cf.get('db1', 'host')),user=eval(cf.get('db1', 'user')),passwd=eval(cf.get('db1', 'passwd')),db=eval(cf.get('db1', 'db')),port=eval(cf.get('db1', 'port')),charset='utf8')
#cur = conn.cursor()
#hero = DBConnection.DBConn(eval(cf.get('db1', 'db')),conn,cur)
#hero.insert("INSERT INTO `authentication_info` VALUES ('7000004', 'client_qh001', 'client_qh001', 'client_qh001', '1', '091945003b065c0d0a42', 0x01010101010101010101010101070104, 0x6677206465643565672772622B3E3565652D6532686064605F5F60652B742B68, 0x01010101010101010101010101010101, 0x6677206465643565672772622B3E3565652D6532686064605F5F60652B742B68, 0x01010101010101010101010101010101, 0x6677206465643565672772622B3E3565652D6532686064605F5F60652B742B68);")