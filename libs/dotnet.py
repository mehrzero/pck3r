#!/usr/bin/python3
from os import system as syscall
#color zone
NRM = "\x1B[0m"
RED = "\x1B[31m"
GRN = "\x1B[32m"
YEL = "\x1B[33m"
BLU = "\x1B[34m"
MAG = "\x1B[35m"
CYN = "\x1B[36m"
WHT = "\x1B[37m"
#end of color zone

# system error (red logo print)
def sysErorr():
    return("\n%s尸⼕长㇌尺 : ERROR !\n%s"% (RED, NRM))

#system call done (green logo print)
def sysOk():
    return("\n%s尸⼕长㇌尺 :\n %s" % (GRN, NRM))

def install_dotnet():
    if (syscall("wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo dpkg -i packages-microsoft-prod.deb")) !=0 :
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)




    elif (syscall("sudo apt update")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt  install -y apt-transport-https")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt  updat")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall(" sudo apt  install -y dotnet-sdk-3.1")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt  install -y aspnetcore-runtime-3.1")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt  install -y dotnet-runtime-3.1")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt install -y mono-complete")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 )  "% RED)



    elif (syscall("sudo apt  update")) != 0:
        sysErorr()
        print("%scan't install .NET (only for *UBUNTU 20.04 )  "% RED)


    else:
        sysOk()
        print("%s.NET(microsoft dotnet and MCS compiler (LINUX platform) ) installed  "% GRN )
