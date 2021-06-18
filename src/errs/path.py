
"""
 *  File: path.py
 *  Desc: Path operation related errors.
 *  Auth: Niklas Larsson
"""


def invalid(path: str, language: str="eng") -> str:
	"""Error given when path provided for project is invalid."""
	if language == "fi":
		error_msg: str = "Virhe: Polku ”{}” virheellinen".format(path)
	elif language == "eng":
		error_msg: str = "Error: Path ”{}” invalid".format(path)
	return error_msg
