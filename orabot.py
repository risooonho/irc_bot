#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This code was written for Python 3.1.1

import socket, sys, multiprocessing, time
import os
import re
from datetime import date
import sqlite3
import hashlib
import random
import pywapi
import urllib.request
import imp

import commands
import admin_commands

# root admin
root_admin = "ihptru"
root_admin_password = "password" #only for the successful first run, dont forget to remove it later

### UNCOMMENT BELOW ON THE FIRST RUN
#conn = sqlite3.connect('db/openra.sqlite')
#cur = conn.cursor()
#sql = """CREATE TABLE register (
#uid int NOT NULL,
#user varchar(20) NOT NULL,
#pass varchar(50),
#owner boolean NOT NULL DEFAULT '0',
#authenticated boolean NOT NULL DEFAULT '0'
#)
#"""
#cur.execute(sql)
#conn.commit()
#
#user_password = hashlib.md5(root_admin_password.encode('utf-8')).hexdigest()     
#sql = """INSERT INTO register
#        (uid,user,pass,owner)
#        VALUES
#        (
#        1,'"""+root_admin+"','"+str(user_password)+"'"+""",1
#        )       
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE black_list (
#    uid integer NOT NULL,
#    user varchar(30) NOT NULL,
#    date_time date NOT NULL,
#    count integer NOT NULL
#    )        
#"""
#cur.execute(sql)
#conn.commit()
#sql = """INSERT INTO black_list
#       (uid,user,date_time,count)
#       VALUES
#       (
#       1,'test',strftime('%Y-%m-%d-%H-%M'),1
#       )
#"""
#cur.execute(sql)
#conn.commit()
#
#sql = """CREATE TABLE commands (
#        uid integer NOT NULL,
#        user varchar(30) NOT NULL,
#        command varchar(300) NOT NULL,
#        date_time date NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#for i in range(31):
#    sql = """INSERT INTO commands
#        (uid,user,command,date_time)
#        VALUES
#        (
#        1,'test','test_command',strftime('%Y-%m-%d-%H-%M-%S')
#        )
#    """
#    cur.execute(sql)
#    conn.commit()
#sql = """CREATE TABLE users (
#uid integer NOT NULL,
#user varchar(30) NOT NULL,
#date date
#)               
#"""
#cur.execute(sql)
#conn.commit()
#sql= """INSERT INTO users
#        (uid,user)
#        VALUES
#        (
#        1,'test'
#        )
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE later (
#        uid integer NOT NULL,
#        sender varchar(30) NOT NULL,
#        reciever varchar(30) NOT NULL,
#        channel varchar(30) NOT NULL,
#        date date NOT NULL,
#        message varchar(1000) NOT NULL
#)             
#"""
#cur.execute(sql)
#conn.commit()
#sql = """INSERT INTO later
#        (uid,sender,reciever,channel,date,message)
#        VALUES
#        (
#        1,'test','test','#test',strftime('%Y-%m-%d-%H-%M-%S'),'Hello, how are you?'
#        )                
#"""
#cur.execute(sql)
#conn.commit()
###
#sql = """CREATE TABLE "pickup_1v1" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"host" BOOL NOT NULL  DEFAULT 0,
#"timeout" DATETIME NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_2v2" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"host" BOOL NOT NULL  DEFAULT 0,
#"timeout" DATETIME NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_3v3" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"host" BOOL NOT NULL  DEFAULT 0,
#"timeout" DATETIME NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_4v4 (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"host" BOOL NOT NULL  DEFAULT 0,
#"timeout" DATETIME NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_5v5" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"host" BOOL NOT NULL  DEFAULT 0,
#"timeout" DATETIME NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_game_start" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"team1" VARCHAR NOT NULL ,
#"team2" VARCHAR NOT NULL ,
#"type" VARCHAR NOT NULL ,
#"host" VARCHAR NOT NULL ,
#"map" VARCHAR NOT NULL ,
#"time" DATETIME NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_maps" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"1v1" BOOL NOT NULL ,
#"2v2" BOOL NOT NULL ,
#"3v3" BOOL NOT NULL ,
#"4v4" BOOL NOT NULL ,
#"5v5" BOOL NOT NULL
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """INSERT INTO "pickup_maps"
#       (name,1v1,2v2,3v3,4v4,5v5)
#       VALUES
#       (
#       'East vs West',1,1,0,0,0
#       )
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "pickup_stats" (
#"uid" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
#"name" VARCHAR NOT NULL ,
#"games" INTEGER NOT NULL  DEFAULT 0,
#"hosts" INTEGER NOT NULL  DEFAULT 0,
#"complaints" INTEGER NOT NULL  DEFAULT 0
#)
#"""
#cur.execute(sql)
#conn.commit()
#sql = """CREATE TABLE "notify" (
#uid INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE,
#user VARCHAR NOT NULL,
#date DATETIME NOT NULL,
#mod VARCHAR NOT NULL DEFAULT "all",
#version VARCHAR NOT NULL DEFAULT "all",
#timeout VARCHAR NOT NULL DEFAULT "all",
#timezone VARCHAR NOT NULL DEFAULT "GMT"
#)                
#"""
#cur.execute(sql)
#conn.commit()
#cur.close()
###

languages=['af','sq','ar','be','bg','ca','zh-CN','hr','cs','da','nl','en','et','tl','fi','fr','gl','de','el','iw','hi','hu','is','id','ga','it','ja','ko','lv','lt','mk','ml','mt','no','fa','pl','ro','ru','sr','sk','sl','es','sw','sv','th','tr','uk','vi','cy','yi']
real_langs=['Afrikaans','Albanian','Arabic','Belarusian','Bulgarian','Catalan','Chinese_Simplified','Croatian','Czech','Danish','Dutch','English','Estonian','Filipino','Finnish','French','Galician','German','Greek','Hebrew','Hindi','Hungarian','Icelandic','Indonesian','Irish','Italian','Japanese','Korean','Latvian','Lithuanian','Macedonian','Malay','Maltese','Norwegian','Persian','Polish','Romanian','Russian','Serbian','Slovak','Slovenian','Spanish','Swahili','Swedish','Thai','Turkish','Ukrainian','Vietnamese','Welsh','Yiddish']
codes=['AF','AX','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BQ','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CW','CY','CZ','DK','DJ','DM','DO','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GG','GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IM','IL','IT','JM','JP','JE','JO','KZ','KE','KI','KP','KR','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','ME','MS','MA','MZ','MM','NA','NR','NP','NL','NC','NZ','NI','NE','NG','NU','NF','MP','NO','OM','PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RU','RW','BL','SH','KN','LC','MF','PM','VC','WS','SM','ST','SA','SN','RS','SC','SL','SG','SX','SK','SI','SB','SO','ZA','GS','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','GB','US','UM','UY','UZ','VU','VE','VN','VG','VI','WF','EH','YE','ZM','ZW']
match_codes=['AFGHANISTAN','ALAND ISLANDS','ALBANIA','ALGERIA','AMERICAN SAMOA','ANDORRA','ANGOLA','ANGUILLA','ANTARCTICA','ANTIGUA and BARBUDA','ARGENTINA','ARMENIA','ARUBA','AUSTRALIA','AUSTRIA','AZERBAIJAN','BAHAMAS','BAHRAIN','BANGLADESH','BARBADOS','BELARUS','BELGIUM','BELIZE','BENIN','BERMUDA','BHUTAN','BOLIVIA, PLURINATIONAL STATE OF','BONAIRE, SAINT EUSTATIUS and SABA','BOSNIA and HERZEGOVINA','BOTSWANA','BOUVET ISLAND','BRAZIL','BRITISH INDIAN OCEAN TERRITORY','BRUNEI DARUSSALAM','BULGARIA','BURKINA FASO','BURUNDI','CAMBODIA','CAMEROON','CANADA','CAPE VERDE','CAYMAN ISLANDS','CENTRAL AFRICAN REPUBLIC','CHAD','CHILE','CHINA','CHRISTMAS ISLAND','COCOS (KEELING) ISLANDS','COLOMBIA','COMOROS','CONGO','CONGO, THE DEMOCRATIC REPUBLIC OF THE','COOK ISLANDS','COSTA RICA',"COTE D'IVOIRE",'CROATIA','CUBA','CURACAO','CYPRUS','CZECH REPUBLIC','DENMARK','DJIBOUTI','DOMINICA','DOMINICAN REPUBLIC','ECUADOR','EGYPT','EL SALVADOR','EQUATORIAL GUINEA','ERITREA','ESTONIA','ETHIOPIA','FALKLAND ISLANDS (MALVINAS)','FAROE ISLANDS','FIJI','FINLAND','FRANCE','FRENCH GUIANA','FRENCH POLYNESIA','FRENCH SOUTHERN TERRITORIES','GABON','GAMBIA','GEORGIA','GERMANY','GHANA','GIBRALTAR','GREECE','GREENLAND','GRENADA','GUADELOUPE','GUAM','GUATEMALA','GUERNSEY','GUINEA','GUINEA-BISSAU','GUYANA','HAITI','HEARD ISLAND AND MCDONALD ISLANDS','HOLY SEE (VATICAN CITY STATE)','HONDURAS','HONG KONG','HUNGARY','ICELAND','INDIA','INDONESIA','IRAN, ISLAMIC REPUBLIC OF','IRAQ','IRELAND','ISLE OF MAN','ISRAEL','ITALY','JAMAICA','JAPAN','JERSEY','JORDAN','KAZAKHSTAN','KENYA','KIRIBATI',"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",'KOREA, REPUBLIC OF','KUWAIT','KYRGYZSTAN',"LAO PEOPLE'S DEMOCRATIC REPUBLIC",'LATVIA','LEBANON','LESOTHO','LIBERIA','LIBYAN ARAB JAMAHIRIYA','LIECHTENSTEIN','LITHUANIA','LUXEMBOURG','MACAO','MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF','MADAGASCAR','MALAWI','MALAYSIA','MALDIVES','MALI','MALTA','MARSHALL ISLANDS','MARTINIQUE','MAURITANIA','MAURITIUS','MAYOTTE','MEXICO','MICRONESIA, FEDERATED STATES OF','MOLDOVA, REPUBLIC OF','MONACO','MONGOLIA','MONTENEGRO','MONTSERRAT','MOROCCO','MOZAMBIQUE','MYANMAR','NAMIBIA','NAURU','NEPAL','NETHERLANDS','NEW CALEDONIA','NEW ZEALAND','NICARAGUA','NIGER','NIGERIA','NIUE','NORFOLK ISLAND','NORTHERN MARIANA ISLANDS','NORWAY','OMAN','PAKISTAN','PALAU','PALESTINIAN TERRITORY, OCCUPIED','PANAMA','PAPUA NEW GUINEA','PARAGUAY','PERU','PHILIPPINES','PITCAIRN','POLAND','PORTUGAL','PUERTO RICO','QATAR','REUNION','ROMANIA','RUSSIAN FEDERATION','RWANDA','SAINT BARTHELEMY','SAINT HELENA, ASCENSION and TRISTAN DA CUNHA','SAINT KITTS and NEVIS','SAINT LUCIA','SAINT MARTIN (FRENCH PART)','SAINT PIERRE and MIQUELON','SAINT VINCENT and THE GRENADINES','SAMOA','SAN MARINO','SAO TOME and PRINCIPE','SAUDI ARABIA','SENEGAL','SERBIA','SEYCHELLES','SIERRA LEONE','SINGAPORE','SINT MAARTEN (DUTCH PART)','SLOVAKIA','SLOVENIA','SOLOMON ISLANDS','SOMALIA','SOUTH AFRICA','SOUTH GEORGIA and THE SOUTH SANDWICH ISLANDS','SPAIN','SRI LANKA','SUDAN','SURINAME','SVALBARD and JAN MAYEN','SWAZILAND','SWEDEN','SWITZERLAND','SYRIAN ARAB REPUBLIC','TAIWAN, PROVINCE OF CHINA','TAJIKISTAN','TANZANIA, UNITED REPUBLIC OF','THAILAND','TIMOR-LESTE','TOGO','TOKELAU','TONGA','TRINIDAD and TOBAGO','TUNISIA','TURKEY','TURKMENISTAN','TURKS and CAICOS ISLANDS','TUVALU','UGANDA','UKRAINE','UNITED ARAB EMIRATES','UNITED KINGDOM','UNITED STATES','NITED STATES MINOR OUTLYING ISLANDS','URUGUAY','UZBEKISTAN','VANUATU','VENEZUELA, BOLIVARIAN REPUBLIC OF','VIET NAM','VIRGIN ISLANDS, BRITISH','VIRGIN ISLANDS, U.S.','WALLIS and FUTUNA','WESTERN SAHARA','YEMEN','ZAMBIA','ZIMBABWE']
notify_ip_list = []

# Defining a class to run the server. One per connection. This class will do most of our work.
class IRC_Server:

    # The default constructor - declaring our global variables
    # channel should be rewritten to be a list, which then loops to connect, per channel.
    # This needs to support an alternate nick.
    def __init__(self, host, port, nick, channel , password =""):
        self.irc_host = host
        self.irc_port = port
        self.irc_nick = nick
        self.irc_channel = channel
        self.irc_sock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        self.is_connected = False
        self.should_reconnect = False
        self.command = ""
        

    ## The destructor - Close socket.
    def __del__(self):
        self.irc_sock.close()

    # This is the bit that controls connection to a server & channel.
    # It should be rewritten to allow multiple channels in a single server.
    # This needs to have an "auto identify" as part of its script, or support a custom connect message.       
    def connect(self):
        self.should_reconnect = True
        try:
            self.irc_sock.connect ((self.irc_host, self.irc_port))
        except:
            print ("Error: Could not connect to IRC; Host: " + str(self.irc_host) + "Port: " + str(self.irc_port))
            exit(1) # We should make it recconect if it gets an error here
        print ("Connected to: " + str(self.irc_host) + ":" + str(self.irc_port))

        str_buff = ("NICK %s \r\n") % (self.irc_nick)
        self.irc_sock.send (str_buff.encode())
        print ("Setting bot nick to " + str(self.irc_nick) )

        str_buff = ("USER %s 8 * :X\r\n") % (self.irc_nick)
        self.irc_sock.send (str_buff.encode())
        print ("Setting User")
        # Insert Alternate nick code here.

        # Insert Auto-Identify code here.

        str_buff = ( "JOIN %s \r\n" ) % (self.irc_channel)
        self.irc_sock.send (str_buff.encode())
        print ("Joining channel " + str(self.irc_channel) )
        self.is_connected = True
        self.listen()
        
    def listen(self):
        while self.is_connected:
            recv = self.irc_sock.recv( 4096 )
            ### for logs
            a = date.today()
            a = str(a)
            a = a.split('-')
            year = a[0]
            month = a[1]
            day = a[2]
            b = time.localtime()
            b = str(b)
            hours = b.split('tm_hour=')[1].split(',')[0]
            minutes = b.split('tm_min=')[1].split(',')[0]
            if len(hours) == 1:
                real_hours = '0'+hours
            else:
                real_hours = hours
            if len(minutes) == 1:
                real_minutes = '0'+minutes
            else:
                real_minutes = minutes
            ### for logs end
            if str(recv).find ( "PING" ) != -1:
                self.irc_sock.send ( "PONG ".encode() + recv.split() [ 1 ] + "\r\n".encode() )             
             
            #recover all nicks on channel
            #if str(recv).find ( "353 orabot =" ) != -1:
            #    print (str(recv))
            #    user_nicks = str(recv).split(':')[2].rstrip()
            #    user_nicks = user_nicks.replace('+','').replace('@','')
            #    user_nicks = user_nicks.split(' ')
            #    self.nicks = user_nicks
            if str(recv).find ( "PRIVMSG" ) != -1:
                irc_user_nick = str(recv).split ( '!' ) [ 0 ] . split ( ":")[1]
                irc_user_host = str(recv).split ( '@' ) [ 1 ] . split ( ' ' ) [ 0 ]
                irc_user_message = self.data_to_message(str(recv))
                # if PRIVMSG is still in string - message from person with ipv6
                suit = re.compile('PRIVMSG')
                if suit.search(irc_user_message):
                    irc_user_message = str(recv).split ( 'PRIVMSG' ) [ 1 ] . split ( ' :') [ 1: ]
                    irc_user_message = " ".join(irc_user_message)
                    irc_user_message = irc_user_message[:-5]
                ###logs
                chan = str(recv).split ( 'PRIVMSG' ) [ 1 ] . lstrip() . split(' :')[0]  #channel ex: #openra
                if self.irc_channel == '#openra' or self.irc_channel == '#openra-dev':
                    row = '['+real_hours+':'+real_minutes+'] '+irc_user_nick+': '+str(irc_user_message)+'\n'
                    if self.irc_channel == '#openra':
                        chan_d = 'openra'
                    elif self.irc_channel == '#openra-dev':
                        chan_d = 'openra-dev'
                    else:
                        chan_d = 'trash'
                    filename = '/var/openra/irc/logs/'+chan_d+'/'+year+'/'+month+'/'+day
                    dir = os.path.dirname(filename)
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    file = open(filename,'a')
                    file.write(row)
                    file.close()
                ### logs end
                print ( irc_user_nick + ": " + irc_user_message)
                # "]" Indicated a command
                if ( str(irc_user_message[0]) == "]" ):
                    self.command = str(irc_user_message[1:])
                    # (str(recv)).split()[2] ) is simply the channel the command was heard on.
                    self.process_command(irc_user_nick, ( (str(recv)).split()[2] ))
### when message cotains link, show title
                if re.search('.*http.*://.*', str(irc_user_message)):
                    link = str(irc_user_message).split('://')[1].split()[0]
                    pre = str(irc_user_message).split('http')[1].split('//')[0]
                    link = 'http'+pre+'//'+link
                    if re.search('http.*youtube.com/watch.*', link):
                        if re.search("^#", chan):
                            link = link.split('&')[0]
                            try:
                                site = urllib.request.urlopen(link)
                                site = site.read()
                                site = site.decode('utf-8')
                                title = site.split('<title>')[1].split('</title>')[0].split('&#x202c;')[0].split('&#x202a;')[1].replace('&amp;','&').replace('&#39;', '\'').rstrip().lstrip()
                                if ( title != 'YouTube - Broadcast Yourself.' ):    #video exists
                                    self.send_message_to_channel( ("Youtube: "+title), chan )
                            except:
                                pass
                    else:
                        if re.search("^#", chan):
                            try:
                                site = urllib.request.urlopen(link)
                                site = site.read()
                                site = site.decode('utf-8')
                                title = site.split('<title>')[1].split('</title>')[0].rstrip().lstrip()
                                self.send_message_to_channel( ("Title: "+title), chan )
                            except:
                                pass
                        
###
            if str(recv).find ( "JOIN" ) != -1:
                conn = sqlite3.connect('../db/openra.sqlite')   # connect to database
                cur=conn.cursor()
                print (str(recv))
                irc_join_nick = str(recv).split( '!' ) [ 0 ].split( ':' ) [ 1 ]
                irc_join_host = str(recv).split( '!' ) [ 1 ].split( ' ' ) [ 0 ]
                #chan = str(recv).split( "JOIN" ) [ 1 ].lstrip().split( ":" )[1].rstrip()     #channle ex: #openra
                #chan = str(recv).split()[2].replace(':','').rstrip()
                sql = """SELECT * FROM users
                        WHERE user = '"""+irc_join_nick+"'"+"""
                """
                cur.execute(sql)
                conn.commit()
                row = []
                for row in cur:
                    pass
                if irc_join_nick not in row:     #user NOT found, add him (if user is not in db, he could not have ]later message)
                    #get last uid
                    sql = """SELECT * FROM users
                            ORDER BY uid DESC LIMIT 1
                    """
                    cur.execute(sql)
                    conn.commit()
                    row = []
                    for row in cur:
                        pass
                    uid_users = row[0]
                    uid_users = uid_users + 1   # uid + 1
                    sql = """INSERT INTO users
                            (uid,user)
                            VALUES
                            (
                            """+str(uid_users)+",'"+str(irc_join_nick)+"'"+"""
                            )
                    """
                    cur.execute(sql)
                    conn.commit()
                else:   #he can have ]later messages
                    sql = """SELECT reciever FROM later
                            WHERE reciever = '"""+irc_join_nick+"'"+"""
                    """
                    cur.execute(sql)
                    conn.commit()

                    row = []
                    for row in cur:
                        pass
                    if irc_join_nick in row:    #he has messages in database, read it
                        sql = """SELECT * FROM later
                                WHERE reciever = '"""+irc_join_nick+"'"+"""
                        """
                        cur.execute(sql)
                        conn.commit()
                        row = []
                        msgs = []
                        for row in cur:
                            msgs.append(row)
                        msgs_length = len(msgs) #number of messages for player
                        self.send_message_to_channel( ("You have "+str(msgs_length)+" offline messages:"), irc_join_nick )
                        for i in range(int(msgs_length)):
                            who_sent = msgs[i][1]
                            on_channel = msgs[i][3]
                            message_date = msgs[i][4]
                            offline_message = msgs[i][5]
                            self.send_message_to_channel( ("### From: "+who_sent+";  channel: "+on_channel+";  date: "+message_date), irc_join_nick )
                            self.send_message_to_channel( (offline_message.replace("~qq~","'")), irc_join_nick )
                        time.sleep(0.1)
                        sql = """DELETE FROM later
                                WHERE reciever = '"""+irc_join_nick+"'"+"""
                        
                        """
                        
                        cur.execute(sql)
                        conn.commit()
                    sql = """UPDATE users
                            SET date = ''
                            WHERE user = '"""+irc_join_nick+"'"+"""
                    """
                    cur.execute(sql)
                    conn.commit()
                    cur.close()
                ###logs
                if self.irc_channel == '#openra' or self.irc_channel == '#openra-dev':
                    row = '['+real_hours+':'+real_minutes+'] '+'* '+irc_join_nick+' ('+irc_join_host+') has joined '+self.irc_channel+'\n'
                    if self.irc_channel == '#openra':
                        chan_d = 'openra'
                    elif self.irc_channel == '#openra-dev':
                        chan_d = 'openra-dev'
                    else:
                        chan_d = 'trash'
                    filename = '/var/openra/irc/logs/'+chan_d+'/'+year+'/'+month+'/'+day
                    dir = os.path.dirname(filename)
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    file = open(filename,'a')
                    file.write(row)
                    file.close()
                ###
            if str(recv).find ( "QUIT" ) != -1:
                conn = sqlite3.connect('../db/openra.sqlite')   # connect to database
                cur=conn.cursor()
                print (str(recv))
                irc_quit_nick = str(recv).split( "!" )[ 0 ].split( ":" ) [ 1 ]
                irc_quit_message = str(recv).split('QUIT :')[1].rstrip()
                #change authenticated status
                sql = """SELECT * FROM register
                        WHERE user = '"""+irc_quit_nick+"'"+"""
                """
                cur.execute(sql)
                conn.commit()
                row = []
                for row in cur:
                    pass
                if irc_quit_nick in row:
                    authenticated = row[4]
                    if authenticated == 1:
                        sql = """UPDATE register
                                SET authenticated = 0
                                WHERE user = '"""+irc_quit_nick+"'"+"""
                        """
                        cur.execute(sql)
                        conn.commit()
                ### for ]last              
                sql = """UPDATE users
                        SET date = strftime('%Y-%m-%d-%H-%M-%S')
                        WHERE user = '"""+str(irc_quit_nick)+"'"+"""
                """
                cur.execute(sql)
                conn.commit()
                cur.close()
                ### for ]pick
                modes = ['1v1','2v2','3v3','4v4']
                diff_mode = ''
                for diff_mode in modes:
                    sql = """DELETE FROM pickup_"""+diff_mode+"""
                            WHERE name = '"""+irc_quit_nick+"""'
                    """
                    cur.execute(sql)
                    conn.commit()
                ##logs
                if self.irc_channel == '#openra' or self.irc_channel == '#openra-dev':
                    row = '['+real_hours+':'+real_minutes+'] '+'* '+irc_quit_nick+' has quit ('+irc_quit_message.rstrip()+')\n'
                    if self.irc_channel == '#openra':
                        chan_d = 'openra'
                    elif self.irc_channel == '#openra-dev':
                        chan_d = 'openra-dev'
                    else:
                        chan_d = 'trash'
                    filename = '/var/openra/irc/logs/'+chan_d+'/'+year+'/'+month+'/'+day
                    dir = os.path.dirname(filename)
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    file = open(filename,'a')
                    file.write(row)
                    file.close()
            if str(recv).find ( "PART" ) != -1:
                conn = sqlite3.connect('../db/openra.sqlite')   # connect to database
                cur=conn.cursor()
                print (str(recv))
                irc_part_nick = str(recv).split( "!" )[ 0 ].split( ":" ) [ 1 ]
                #chan = str(recv).split()[2].replace(':','')
                ###logout
                sql = """SELECT * FROM register
                        WHERE user = '"""+irc_part_nick+"'"+"""
                """
                cur.execute(sql)
                conn.commit()
                row = []
                for row in cur:
                    pass
                if irc_part_nick in row:
                    authenticated = row[4]
                    if authenticated == 1:
                        sql = """UPDATE register
                                SET authenticated = 0
                                WHERE user = '"""+irc_part_nick+"'"+"""
                        """
                        cur.execute(sql)
                        conn.commit()
                ### for ]last              
                sql = """UPDATE users
                        SET date = strftime('%Y-%m-%d-%H-%M-%S')
                        WHERE user = '"""+str(irc_part_nick)+"'"+"""
                """
                cur.execute(sql)
                conn.commit()
                cur.close()
                ### for ]pick
                modes = ['1v1','2v2','3v3','4v4']
                diff_mode = ''
                for diff_mode in modes:
                    sql = """DELETE FROM pickup_"""+diff_mode+"""
                            WHERE name = '"""+irc_part_nick+"""'
                    """
                    cur.execute(sql)
                    conn.commit()
                ###logs
                if self.irc_channel == '#openra' or self.irc_channel == '#openra-dev':
                    row = '['+real_hours+':'+real_minutes+'] '+'* '+irc_part_nick+' has left '+self.irc_channel+'\n'
                    if self.irc_channel == '#openra':
                        chan_d = 'openra'
                    elif self.irc_channel == '#openra-dev':
                        chan_d = 'openra-dev'
                    else:
                        chan_d = 'trash'
                    filename = '/var/openra/irc/logs/'+chan_d+'/'+year+'/'+month+'/'+day
                    dir = os.path.dirname(filename)
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                    file = open(filename,'a')
                    file.write(row)
                    file.close()
                ###

        if self.should_reconnect:
            self.connect()

    def data_to_message(self,data):
        data = data[data.find(':')+1:len(data)]
        data = data[data.find(':')+1:len(data)]
        data = str(data[0:len(data)-5])
        return data

    # This function sends a message to a channel, which must start with a #.
    def send_message_to_channel(self,data,channel):
        print ( ( "%s: %s") % (self.irc_nick, data) )
        self.irc_sock.send( (("PRIVMSG %s :%s\r\n") % (channel, data)).encode() )
        ### for logs
        a = date.today()
        a = str(a)
        a = a.split('-')
        year = a[0]
        month = a[1]
        day = a[2]
        b = time.localtime()
        b = str(b)
        hours = b.split('tm_hour=')[1].split(',')[0]
        minutes = b.split('tm_min=')[1].split(',')[0]
        if len(hours) == 1:
            real_hours = '0'+hours
        else:
            real_hours = hours
        if len(minutes) == 1:
            real_minutes = '0'+minutes
        else:
            real_minutes = minutes
        if channel == '#openra' or channel == '#openra-dev':
            row = '['+real_hours+':'+real_minutes+'] '+self.irc_nick+': '+str(data)+'\n'
            if channel == '#openra':
                chan_d = 'openra'
            elif channel == '#openra-dev':
                chan_d = 'openra-dev'
            else:
                chan_d = 'trash'
            filename = '/var/openra/irc/logs/'+chan_d+'/'+year+'/'+month+'/'+day
            dir = os.path.dirname(filename)
            if not os.path.exists(dir):
                os.makedirs(dir)
            file = open(filename,'a')
            file.write(row)
            file.close()
        ### for logs end
    # This function takes a channel, which must start with a #.
    def join_channel(self,channel):
        if (channel[0] == "#"):
            str_buff = ( "JOIN %s \r\n" ) % (channel)
            self.irc_sock.send (str_buff.encode())
            # This needs to test if the channel is full
            # This needs to modify the list of active channels

    # This function takes a channel, which must start with a #.
    def quit_channel(self,channel):
        if (channel[0] == "#"):
            str_buff = ( "PART %s \r\n" ) % (channel)
            self.irc_sock.send (str_buff.encode())
            # This needs to modify the list of active channels
    
    def evalAdminCommand(self, commandname, user, channel, owner, authenticated):
        if hasattr(admin_commands, commandname): #Command exists
            imp.reload(admin_commands)
            command_function=getattr(admin_commands, commandname)
            command_function(self, user, channel, owner, authenticated)
            
    def evalCommand(self, commandname, user, channel):
        if hasattr(commands, commandname): #Command exists
            imp.reload(commands)
            command_function=getattr(commands, commandname)
            command_function(self, user, channel)
            
    def process_command(self, user, channel):
        # This line makes sure an actual command was sent, not a plain "!"
        if ( len(self.command.split()) == 0):
            error = "Usage: ]command [arguments]"
            if re.search("^#", channel):
                self.send_message_to_channel( (error), channel)
            else:
                self.send_message_to_channel( (error), user)
            return
        # So the command isn't case sensitive
        command = (self.command)
        # Break the command into pieces, so we can interpret it with arguments
        command = command.split()
        string_command = " ".join(command)

### START OF SPAM FILTER
        conn = sqlite3.connect('../db/openra.sqlite')   # connect to database
        cur=conn.cursor()
        sql = """SELECT * FROM black_list
            WHERE user = '"""+user+"'"+"""
        """
        cur.execute(sql)
        conn.commit()
        
        row = []
        for row in cur:
            pass
        check_ignore = '0'
        if user in row:
            ignore_count = row[3]
            ignore_minutes = str(ignore_count)+'0'
            ignore_date = "".join(str(row[2]).split('-'))
            a = date.today()
            a = str(a)
            a = a.split('-')
            year = a[0]
            month = a[1]
            day = a[2]
            b = time.localtime()
            b = str(b)
            hours = b.split('tm_hour=')[1].split(',')[0]
            minutes = b.split('tm_min=')[1].split(',')[0]
            if len(hours) == 1:
                hours = '0'+hours
            else:
                hours = hours
            if len(minutes) == 1:
                minutes = '0'+minutes
            else:
                minutes = minutes
            localtime = year+month+day+hours+minutes
            difference = int(localtime) - int(ignore_date)  #how many minutes after last ignore
            if int(difference) < int(ignore_minutes):
                check_ignore = '1'  #lock, start ignore
            else:   #no need to ignore, ignore_minutes < difference
                check_ignore = '0'
        if check_ignore == '0':
            #get last uid_commands
            sql = """SELECT * FROM commands
                    ORDER BY uid DESC LIMIT 1
            """
            cur.execute(sql)
            conn.commit()
            
            for row in cur:
                pass
            uid_commands=row[0]
            
            uid_commands = uid_commands + 1
            #clear 'commands' table after each 1 000 000 record
            if uid_commands >= 1000:
                uid_commands = 1
                sql = """DELETE FROM commands WHERE uid > 1"""
                cur.execute(sql)
                conn.commit()
    
            #write each command into 'commands' table 
            sql = """INSERT INTO commands
                    (uid,user,command,date_time)
                    VALUES
                    (
                    """+str(uid_commands)+",'"+str(user)+"','"+string_command.replace("'","~qq~")+"',"+"strftime('%Y-%m-%d-%H-%M-%S')"+""" 
                    )        
            """
            cur.execute(sql)
            conn.commit()
            
            #extract last 30 records
            sql = """SELECT * FROM commands
                ORDER BY uid DESC LIMIT 30
            """
            cur.execute(sql)
            
        
            var=[]
            for row in cur:
                var.append(row)
            var.reverse()
            actual=[]
            user_data=[]
            for i in range(30):
                if user in str(var[i][1]):
                    actual.append(str(var[i][1]))   #name
                    actual.append(str(var[i][3]))   #date and time
                    user_data.append(actual)
                    actual=[]
            user_data_length = len(user_data)
            if user_data_length > 10:
                #get player's (last - 10) record
                user_data_len10 = user_data_length - 10
                actual=user_data[user_data_len10]
                first_date="".join(actual[1].split('-'))    #date and time of last - 10 record
                last_date="".join(user_data[user_data_length-1][1].split('-'))  #current date/time
                seconds_range=int(last_date)-int(first_date)  #how many seconds between player's commands
                if seconds_range < 30:  #player made more then 10 commands in range of 30 seconds. It is too quick, spam!
                    sql = """SELECT * FROM black_list
                            WHERE user = '"""+user+"'"+"""
                    """
                    cur.execute(sql)
                    conn.commit()

                    row = []
                    for row in cur:
                        pass
                    if user not in row:   #user does not exist in 'black_list' table yet
                        #get last uid_black_list

                        sql = """SELECT * FROM black_list
                                ORDER BY uid DESC LIMIT 1
                        """
                        cur.execute(sql)
                        conn.commit()
       
                        for row in cur:
                            pass
                        uid_black_list=row[0]
                        uid_black_list = uid_black_list + 1
                        
                        sql = """INSERT INTO black_list
                            (uid,user,date_time,count)
                            VALUES
                            (
                            """+str(uid_black_list)+",'"+user+"',strftime('%Y-%m-%d-%H-%M'),"+str(1)+"""
                            )                   
                        """
                        cur.execute(sql)
                        conn.commit()
                    else:   #in row : exists in 'black_table'
                        count_ignore = row[3]
                        count_ignore = count_ignore + 1
                        sql = """UPDATE black_list
                                SET count = """+str(count_ignore)+", "+"""date_time = strftime('%Y-%m-%d-%H-%M')
                                WHERE user = '"""+user+"'"+""" 
                        """
                        cur.execute(sql)
                        conn.commit()
                    sql = """SELECT * FROM black_list
                        WHERE user = '"""+user+"'"+"""
                    """
                    cur.execute(sql)
                    conn.commit()

                    row = []
                    for row in cur:
                        pass
                    if user in row:
                        ignore_count = row[3]
                        ignore_minutes = str(ignore_count)+'0'
                        check_ignore = '1'  #lock, start ignore        
                        if re.search("^#", channel):
                            self.send_message_to_channel( (user+", your actions are counted as spam, I will ignore you for "+str(ignore_minutes)+" minutes"), channel )
                        else:
                            self.send_message_to_channel( (user+", your actions are counted as spam, I will ignore you for "+str(ignore_minutes)+" minutes"), user )
                        return
### END OF SPAM FILTER
############    COMMADS:
            ### check if user is registered for privileged commands
            sql = """SELECT * FROM register
                    WHERE user = '"""+user+"'"+"""
            """
            cur.execute(sql)
            conn.commit()
            row = []
            for row in cur:
                pass
            if user in row:     #user exists in 'register' table
                owner = row[3]
                authenticated = row[4]
                if (authenticated == 1):    #he is also authenticated           
                    ### All admin only commands go in here.
                    self.evalAdminCommand(command[0].lower(), user, channel, str(owner), str(authenticated))
                    
            cur.close()
                    
            ### All public commands go here
            self.evalCommand(command[0].lower(), user, channel)
#####
class BotCrashed(Exception): # Raised if the bot has crashed.
    pass

def main():
    # Here begins the main programs flow:
    test2 = IRC_Server("irc.freenode.net", 6667, "orabot", "#openra")
    test = IRC_Server("irc.freenode.net", 6667, "orabot", "#openra")
    run_test = multiprocessing.Process(None,test.connect,name="IRC Server" )
    run_test.start()
    
    def notification(self):
        while True:
            time.sleep(3)
### NOTIFICATIONS
            ip_current_games = []
            url = 'http://master.open-ra.org/list.php'
            stream = urllib.request.urlopen(url).read()
            if ( stream != b'' ):
                split_games = str(stream).split('\\nGame')
                length_games = len(split_games)
                for i in range(int(length_games)):
                    ip = split_games[i].split('\\n\\t')[3].split()[1].split(':')[0]
                    ip_current_games.append(ip)
                    state = split_games[i].split('\\n\\t')[4]
                    if ( ip in notify_ip_list ):
                        if ( state == 'State: 2' ):
                            #game in list but started, remove from `notify_ip_list`
                            ip_index = notify_ip_list.index(ip)
                            del notify_ip_list[ip_index]
                            ip_index = ip_current_games.index(ip)
                            del ip_current_games[ip_index]
                    else:   #ip is not in a list
                        if ( state == 'State: 1' ):
                            notify_ip_list.append(ip)
                            name = " ".join(split_games[i].split('\\n\\t')[2].split()[1:])
                            mod = split_games[i].split('\\n\\t')[7].split()[1].split('@')[0]
                            try:
                                version = " - version: " + split_games[i].split('\\n\\t')[7].split()[1].split('@')[1]
                            except:
                                version = ''    #no version in output
                            down = name.split('[down]')
                            if ( len(down) == 1 ):  #game is not [down]
                                conn = sqlite3.connect('../db/openra.sqlite')
                                cur = conn.cursor()
                                sql = """SELECT user,date,mod,version,timeout FROM notify
                                """
                                cur.execute(sql)
                                conn.commit()
                                row = []
                                data = []
                                for row in cur:
                                    data.append(row)
                                if ( data != [] ):
                                    length_data = len(data)
                                    for i in range(int(length_data)):
                                        db_user = data[i][0]
                                        db_date = data[i][1]
                                        db_mod = data[i][2]
                                        db_version = data[i][3]
                                        db_timeout = data[i][4]
                                        notify_message = "New game: "+name+" - mod: "+mod+version
                                        self.irc_sock.send( (("PRIVMSG %s :%s\r\n") % (db_user, notify_message)).encode() )
                length = len(notify_ip_list)
                indexes = []
                for i in range(int(length)):
                    if ( notify_ip_list[i] not in ip_current_games ):
                        indexes.append(i)   #indexes to remove from notify_ip_list
                for i in indexes:
                    del notify_ip_list[i]
############
    run_notify = multiprocessing.Process(None,notification(test))
    run_notify.start()
    
    try:
        while(test.should_reconnect):
            time.sleep(5)
        run_test.join()
    except KeyboardInterrupt: # Ctrl + C pressed
        pass # We're ignoring that Exception, so the user does not see that this Exception was raised.
    if run_test.is_alive:
        run_test.terminate()
        run_test.join() # Wait for terminate
    if run_test.exitcode == 0 or run_test.exitcode < 0:
        print("Bot exited.")
    else:
        raise BotCrashed("The bot has crashed")
