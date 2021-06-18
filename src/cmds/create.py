
"""
 *  File: create.py  
 *  Desc: Project / creation procedures.
 *  Auth: Niklas Larsson
"""

# TODO: Windows compatibility? - This is mostly about the backslashes,
# as Unix based systems uses forward slashes.

# TODO: Is it actually necessary to be able to create projects to custom
# locations? Because probably the use case is usually that, when one
# wishes to create a new project user already is in the right location thus,
# it kind of would be just useless, no?

import getpass
import os
import string

ENCODING: str = "utf-8"
USERNAME: str = getpass.getuser()

INVALID_PREFIXES: tuple = (
		"@", "*", "-", "=", "+", "&", "€", "/",
		"\\", "^", "(", ")", "[", "]", "{", "}"
		)
INVALID_SUFFIXES: tuple = (
		"@", "*", "-", "=", "+", "&", "€", "/",
		"\\", "^", "(", ")", "[", "]", "{", "}"
		)


def project(name: str, language: str="eng", git: bool=False) -> str:
	"""Create new python project."""
	forward_slashes: bool = "/" in name

	if language == "fi":
		success_msg: str = "Luotiin uusi projekti ”{}”.".format(name.lower())
	elif language == "eng":
		success_msg: str = "Created new project ”{}”.".format(name.lower())

	# To avoid problems, prohibit use of
	# certain characters as prefix and suffix.
	if name.startswith(INVALID_PREFIXES):
		return "PROJECT_NAME_INVALID"
	elif name.endswith(INVALID_SUFFIXES):
		return "PROJECT_NAME_INVALID"

	# Allow using the ”~/” abbreviation; it's nicer to write less.
	# This is used because os module does not allow using the ~/
	# abbreviation, so it must be done manually here.
	elif name.startswith("~/"):
		name.replace("~/", "/Users/{}/".format(USERNAME))

	if forward_slashes:
		# Split the path, for example /Users/<user>/Documents/, like:
		# "", "Users", "<user>", "Documents", ""
		path_split: list = name.split("/")
		# Iterate through the given path and, if any section of the
		# given path is invalid, return an error; there is no need
		# to check the validity of every part of the given path as,
		# if any of the parts turns out to be invalid, then we already
		# know, that the path is not going to be valid anyway.
		for part in path_split:
			# When the path user provides starts, or ends with a forward slash,
			# those first and last forward slashes are going to be empty
			# items in the path_split, thus, they need to be ignored, as they
			# would count as invalid sections in the path.
			#
			# First, check the first section of the path, like: /Users/
			# Then, check the second, like: /Users/<user>/, and so on...
			if part != "":
				if not os.path.exists(part):
					return "INVALID_PATH"

		# After validating the path, check that no existing
		# project with same name exists in the location.
		if os.path.exists(name):
			return "PROJECT_EXISTS"
		# Project-dir
		os.mkdir(name.lower())
		# Source-dir
		os.mkdir("{}/src".format(name.lower()))
		# Readme
		with open("{}/README.md".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("# {}".format(name.title()))
		# Changelog
		with open("{}/CHANGELOG.md".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("# Changelog")
		# src/main.py
		with open("{}/src/main.py".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("\n\"\"\"\n")
			f.write("File: main.py  \nDesc: --  \nAuth: {} <email>".format(USERNAME))
			f.write("\n\"\"\"\n")
			f.write("\n\ndef main() -> None:\n\tpass\n")
			f.write("\n\nif __name__ == \"__main__\":\n\tmain()")
		# src/__init__.py
		with open("{}/src/__init__.py".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("\n\"\"\"\n")
			f.write("File: __init__.py  \nDesc: --")
			f.write("\n\"\"\"")
		return success_msg

	else:
		if os.path.exists(name):
			return "PROJECT_EXISTS"
		# Project-dir
		os.mkdir(name.lower())
		# Source-dir
		os.mkdir("{}/src".format(name.lower()))
		# Readme
		with open("{}/README.md".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("# {}".format(name.title()))
		# Changelog
		with open("{}/CHANGELOG.md".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("# Changelog")
		# src/main.py
		with open("{}/src/main.py".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("\n\"\"\"\n")
			f.write("File: main.py  \nDesc: --  \nAuth: {} <email>".format(USERNAME))
			f.write("\n\"\"\"\n")
			f.write("\n\ndef main() -> None:\n\tpass\n")
			f.write("\n\nif __name__ == \"__main__\":\n\tmain()")
		# src/__init__.py
		with open("{}/src/__init__.py".format(name.lower()), "w", encoding=ENCODING) as f:
			f.write("\n\"\"\"\n")
			f.write("File: __init__.py  \nDesc: --")
			f.write("\n\"\"\"")
		return success_msg
