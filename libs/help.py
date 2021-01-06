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
    print("""%s
-----------------------------------------
|                                       |
| pck3r : It is a versatile program and |
|                                       |
| you avoid using useless commands and  |
|                                       |
| it is written for Ubuntu...           |
|                                       |
-----------------------------------------

\"install\" command :

    $ pck3r install \"somthing\" :
    {
            nodejs,
            python3pip,
            java,
            wine,
            ohmyzsh,
            or ...
    }

\"clear\" command :

    $ pck3r clear:
    {clear your terminal }

\"iso\" command :

    $ pck3r iso 32/64  \"somthing\":
    {
        mint,
        fedora,
        gentoo,
        or ...
    }

\"dwn\" command :

    $ pck3r dwn \"https/http://somthing\"
    {dwn is downloader for pck3r }

\"sys\" command :

    $ pck3r sys update
    (update your oprating system)

    $ pck3r sys upgrade
    (upgrade your oprating system)

    $ pck3r updgr
    (both, update and upgrade (full upgrade))

\"term\" command :
    $pck3r term
    (command for run, pck3r terminal emulator)

\"google\" command :


    $pck3r google <browser> <search section(word1 word2 word3 ...)
    (quick google search ...)
    (like this : $ pck3r google firefox what is google search engine)

\"tilix\" command :


    $ pck3r tilix
    (tilix terminal ...)

\"dotnet\" command :


    $ pck3r install dotnet
    (installing .NET (dot net ) C0RE, ASP, MCS compiler , ...)

\"pkg\" command :


    $ pck3r pkg <package name>
    (search for packages ...)
    """ % YEL)