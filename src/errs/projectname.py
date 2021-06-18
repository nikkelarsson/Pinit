
"""
 *  File: projectname.py  
 *  Desc: Errors related to project name things.
 *  Auth: Niklas Larsson
"""


def invalid(project_name: str, language: str='eng') -> str:
	"""Error given when invalid kind of name for project is given."""
	if language == 'fi':
		error_msg: str = """
		Virhe: Huono nimeämiskäytäntö ”{}”, projektia ei luotu.
		""".format(project_name)
	elif language == 'eng':
		error_msg: str = """
		Error: Bad naming convention ”{}”, project wasn't created.
		""".format(project_name)
	return error_msg


def missing(language: str='eng') -> str:
	"""Error given when user forgot to provide name for a project."""
	if language == 'fi':
		error_msg: str = "Virhe: <nimi> puuttuu."
	elif langage == 'eng':
		error_msg: str = "Error: <name> missing."
	return error_msg
