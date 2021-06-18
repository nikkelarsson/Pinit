
"""
 *  File: version.py  
 *  Desc: Version description command.
 *  Auth: Niklas Larsson
"""


def get(program: str, version: str) -> None:
	"""Print program version."""
	print('{0} {1}'.format(program.title(), version))
