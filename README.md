## Pinit (Project Initializer)
Pinit is a command line tool that is intended to be used to improve your progamming workflow.

## Installation
**Clone**
'''git clone https://github.com/nikkelarsson/Pinit.git'''

## How to use Pinit
1. Run it with python3
2. Compile it (with nuitka for example) and run as binary

**Run with pyhton**
'''python3 main.py'''

**Compile and run as binary**
First compile (nuitka works good for this)
'''python3 -m nuitka --follow-imports main.py'''

After compiling you will have main.bin (on MacOS, on linux it's propably just main).
Then you can rename main.bin to pinit and use as is.
'''./pinit'''

Or move the binary somewhere more appropriate, like usr/local/bin and then run
'''pinit'''

## Project creation
**Create a project with README.md**
'''pinit myproject --add-readme'''

or 

'''pinit myproject --add-readme=yes'''

**Create a project without README.md**
'''pinit myproject'''

or

'''pinit myproject --add-readme=no'''
