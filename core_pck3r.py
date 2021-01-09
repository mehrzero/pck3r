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

from os import system as syscall
from os import getenv, getcwd, chdir
from sys import argv
from libs import stuff
from libs import google
from libs import dotnet

argc = len(argv)

for i in range(argc):

        # if user just type $ pck3r
        if argc <= 1:
            print("%s%sNo arguments\nPlease try :\n$ pck3r <commands>\nOR\n$ pck3r help %s" % (stuff.sysErorr(), stuff.RED, stuff.NRM))

        else:

            # if argument 1 equal to "clear"
            # clear terminal
            # do :
            if argv[1] == "clear" and argc == 2:
                syscall("clear")
                print("%sThis is funny clear command :D "%stuff.sysOk())
            
            # pck3r updator
            elif argv[1] == "update" and argc == 2:
                chdir("%s/.pck3r" % getenv("HOME"))
                print("%s/.pck3r/./source-updator-for-dev"  % getenv("HOME"))
                syscall("./source-updator-for-dev")

            # if argument 1 equal to "help"
            # like -> $ pck3r help
            # do :
            elif argv[1] == "help" and argc == 2:
                from libs import help

            # if argument 1 equal to "install"
            # and argument 2 is not empty
            # do :
            elif argv[1] == "install" and argc >= 2:

                # if after install is empty
                if argv[1]== "install" and argc <= 2:
                    print("%s%sAfter \"install\" is empty !%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))

                # if argument 2 is nodejs
                elif argv[2]=="nodejs" and argc==3:

                    if (syscall("echo %s ; curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - ; echo %s ; sudo apt install nodejs; sudo apt-get update && echo %s; sudo apt install yarnpkg -y" % (stuff.YEL, stuff.CYN, stuff.MAG)))==0:

                        print("%s" % stuff.sysOk())

                        syscall("echo %s\"Nodejs LTS Version :\" ;  node --version %s" %(stuff.GRN, stuff.NRM))
                        syscall("echo \"Npm Version :\" %s; npm --version %s" %(stuff.GRN, stuff.NRM))

                        # Exception
                    else:
                        print("%s%sInstallation breaked\npackage(s) : nodejs ! !%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))

                elif argv[2] == "dotnet" and argc==3:
                    dotnet.install_dotnet()

                elif argv[2] == "ohmyzsh" and argc==3:
                    syscall("sudo apt install zsh curl")
                    syscall("sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"") if (syscall("curl --version")) == 0 else syscall("echo \"curl\" is required for using \"ohMyZsh\" ; sudo apt install curl")

                # argument 2 is not empty
                elif argv[2:] != [] and argc >= 2:
                    print("%s%s\nCommand is valid!\n%s" % (stuff.sysOk(), stuff.GRN, stuff.YEL))
                    syscall("sudo apt install %s" % " ".join(argv[2:]))
                # Exception
                else:
                    print("Command or package(s) not found ! %s" % (stuff.sysErorr(), argv[2:]))

            # if argument 1 equal to "uninstall"
            elif argv[1] == "uninstall" and argc >= 2:

                # if after "uninstall" is empty
                if argv[1] == "uninstall" and argc <= 2:
                    print("%s %sAfter \"uninstall\" is empty !%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))
                
                # if user want uninstall dotnet 
                # do :
                elif argv[2]=="dotnet" and argc==3:
                    dotnet.uninstall_dotnet()

                # argument 2 is not empty
                # do :
                elif argv[2:] != [] and argc >= 2:
                    print("%s%s\nCommand is valid!\n%s" % (stuff.sysOk(), stuff.GRN, stuff.YEL))
                    syscall("sudo apt purge %s" % " ".join(argv[2:]))

            # if argument 1 equal to "rm" (sudo apt remove)
            elif argv[1] == "rm" and argc >= 2:

                # if after install is empty
                if argv[1]== "rm" and argc<=2:
                    print("%s %sAfter \"rm\" is empty !%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))

                #  argument 2 is not empty
                # do :
                if argv[2:] != [] and argc>=2:
                    print("%s%s\nCommand is valid!\n%s" % (stuff.sysOk(), stuff.GRN, stuff.YEL))
                    syscall("sudo apt remove %s" % " ".join(argv[2:]))

                # Exception
                else:
                    print("Command or package(s) not found ! %s" % (stuff.sysErorr(), argv[2:]))


            # Too many arguments error for $ pck3r term
            # Only use :
            # $ pck3r term <somthing> <somthing> <somthing> <somthing>, ...
            elif argv[1] =="term" and argc>2:
                print("%s%sToo many arguments !\nOnly use :\n$ pck3r term %s" % (stuff.sysErorr(), stuff.RED, stuff.NRM))

            elif argv[1] =="term" and argc==2:
                from libs import pck3rTerminal


            # Too many arguments error for $ pck3r term
            # Only use :
            # $ pck3r tilix <somthing> <somthing> <somthing> <somthing>, ...
            elif argv[1] =="tilix" and argc==2:
                syscall("sudo apt install tilix  ; clear ; tilix ")


            # Too many arguments error for $ pck3r tilix
            # Only use :
            # $ pck3r tilix <somthing> <somthing> <somthing> <somthing>, ...
            elif argv[1] =="tilix" and argc>2:
                    print("%s%sToo many arguments !\nOnly use :\n$ pck3r term %s" % (stuff.sysErorr(), stuff.RED, stuff.NRM))


            # if argument 1 equal to "google"
            # after 3 argument ($pck3r google <args>) will  send all other arguments to google_firefox function
            # this function substitute all marks or simbols (+,-,\?, ...)
            # and all arguments are  valid  for search input

            elif argv[1] == "google" and argc >= 2:

                # if after google is empty
                if argv[1]== "google" and argc==2:
                    print("%s%sAfter \"google\" is empty !\nPlease try:\n$ pck3r google <browser>%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))

                # only open google.com (browser == argv[2])
                elif argv[2] != [] and argc==3:
                    if argv[2] == "chrome":
                        google.google_other("google-chrome", argv)
                    else:
                        google.only_google_com(argv[2])

                elif argv[2] == "firefox" and argc>3:
                    google.google_firefox(argv)

                elif argv[2]=="chrome" and argc>3:
                    google.google_other("google-chrome", argv)

                # open google.com only (google chrome)
                elif argv[2]=="chrome" and argc==3:
                    google.google_other("google-chrome", argv)

                # open google.com only (google chrome)
                elif argv[2]=="google-chrome" and argc==3:
                    google.google_other("google-chrome", argv)

                # open google.com with other browser
                elif argv[2]!= [] and argc > 3:
                    google.google_other(argv[2], argv)


            # if after "sys" command is empty
            elif argv[1] == "sys" and argc == 2:
                print("%s%sAfter \"sys\" is empty !\nPlease try:\n$ pck3r sys <update/upgrade/updgr(update and upgrade)>%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))

            # if after pck3r equal to "sys"
            elif argv[1] == "sys" and argc > 2:
                if argv[2]=="update" and argc==3:
                    syscall("sudo apt update")
                    print("%s%s\nYour oprating system updated%s" % (stuff.sysOk(), stuff.GRN, stuff.NRM))

                # if user command, equal to $ pck3r sys upgrade
                #do :
                elif argv[2] == "upgrade" and argc==3:
                    
                    if (syscall("sudo apt full-upgrade")) == 0:
                        print("%s%syour oprating system  upgraded" % (stuff.sysOk(), stuff.GRN))
                        syscall("echo %s" % stuff.GRN)
                        syscall("echo your oprating system information :")
                        syscall("uname -a ")
                        syscall("echo your machine architecture : ")
                        syscall("uname -p")
                        syscall("echo %s" % stuff.NRM)
                    
                    else:
                        print(f"{stuff.sysErorr()}{stuff.RED}{stuff.NRM}")

                # if user command, equal to $ pck3r sys updgr
                #do :
                elif argv[2] == "updgr" and argc==3:
                    
                    if (syscall("sudo apt update && apt full-upgrade")) ==0:
                            
                        print("%s%syour oprating system updated and upgraded" % (stuff.sysOk(), stuff.GRN))
                        syscall("echo %s" % stuff.GRN)
                        syscall("echo your oprating system information :")
                        syscall("uname -a ")
                        syscall("echo your machine architecture : ")
                        syscall("uname -p")
                        syscall("echo %s" % stuff.NRM)
                    
                    else:
                        print(f"{stuff.sysErorr()}{stuff.RED}{stuff.NRM}")
                
                # if command is not a valid one !
                # will send an error to the user.
                # do :
                else:
                    print("%s%sPlease try this :\n$ pck3r google <browser> <word(1, 2, 3, 4, 5, 6, ...)-<word(n)>%s" % (stuff.sysErorr(), stuff.RED, stuff.NRM))

            # if after "pkg" is empty
            elif argv[1]== "pkg" and argc <= 2:
                print("%s%sAfter \"pkg\" is empty !%s " % (stuff.sysErorr() , stuff.RED, stuff.NRM))
            
            # if after "pkg" is not empty
            elif argv[1] == "pkg" and argc >= 2:


                # if after "pkg" isn't empty
                if argv[2:] != [] and argc >= 2:
                    syscall("sudo apt search %s" % " ".join(argv[2:]))

                
            # if comamnd not a valid command in pck3r
            # do :
            else:
                print("%s%sCommand not found !%s\nPlease try:\n$ pck3r help %s" %  (stuff.sysErorr(), stuff.RED, stuff.CYN, stuff.NRM))

        # end of (for) loop
        break
