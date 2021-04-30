'''
file : __init__.py  
desc : Catalog of available commands and flags.
'''

# Imports here are sorted alphabetically.
import cmds.usage
import cmds.version
import cmds.help
import cmds.create

# Available commands and flags. Maybe sort them here alphabetically too?
commands = {}
flags = {}

commands['create'] = {'long' : 'create'}

#flags['git'] = {'long' : '--init-as-git'}
flags['help'] = {'short' : '-h', 'long' : '--help'}
flags['version'] = {'short' : '-V', 'long' : '--version'}
flags['verbose'] = {'short' : '-v', 'long' : '--verbose'}