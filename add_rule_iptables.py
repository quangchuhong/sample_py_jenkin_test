# -*- coding: utf-8 -*-

import os
import time
import sys
import subprocess


def add_rules_input(line01,lin02, line03):
    # open file rad all lines
    with open("iptables.conf",'r+') as f:
        lines = f.readlines()
        i=0
        for line in lines:
            if '-A INPUT -i lo -j ACCEPT' in line:      # tim line co dong string '-A INPUT -i lo -j ACCEPT'
                #insert line01 vao list lines voi thu tu i++
                lines.insert(i+1,line01)
                lines.insert(i+2,line02)
                lines.insert(i+3,line03)
            i += 1
    with open("iptables.conf",'r+') as f:
        for line in lines:
            f.write(line)  
    # reload file iptables sau khi add new rule
    #subprocess.call('sudo systemctl reload iptables', shell=True)



def add_rules_output(line04,lin05,line06):
    # open file rad all lines
    with open("/etc/sysconfig/iptables",'r+') as f:
        lines = f.readlines()
        i=0
        for line in lines:
            if '-A OUTPUT -o lo -j ACCEPT' in line:      # tim line co dong string -A OUTPUT -o lo -j ACCEPT
                #insert line01 vao list lines voi thu tu i++
                lines.insert(i+1,line04)
                lines.insert(i+2,line05)
                lines.insert(i+3,line06)
            i += 1
    with open("/etc/sysconfig/iptables",'r+') as f:
        for line in lines:
            f.write(line)  

# function run file /etc/sysconfig/iptables
def run_file_iptables(line01,line02,line03,line04,line05,line06):
    # copy file /etc/sysconfig/iptables to iptables.bak
    subprocess.call('sudo cp -r /etc/sysconfig/iptables /etc/sysconfig/iptables.bak', shell=True)
    # call funtion ad rule input vs output
    add_rules_input(line01,line02,line03)
    add_rules_output(line04,line05,line06)
    subprocess.call('sudo systemctl reload iptables', shell=True)
    print "run file done !"

# define rule input
line01 = '\n######################## Add rule permit ssh ########################\n'
line02 = '-A INPUT -s 10.61.18.189 -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT\n'
line03 = '-A INPUT -s 10.0.18.18 -p tcp -m state --state NEW -m tcp --dport 1521 -j ACCEPT\n'

# define rule output
line04 = '\n######################## Add OUTPUT rule permit ssh ########################\n'
line05 = '-A OUTPUT -d 10.61.18.189 -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT\n'
line06 = '-A OUTPUT -d 10.0.18.18 -p tcp -m state --state NEW -m tcp --dport 1521 -j ACCEPT\n'

# call file add rule iptables
add_rules_input(line01,line02,line03)



