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
__authors__ = ["M.Amin Azimi .K (amzy-0)", "mehrzero", "https://github.com/amzy-0/pck3r/graphs/contributors"]


from libs import stuff
from os import  getcwd, getenv, chdir
from os import system as syscall
###############################################################################
# preinstall requirements                                                     #
syscall("mkdir -p ~/.pck3r/icon ; cp -rf ./icon/pck3r-logo.png ~/.pck3r/icon")#
syscall("sudo apt install python3-tk -y")                                     #
syscall("sudo apt install python3-pil python3-pil.imagetk -y")                #
syscall("sudo apt install g++ -y")                                            # 
###############################################################################
from tkinter import *
from tkinter.ttk import *
import time
from PIL import ImageTk,Image



# creating tkinter window
root = Tk()


make_link = "sudo ln -s %s/.pck3r/core_pck3r.py /bin/pck3r" % getenv("HOME")

# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
length = 100, mode = "determinate")

# Function responsible for the updation
# of the progress bar value
def bar():


    progress["value"] = 20
    root.update_idletasks()
    time.sleep(1)
    print("Unlinking pck3r (if was installed) ")
    syscall("sudo unlink /bin/pck3r ")
    syscall("sudo rm -rf /bin/pck3r*")
    progress["value"] = 40
    root.update_idletasks()
    time.sleep(1)




    
    syscall("rm -rf ~/.pck3r") if (syscall("echo %s ; ls ~/.pck3r" % stuff.CYN)) ==0 else print("%sCopy all pck3r directory %s" %(stuff.CYN, stuff.NRM))
    syscall("mkdir ~/.pck3r")
    syscall("cp -rf . ~/.pck3r")
    progress["value"] = 50
    root.update_idletasks()
    time.sleep(1)

    syscall(make_link)
    progress["value"] = 60
    root.update_idletasks()
    time.sleep(1)

    print("%sCheck link " % stuff.YEL)
    print("Link created ") if (syscall("ls -l  /bin/pck3r")) == 0  else print("%s%sNo link (/bin/pck3r)%s " % (stuff.sysOk(), stuff.RED, stuff.NRM))
    progress["value"] = 80
    root.update_idletasks()
    time.sleep(1)
    progress["value"] = 100

    print("%s%sPck3r installed successfuly %s" % (stuff.sysOk(), stuff.GRN, stuff.NRM))
    # user theme and window configuration
    root.quit()


# packing to main window (panel)
icon = Image.open("%s/.pck3r/icon/pck3r-logo.png" % getenv("HOME"))
root.title("Pck3r Installer")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)
root.geometry("400x80")
root.configure(background="black")
root.resizable(False, False)
root.style = Style()
root.style.theme_use("alt")
progress.pack(fill="x", pady = 10)
Button(root, text="install pck3r (system wide) ", command = bar).pack(fill="x", pady = 10)



# infinite loop
mainloop()

