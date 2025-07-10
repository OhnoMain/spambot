import pyautogui as gui
import time
import random, string
import os
import sys

# Color setup
from colorama import init, Fore
init()

class GreenText:
    def write(self, text):
        sys.__stdout__.write(Fore.GREEN + text)
    def flush(self):
        sys.__stdout__.flush()

sys.stdout = GreenText()

# Boot intro
os.system('cls')
print("loading...")
time.sleep(1)
print("\nSetting up boot config...")
time.sleep(0.5)
print("\nEnabling bios...")
time.sleep(0.5)
print("\nHacking into the mainframe...")
time.sleep(0.5)
print("\nConfiguring windows...")
time.sleep(0.5)
print("\nSkid final boss mode activated...")
time.sleep(0.5)
print("\nWelcome to the FSociety...")
time.sleep(2)

os.system('cls')

outro = """
<------------------------------------------------>

                    made by Ohno
       
        feel free to checkout the github at 
            https://github.com/OhnoMain 
                         
<------------------------------------------------->             
"""

banner = """
           ▄████████    ▄███████▄    ▄████████   ▄▄▄▄███▄▄▄▄  
          ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄
          ███    █▀    ███    ███   ███    ███ ███   ███   ███
          ███          ███    ███   ███    ███ ███   ███   ███
        ▀███████████ ▀█████████▀  ▀███████████ ███   ███   ███
                 ███   ███          ███    ███ ███   ███   ███
           ▄█    ███   ███          ███    ███ ███   ███   ███
         ▄████████▀   ▄████▀        ███    █▀   ▀█   ███   █▀ 

▀█████████▄   ▄██████▄      ███                       
  ███    ███ ███    ███ ▀█████████▄                   
  ███    ███ ███    ███    ▀███▀▀██                   
 ▄███▄▄▄██▀  ███    ███     ███   ▀                   
▀▀███▀▀▀██▄  ███    ███     ███                       
  ███    ██▄ ███    ███     ███                       
  ███    ███ ███    ███     ███                       
▄█████████▀   ▀██████▀     ▄████▀                     

                   by ohno
"""

msg1 = """
[1]: random spam 
[2]: custom spam 
[3]: how to use 
[4]: about me 
"""
sel = "┌──(root㉿hacker)-[~]"

custom = """
[1]: big 2025 words  
[2]: italian brainrot 
"""

def wait_input(prompt, options):
    choice = input(prompt).strip()
    while choice not in options:
        print("❌ Invalid choice. Try again.")
        choice = input(prompt).strip()
    return choice

def wait_number(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Please enter a valid number.")

while True:
    os.system('cls')
    print(banner)
    print(f"\n{msg1}")
    print(f"\n{sel}")

    mode = wait_input("└─ please enter your desired mode: ", ["1", "2", "3", "4"])

    if mode == "1":
        os.system('cls')
        print(sel)
        message = input("└─ input the message: ")
        number = wait_number("└─ how many times do you want to repeat the message: ")
        time.sleep(3)

        for i in range(number):
            gui.typewrite(message)
            gui.press("Enter")

        print("✅ Complete!")
        time.sleep(2)

    elif mode == "2":
        os.system('cls')
        print(custom)
        bum = wait_input("└─ select spam file [1 or 2]: ", ["1", "2"])

        file_path = "crazy.txt" if bum == "1" else "italian.txt"

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                words = f.read().split()
        except FileNotFoundError:
            print("❌ File not found. Make sure the text file exists.")
            time.sleep(2)
            continue

        number = wait_number("└─ how many times do you want to loop all words: ")
        time.sleep(3)

        for _ in range(number):
            for word in words:
                gui.typewrite(word)
                gui.press("Enter")

        print("✅ Complete!")
        time.sleep(2)

    elif mode == "3":
        os.system('cls')
        print("""
HOW TO USE

1. Open any text box or chat where you want to send spam.
2. Select the desired mode:
   - Random spam: you input your own message.
   - Custom spam: uses pre-written files (crazy.txt or italian.txt).
3. Enter how many times you want the message(s) to repeat.
4. Once the timer ends, the spam will begin. Make sure your target window is focused!

⚠️ WARNING: This script simulates real keyboard input. 
Make sure you're not typing or using the mouse during the spam or things will go weird.
""")
        input("\nPress Enter to return to main menu...")

    elif mode == "4":
        os.system('cls')
        print("""
ABOUT ME

Hi, I'm Ohno 👋

I'm a casual coder who enjoys making weirdly fun scripts for fun and chaos. I do:
- Python scripting (like this beast)
- Roblox game development
- Little bits of automation and dumb utilities

Discord: Ohno_18533
GitHub: https://github.com/OhnoMain

Feel free to reach out if you want collabs, ideas, or help!
""")
        input("\nPress Enter to return to main menu...")

    print(sel)
    res = wait_input(f"\n└─ do you want to restart (y/n)?: ", ["y", "n"])
    if res == "n":
        print(f"\n{outro}")
        time.sleep(3)
        input("Press enter to exit: ")
        break
