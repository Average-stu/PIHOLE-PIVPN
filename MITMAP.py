import os
header="""
                                                          ---------|
 |\      /|   --------  ---------- |\      /|      /\     |        |
 | \    / |      |          |      | \    / |     /  \    |        |
 |  \  /  |      |          |      |  \  /  |    /    \   |--------|       
 |   \/   |      |          |      |   \/   |   /----- \  |
 |        |   --------      |      |        |  /        \ |

"""

print(header)
print("Welcome to MITM AP Version 1.0")
c=input("Do u want to continue : Y/N")
if(c=='Y' or c=='y'):
    x=input("Do u want to change the MAC ADDRESS: Y/N")
    if(x=='Y' or x=='y'):
        os.system('mac.py')
        os.system('scanner.py')
        os.system('scanner2.py')
        os.system('arp.py')
        os.system('psniffer.py')
        print("1.DNS PROOF")
        print("2.File Injector")
        print("3.Code Injector")
        print("4.Https Bypassing")
        print("5.Exit")
        ch=input("Enter your choice")
        while(True):
            if(ch==1):
                os.system('dns_spoof.py')
            elif(ch==2):
                os.system('file_int.py')
            elif(ch==3):
                os.system('co.in.py')
            elif(ch==4):
                os.system('https.py')
            elif(ch==5):
                exit()



    else:
        os.chdir('/users/Lenovo')
else:
    os.chdir('/users/Lenovo')
    