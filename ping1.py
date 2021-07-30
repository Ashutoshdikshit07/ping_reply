from ping3 import ping, verbose_ping

filename=input("enter file name: ")
f = open(filename,'r')

c=0
a=open('C:\\Users\\ashut\\OneDrive\\Desktop\\result.txt','w')
ips=f.read()
n=ips.split("\n")
for i in n:
    p=ping(i)
    print(ping(i))
    if p==None:
        z=i+": down\n"
        a.write(z)
        a.flush()
    else:
        z=i+": up\n"
        a.write(z)
        a.flush()
