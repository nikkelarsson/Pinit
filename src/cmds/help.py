'''
file : help.py  
desc : Management of printing command and flag descriptions.
'''

#
# The output should look something like:
#
# <program> X.X, short description here.
# Usage: <program> [options]...
#
# <category name>:
#     -f,  --flags-here               Description here.
#

import cmds.descs.cmd
import cmds.descs.usg 

def get(pname, version, language='eng'):
	'''Print descriptions for Pinit's commands.'''

	if language == 'fi':
		usage_description = cmds.descs.usg.finnish.usage['desc']
		usage = cmds.descs.usg.finnish.usage['usage']
		opts = cmds.descs.usg.finnish.usage['opts']
		cmd_descriptions = cmds.descs.cmd.finnish.__doc__
	elif language == 'eng':
		usage_description = cmds.descs.usg.english.usage['desc']
		usage = cmds.descs.usg.english.usage['usage']
		opts = cmds.descs.usg.english.usage['opts']
		cmd_descriptions = cmds.descs.cmd.english.__doc__

	print('{} {}, {}'.format( pname[0].upper() + pname[1:].lower(), version, usage_description ))
	print('{}: {} {}'.format( usage, pname, opts ))
	print()
	print('{}'.format( cmd_descriptions ))