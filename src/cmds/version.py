
'''
File : version.py  
Desc : Version description.
'''


def get(program: str, version: str) -> None:
	'''Print Pinit's current version.'''
	print('{0} {1}'.format( program[0].upper() + program[1:].lower(), version ))
