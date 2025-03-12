#Davloper :- https://t.me/+PCHk9_nDCMM3NDI1

I = '\x1b[1;32m'
Q = '\x1b[00m'
dt = f'{Q}[{I}•{Q}]'
n = '\n'
import os
import sys
import time
import requests
from requests.structures import CaseInsensitiveDict
import random
os.system('clear')
biblack = '\x1b[1;90m'
bired = '\x1b[1;91m'
bigreen = '\x1b[1;92m'
biyellow = '\x1b[1;93m'
biblue = '\x1b[1;94m'
bipurple = '\x1b[1;95m'
bicyan = '\x1b[1;96m'
biehite = '\x1b[1;97m'
print (" \x1b[1;97mJ\x1b[1;96mO\x1b[1;95mN\x1b[1;94mE\x1b[1;90m")
os.system (" xdg-open https://t.me/+PCHk9_nDCMM3NDI1")
print(bired + '\n\x1b[1;\033[41m\x1b[1;97m##    ##  ######   ########   \33[m \n ##   ##  ##    ##  ## \033[32m          \n ##  ##   ##        ##  \033[33m         \n #####    ##   #### ######     \33[1;96m \n ##  ##   ##    ##  ##    \x1b[0;34m      \n ##   ##  ##    ##  ##    \033[95m      \n  ##    ##  ######   ##\n             \n\x1b[1;96m__________________________________________________\n__________________________________________________\n\n')

def DH():
    import sys
while True:
    usern = 'ADNAN-R15'
    passwd = 'ADNAN-V4'
    inpuser = str(input(bigreen + ' \x1b[1;97m[•] Enter Your Username: '))
    inppass = str(input(' \x1b[1;97m[•] Enter Your Password: '))
    if usern == inpuser and passwd == inppass:
        print(bigreen + ' [√]User & Password Correct !')
        break
    print(bired + ' [×] Wrong User or Password !')
    Please_Try_Again()
    os.system('xdg-open https://t.me/+PCHk9_nDCMM3NDI1')
os.system('clear')
logo = '\033[41m\x1b[1;97m##    ##  ######   ########   \33[m \n ##   ##  ##    ##  ## \033[32m          \n ##  ##   ##        ##  \033[33m         \n #####    ##   #### ######     \33[1;96m \n ##  ##   ##    ##  ##    \x1b[0;34m      \n ##   ##  ##    ##  ##    \033[95m      \n  ##    ##  ######   ##\n97m__________________________________________________\n\x1b[1;97m__________________________________________________\n'

def clear():
    os.system('clear')

def menu():
    clear()
    print(logo)
    print(f' {dt} [01] CUSTOM SMS')
    print(f' {dt} [02] CUSTOM SMS BOMBER')
    print(f' {dt} [03] TOOLS OWNER')
    print(f' {dt} [04] EXIT')
    user = input(f' {dt} CHOICE OPTION : ')
    if user in ['01', '1']:
        custom()
    elif user in ['02', '2']:
        customb()
    elif user in ['03', '3']:
        os.system('xdg-open https://t.me/+PCHk9_nDCMM3NDI1')
    else:
        exit(f' {dt} THANKS FOR USEING MY TOOLS ')

def custom():
    clear()
    print(logo)
    nmbr = input(f' {dt} ENTER NUMBER : ')
    msg = input(f' {dt} ENTER MESSAGE : ')
    api = f'https://bd-custom-sms.vercel.app/send-sms?key=sms&number={nmbr}&message={msg}'
    requests.get(api)
    print('SMS Send Successful')
    time.sleep(5.09)
    os.system('xdg-open https://t.me/+PCHk9_nDCMM3NDI1')
    menu()

def customb():
    clear()
    print(logo)
    nmbr = input(f' {dt} ENTER NUMBER : ')
    msg = input(f' {dt} ENTER MESSAGE : ')
    lmt = int(input(f' {dt} ENTER AMOUNT : '))
    for i in range(lmt):
        api = f'https://bd-custom-sms.vercel.app/send-sms?key=Bomber&number={nmbr}&message={msg}'
        requests.get(api)
        print(str(i + 1) + f' {dt} SMS Send Successful  \n')
    print('Custom SmS Bombing Successful')
    time.sleep(5.09)
    os.system('xdg-open https://t.me/+PCHk9_nDCMM3NDI1')
    menu()
menu()
