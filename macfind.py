#!/usr/bin/python

# Licence

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                  Version 2, December 2004 

# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

#  0. You just DO WHAT THE FUCK YOU WANT TO.

from scapy.all import *

dst = raw_input("Enter target IP address : ")
ether = Ether()
ether.src='00:e0:1c:3c:22:b4'
ether.dst='FF:FF:FF:FF:FF:FF'

# ARP
arp=ARP()
arp.op=1
arp.hwsrc='00:e0:1c:3c:22:b4'
arp.psrc=raw_input("Enter your IP Address : ")
arp.pdst=dst
arp.hwdst='00:00:00:00:00:00'
p=srp1(ether/arp)

# MAC Print
print"Mac address device is ",p.hwsrc
