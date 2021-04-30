'''
file : usage.py  
desc : Management of printing usage description.
'''

import cmds.descs.usg

def get(pname, language='eng'):
	'''Print short usage description on how to use Pinit.'''

	# This is kind of stupid to write tons and tons of if-elif
	# clauses. It would be much more clear and debug friendly to have
	# one ”usage = usg.<lang>.__doc__” line, where the ”<lang>” would
	# be set based on the language set in the ”cfg/__init__.py”.
	# However, I'm sticking to this method for now until I'll
	# figure out someting better.
	if language == 'fi':
		usage = cmds.descs.usg.finnish.usage['usage']
		opts = cmds.descs.usg.finnish.usage['opts']
	elif language == 'eng':
		usage = cmds.descs.usg.english.usage['usage']
		opts = cmds.descs.usg.english.usage['opts']

	print('{}: {} {}'.format( usage, pname, opts ))