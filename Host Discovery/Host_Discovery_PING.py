from scapy.all import *  


ip = IP()

icmp = ICMP()

pingpacket = ip/icmp 

addr = "10.10.10."

ipUpList = []

for i in range(256):
    pingpacket[IP].dst=addr+str(i)

    response = sr1(pingpacket,timeout=0.5,verbose=False)

    if(response):
        ipUpList.append(pingpacket[IP].dst)
    else:
        pass

print(ipUpList)        

