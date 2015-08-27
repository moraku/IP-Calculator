#IP Calculator

IP = "192.168.0.1/30"

All = False
try:
    if (IP.index("-a") > 0):
        All = True
        IP = IP[0:IP.index("-a")]
except ValueError:
    All = False


MASK = int(IP[IP.index("/")+1:])

IP = IP[0:IP.index("/")]
IP = IP.split(".")

print("Address: "+IP[0]+"."+IP[1]+"."+IP[2]+"."+IP[3])

BIN_NET = '{0:32b}'.format(2**32 - 2**(32-MASK))
M1 = int(BIN_NET[0:8],2)
M2 = int(BIN_NET[8:16],2)
M3 = int(BIN_NET[16:24],2)
M4 = int(BIN_NET[24:32],2)
print("Netmask: "+str(M1)+"."+str(M2)+"."+str(M3)+"."+str(M4))
print("Wildcard: "+str(255-M1)+"."+str(255-M2)+"."+str(255-M3)+"."+str(255-M4))

print("")

OCT1 = int(IP[0]) * 16777216
OCT2 = int(IP[1]) * 65536
OCT3 = int(IP[2]) * 256
OCT4 = int(IP[3])

SUM = OCT1 + OCT2 + OCT3 + OCT4

BIN_SUM = '{0:32b}'.format(SUM)
BIN_IP = BIN_SUM[0:MASK]

rang = 2**(32-MASK)
for i in range (rang):
    if(All == False):
        if (i != 0 and i != rang-1):
            continue
            
    BUF_BIN_IP = BIN_IP+("{:0%db}"%(32-MASK)).format(i)
    O1 = str(int(BUF_BIN_IP[0:8],2))
    O2 = str(int(BUF_BIN_IP[8:16],2))
    O3 = str(int(BUF_BIN_IP[16:24],2))
    O4 = str(int(BUF_BIN_IP[24:32],2))
    print(O1+"."+O2+"."+O3+"."+O4)
