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

# Modules error !

def stop():
    print("""%s
This is a module not an executeable program
Alternative command :
$ python3 core_pck3r.py
OR
$ python3 installer.py
OR
$ chmod 755 core_pck3r.py ; ./core_pck3r.py
And for installing :
$ chmod 755 installer.py ; ./installer.py
    """ % RED)

if __name__ == "__main__":
    stop()
else:
    # system error (red logo print)
    def sysErorr():
        return("\n%s尸⼕长㇌尺 : ERROR !\n%s"% (RED, NRM))

    #system call done (green logo print)
    def sysOk():
        return("\n%s尸⼕长㇌尺 :\n %s" % (GRN, NRM))
