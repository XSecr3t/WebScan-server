#!/usr/bin/python
################################
# Coded By Mr.XSecr3t          #
# AnonSec Hackers Universe 	   #
# Release Date : 15-11-2018	   #
################################
import httplib
import socket
import time
import sys
print('----------------------------------------------------')
print('|  Cod3d By :                                      |')
print('|        ___                  ____                 |')
print('|       / _ | ___  ___  ___  / __/__ ____          |')
print('|      / __ |/ _ \/ _ \/ _ \_\ \/ -_) __/          |')
print('|     /_/ |_/_//_/\___/_//_/___/\__/\__/           |')
print('|    AnonSec Hackers:::Universe In Here            |')
print('|   https://www.facebook.com/anonxsecr3t           |')
print('|         anonxsecr3t@tutamail.com                 |')
print('|        ICDT@Offsec.id | anonsec.us               |')
print('|              wwww.icdtSec.net                    |')
print('----------------------------------------------------')
try:
    try:
        site = raw_input("Web Site for Scan?: ")
        site = site.replace("http://","")
        site = site.replace("https://","")
        print ("\tChecking website " + site + "...")
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "\t[$] Yes... Server is Online."
    except (httplib.HTTPResponse, socket.error) as Exit:
        print("\t [!] Oops Error occured")
        raw_input("\t [!] Possible problems: Server offline, Invalid URL,Internet offline")      
        exit()
    conn = httplib.HTTPConnection(site)
    conn.request("HEAD", "/")
    req = conn.getresponse()
    print "\n\t------------------------------------------"
    print "\n\t     [+] Server: "+req.getheader('server')
    power = req.getheader('x-powered-by')
    if power == None:
        print "\t     [X] Powered by: Not Found !"
    else:
        print "\t     [+] Powered by: "+ power
    print "\t     [+] Encoded in: "+req.getheader('Content-type')
    cookie = req.getheader('Set-Cookie')
    if cookie == None:
        print "\t     [X] Set Cookie Failed"
    else:
        print "\t     [+] Set Cookie: "+cookie
    print "\n\t------------------------------------------"
    print "Job Done!"
    time.sleep(0.100) # Wait for 3 second
    print "Greetz To Mr.XSecr3t And All AnonSec Member"
except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Session cancelled"
