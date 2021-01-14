#!/usr/bin/python3

""" 

Short description of this Python module.
Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

"""
__authors__ = ["M.Amin Azimi .K (amzy-0)", "mehrziro", "https://github.com/amzy-0/pck3r/graphs/contributors"]


from . import stuff
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



    elif (syscall("sudo apt  update")) != 0:
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

def uninstall_dotnet():
    if (syscall("sudo apt update")) != 0:
        sysErorr()
        print("%sCan't remove .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt purge  -y apt-transport-https")) != 0:
        sysErorr()
        print("%sCan't remove .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt  update")) != 0:
        sysErorr()
        print("%sCan't remove .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall(" sudo apt purge  -y dotnet-sdk-3.1")) != 0:
        sysErorr()
        print("%sCan't remove .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt purge  -y aspnetcore-runtime-3.1")) != 0:
        sysErorr()
        print("%sCan't remove .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt purge  -y dotnet-runtime-3.1")) != 0:
        sysErorr()
        print("%sCan't remove .NET (only for *UBUNTU 20.04 ) \n "% RED)



    elif (syscall("sudo apt purge  -y mono-complete")) != 0:
        sysErorr()
        print("%scan't remove .NET (only for *UBUNTU 20.04 )  "% RED)



    elif (syscall("sudo apt  update && sudo apt full-upgrade ; sudo apt autoremove -y")) != 0:
        sysErorr()
        print("%scan't remove .NET (only for *UBUNTU 20.04 )  "% RED)


    else:
        sysOk()
        print("%s.NET(microsoft dotnet and MCS compiler (LINUX platform) ) reomved  "% GRN )

