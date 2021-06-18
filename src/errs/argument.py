
"""
 *  File: argument.py  
 *  Desc: Command line argument related errors.
 *  Auth: Niklas Larsson
"""


def excess(arguments: list, language: str="eng") -> None:
	"""Error given when excess arguments for some command or flag are provided."""
	excess_args: str = " ".join("”{}”".format(i) for i in arguments)
	# Another way to put the above expression; maybe a little messier though...
	#excess_args: str = " ".join("”" + i + "”" for i in arguments)
	if language == "fi":
		if len(arguments) > 1:
			error_msg: str = "Virhe: Argumentit {} ylimääräisiä.".format(excess_args)
		elif len(arguments) == 1:
			error_msg: str = "Virhe: Argumentti {} ylimääräinen.".format(excess_args)
	elif language == "eng":
		if len(arguments) > 1:
			error_msg: str = "Error: Arguments {} are redundant.".format(excess_args)
		elif len(arguments) == 1:
			error_msg: str = "Error: Argument {} is redundant.".format(excess_args)
	return error_msg


def invalid(argument: str, language: str="eng") -> None:
	"""Error given when argument user provides is invalid."""
	if language == "fi":
		error_msg: str = "Virhe: Tuntematon argumentti ”{}”.".format(argument)
	elif language == "eng":
		error_msg: str = "Error: Unrecognized argument ”{}”.".format(argument)
	return error_msg
