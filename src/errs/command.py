
'''
file : command.py  
desc : Command related errors.
'''

def is_invalid(cmd, language='eng'):
	'''Error given when a command presented is invalid.'''

	if language == 'fi':
		msg = 'Virhe: Tuntematon komento ”{}”'.format(name)
	elif language == 'eng':
		msg = 'Error: Unrecognized command ”{}”'.format(name)
	print(msg)
