from scapy.all import * 

wl = Ether()
arp = ARP()

wl.dst="ff:ff:ff:ff:ff:ff"

arp.pdst ="10.10.10.1/24"

brcpckt = wl/arp

brcpckt.show()

ans,unans=srp(brcpckt,timeout=5)

ans.summary()
print("#"*30)
unans.summar()

for snd,rcv in ans:
    #print(rcv.sprintf("%Ether.src% %ARP.psrc%"))


    print(rcv.src ,": : ",rcv.psrc)

