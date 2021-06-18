
'''
File : command.py  
Desc : Command related errors.
'''

import sys


def is_invalid(cmd: str, language: str='eng') -> None:
	'''Error given when a command presented is invalid.'''
	if language == 'fi':
		msg = 'Virhe: Tuntematon argumentti ”{}”'.format(cmd)
	elif language == 'eng':
		msg = 'Error: Unrecognized argument ”{}”'.format(cmd)
	print(msg)
	sys.exit(1)


def invalid_type(cmd: str, language: str='eng') -> None:
	'''Error given when a command-type is not valid.'''
	if language == 'fi':
		msg = 'Virhe: Etuliite ”{}” ei tuettu'.format(cmd[0])
	elif language == 'eng':
		msg = 'Error: Prefix ”{}” unsupported'.format(cmd[0])
	print(msg)
	sys.exit(1)


def missing_args(language: str='eng') -> None:
	'''Error given when a command is missing its mandatory arguments.'''
	if language == 'fi':
		msg = 'Virhe: Ei tarpeeksi argumentteja.'
	elif language == 'eng':
		msg = 'Error: Not enough arguments.'
	print(msg)
	sys.exit(1)
