import random
import sys
import time
import os

# setting kecepatan
def slow(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)
def med(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)
def fast(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 170)

try:
    from googlesearch import search

except ImportError:
    fast("[!] you mush install google ..")
    med("[*] wait a moment, this program will install the module ...")
    os.system("pip3 install google")
    time.sleep(3)
    med("[*] done ...")

def banner():
    print("""
 
____ ____ ____ ___  ____ ____
|    |__/ |___ |__] |___ [__  
|___ |  \ |___ |    |___ ___]          
    """)


def clear(): #clear function
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

# pembukaan
if sys.version.startswith("3"):
    slow("[!] wibu hengker has ben detected ...")
    time.sleep(2)
else:
    slow("[x] so you're a normal person then ...")
    time.sleep(3)
    sys.exit(1)

# pembukaan 2
if sys.version.startswith("3"):
    slow("[!] ok continue ...")
    time.sleep(2)
else:
    slow("[x] can't go on ...")
    time.sleep(3)
    sys.exit(1)

# hitung 1
if sys.version.startswith("3"):
    slow("~# 1 ...")
    time.sleep(0.3)
else:
    slow("[-] error bre")
    time.sleep(2)
    sys.exit(1)
    
# hitung 2
if sys.version.startswith("3"):
    slow("~# 2 ...")
    time.sleep(0.3)
else:
    slow("[-] error bre")
    time.sleep(2)
    sys.exit(1)
    
# hitung 3
if sys.version.startswith("3"):
    slow("~# 3 ...")
    time.sleep(0.3)
else:
    slow("[-] error bre")
    time.sleep(2)
    sys.exit(1)

# hitung 4
if sys.version.startswith("3"):
    slow("~# 4 ...")
    time.sleep(0.3)
else:
    slow("[-] error bre")
    time.sleep(2)
    sys.exit(1)
    
# hitung 5
if sys.version.startswith("3"):
    slow("~# 5 ...")
    time.sleep(0.3)
else:
    slow("[-] error bre")
    time.sleep(2)
    sys.exit(1)
    

# starting
slow('[!] loading ..... ')
time.sleep(2)
clear()
time.sleep(2)
banner()
med("""
#================================================================#
~# Pwnd by Flux10n/0x1337                                        #
~# Github : https://github.com/flux10n                           #
~# Monero : -                                                    #
~# Mail : jwyzmhof@duck.com                                      #
~# About : simple tools are useful for dorking gaps              #
#================================================================#""")
time.sleep(3)

try:
    namefile = input("\n[?] do you want to keep the dork (y/n) ").strip()
    dork = ("")

except KeyboardInterrupt:
        print ("\n[!] you press ctrl + c")
        time.sleep(0.5)
        print("\n[!] exit")
        sys.exit(1)


def savefile(namefile):
    file = open((dork) + ".txt", "a")
    file.write(str(namefile))
    file.write("\n")
    file.close()


if namefile.startswith("y" or "Y"):
    print("[!] enter the file name below")
    dork = input("[?] enter the file name : ")
    savefile(namefile)
else:
    print ("[*] file not saved \n")


def akhir():
    try:
        dork = input("\n[*] enter your dork : ")
        uneed = input("[?] what quantity do you want : ")
        print ("\n ")

        requ = 0

        for results in search(dork, tld="com", lang="en", num=int(uneed), start=0, stop=None, pause=2):
            print ("[$]", results)
            time.sleep(0.1)
            requ += 1.
            if requ >= int(uneed):
                break

            namefile = (results)

            savefile(namefile)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("[!] you press ctrl + c ... !")
            print ("[!] exit ..")
            time.sleep(0.5)
            sys.exit(1)

    slow("~# Done :p ... ")
    sys.exit()



akhir()