'''
File : __init__.py  
Desc : Catalog of available commands and flags.
'''

# Imports here are sorted alphabetically.
import cmds.create
import cmds.help
import cmds.version

# Available commands and flags. Maybe sort them here alphabetically too?
commands : dict = {}
flags    : dict = {}

# Commands
commands['create'] = {'long' : 'create'}

# Flags
#flags['git'] = {'long' : '--init-as-git'}
flags['help']      = {'short' : '-h', 'long' : '--help'}
flags['version']   = {'short' : '-V', 'long' : '--version'}
flags['verbose']   = {'short' : '-v', 'long' : '--verbose'}