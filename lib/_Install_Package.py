##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os

from _Check_Readme import ReadmeRst

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    with ReadmeRst():
        os.system("pip install -e .", shell=True)
