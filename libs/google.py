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

if __name__ == "__main__":
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

else:
        # system error (red logo print)
    def sysErorr():
        return("\n%s尸⼕长㇌尺 : ERROR !\n%s"% (RED, NRM))




    # only  user want google.com 
    def only_google_com(browser):
    
        
        if browser == "google-chrome": 

            syscall("%s google.com" % browser) if (syscall("whereis google-chrome")) == 0 else print("%s%sBrowser is not a valid one !!!\nOnly firefox, chrome(google-chrome), chromium%s" % (sysErorr(), RED, NRM))
            
        elif browser == "firefox":
            syscall("%s google.com" % browser)

        elif browser == "chromium":
            syscall("%s google.com" % browser)
        
        else:
            print("%s%sBrowser is not a valid one !!!\nOnly : firefox, chrome(google-chrome), chromium%s" % (sysErorr(), RED, NRM))

    # only firefox open search (firefox)
    def google_firefox(argv):
        argv_joined = " ".join(argv[3:])
        argv_joined = argv_joined.replace("?", "%3F")
        argv_joined = argv_joined.replace("+", "%2B")
        argv_joined = argv_joined.replace("-", "-&g")
        argv_joined = argv_joined.replace(" ", "+")
        syscall("firefox https://www.google.com/search?q=%s" % argv_joined)

    # other browser (firefox/chrome/chromium)
    def google_other(argv_browser, argv_two):

        if argv_browser == "firefox":
            argv_joined = " ".join(argv_two[3:])
            argv_joined = argv_joined.replace("+", "%2B")
            argv_joined = argv_joined.replace("-", "%-&gs")
            argv_joined = argv_joined.replace("?", "%3F")
            argv_joined = argv_joined.replace(" ", "+")
            syscall("%s https://www.google.com/search?q=%s" % (argv_browser, argv_joined))
            
        elif argv_browser == "chromium" : 
            
            argv_joined = " ".join(argv_two[3:])
            argv_joined = argv_joined.replace("+", "%2B")
            argv_joined = argv_joined.replace("-", "%-&gs")
            argv_joined = argv_joined.replace("?", "%3F")
            argv_joined = argv_joined.replace(" ", "+")    
            print("%s%sBrowser is not a valid one !!!\nOnly firefox, chrome(google-chrome), chromium%s" % (sysErorr(), RED, NRM)) if(syscall("ls /usr/bin/chromium")) !=0 else syscall("%s https://www.google.com/search?q=%s" % (argv_browser, argv_joined))


        elif argv_browser == "chrome" or argv_browser == "google-chrome":

            argv_joined = " ".join(argv_two[3:])
            argv_joined = argv_joined.replace("+", "%2B")
            argv_joined = argv_joined.replace("-", "%-&gs")
            argv_joined = argv_joined.replace("?", "%3F")
            argv_joined = argv_joined.replace(" ", "+")    
            print("%s%sBrowser is not a valid one !!!\nOnly firefox, chrome(google-chrome), chromium%s" % (sysErorr(), RED, NRM)) if(syscall("ls  /usr/bin/google-chrome")) !=0 else syscall("%s https://www.google.com/search?q=%s" % (argv_browser, argv_joined))

        # Exception
        else : 
            print(sysErorr())
            print("%sBrowser is not a valid one !!!\nOnly firefox, chrome(google-chrome), chromium%s" % (RED, NRM))
