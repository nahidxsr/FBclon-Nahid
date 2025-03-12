# -*- coding: utf-8 -*-

import os
import time

# ANSI রঙ কোড
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# ইউজারের নাম
project_owner = "🔥 Nahid's Project 🔥"

# টারমাক্সে টেক্সট প্রিন্ট করা
def print_banner():
    os.system("clear")
    print(f"{RED}{'='*40}{RESET}")
    print(f"{GREEN}{project_owner.center(40)}{RESET}")
    print(f"{RED}{'='*40}{RESET}")
    print(f"{YELLOW}[1] Visit My YouTube Channel{RESET}")
    print(f"{YELLOW}[2] Update Packages{RESET}")
    print(f"{YELLOW}[3] Install Required Tools{RESET}")
    print(f"{YELLOW}[4] Exit{RESET}")
    print(f"{RED}{'='*40}{RESET}")

# ইউটিউব চ্যানেলে যাওয়ার ফাংশন
def open_youtube():
    print(f"{GREEN}Opening YouTube...{RESET}")
    time.sleep(1)
    os.system("xdg-open https://www.youtube.com/@yourchannel")

# টারমাক্স প্যাকেজ আপডেট করা
def update_packages():
    print(f"{GREEN}Updating Termux packages...{RESET}")
    time.sleep(1)
    os.system("pkg update && pkg upgrade -y")

# প্রয়োজনীয় টুল ইনস্টল করা
def install_tools():
    print(f"{GREEN}Installing Required Tools...{RESET}")
    time.sleep(1)
    os.system("pkg install python git -y")

# মেনু রান করানো
def main():
    while True:
        print_banner()
        choice = input(f"{BLUE}Enter your choice: {RESET}")

        if choice == "1":
            open_youtube()
        elif choice == "2":
            update_packages()
        elif choice == "3":
            install_tools()
        elif choice == "4":
            print(f"{RED}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Try again.{RESET}")
        time.sleep(2)

if __name__ == "__main__":
    main()
