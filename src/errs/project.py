
"""
File: project.py  
Desc: --
"""


def exists(name: str, language: str="eng") -> None:
	if language == "fi":
		error_msg: str = "Virhe: ”{}” on jo olemassa.".format(name)
	elif language == "eng":
		error_msg: str = "Error: ”{}” already exists.".format(name)
	return error_msg
