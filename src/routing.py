
"""
 *  File: routing.py  
 *  Desc: User input routing.
 *  Auth: Niklas Larsson
"""

# TODO: For longer and more complex commands, handle them here like:
# handle_<commandname1>.py
# handle_<commandname2>.py
# and etc etc...

import cmds
import errs
import globs
import sys
import textwrap

silent: bool = False # Right now, this has no purpose.

# Map arguments to functions respectively here.
# For example:
#
#   "--help" : globs.descriptions.descriptions(),
#   "--version" : cmds.version.get()
#
# Or actually more like this:
#
#   cmds.flags["help"]["short"] : globs.descriptions.descriptions()
#   cmds.flags["help"]["long"] : cmds.version.get()
HANDLE_ARGS: dict = {
		cmds.flags["help"]["short"] : globs.descriptions.descriptions(),
		}


def route(args: list, settings: dict) -> None:
	"""Take user input from commandline, and handle it accordingly."""
	if len(args) < 2:
		globs.descriptions.usage()

	count: int = 0
	# Iterate through arguments here, that are gathered from command line
	# and handle each argument respectively.
	for arg in args:
		# So, here, handle each argument, and if an argument is invalid,
		# then execute the ’default’ option, which can be the invalid
		# argument error.
		#HANDLE_ARGS.get(arg, default) # <= Prototype.
		if count > 0:
			HANDLE_ARGS.get(arg, errs.argument.invalid(args[1], settings["language"]))
		elif not count >= 1:
			count += 1

 #	# --help
 #	if (args[1] == cmds.flags["help"]["short"]) \
 #	or (args[1] == cmds.flags["help"]["long"]):
 #		if args[2:]:
 #			print(errs.argument.excess(args[2:], settings["language"]))
 #			sys.exit(1)
 #          # Could this be done also like this, all in one line?
 #          sys.exit(errs.argument.excess(args[2:], settings["language"]))
 #		globs.descriptions.descriptions()
 # 
 #	# --version
 #	elif (args[1] == cmds.flags["version"]["short"]) \
 #	or (args[1] == cmds.flags["version"]["long"]):
 #		if args[2:]:
 #			print(errs.argument.excess(args[2:], settings["language"]))
 #			sys.exit(1)
 #          # Could this be done also like this, all in one line?
 #          sys.exit(errs.argument.excess(args[2:], settings["language"]))
 #		cmds.version.get(settings["program"], settings["version"])
 # 
 #	# create
 #	elif (args[1] == cmds.commands["create"]["long"]):
 #		if not args[2:]:
 #			print(errs.projectname.missing(settings["language"]))
 #			sys.exit(1)
 #		if args[3:]:
 #			print(errs.argument.excess(args[3:], settings["language"]))
 #			sys.exit(1)
 #          # Could this be done also like this, all in one line?
 #          sys.exit(errs.argument.excess(args[2:], settings["language"]))
 #		# This message contains either an error status message, or the
 #		# success message, which is the ”Project X was created successfully.”.
 #		status_msg: str = cmds.create.project(args[2], settings["language"])
 #		if status_msg == "PROJECT_NAME_INVALID":
 #			print(textwrap.dedent(errs.projectname.invalid(args[2], settings["language"])).strip())
 #			sys.exit(1)
 #		elif status_msg == "INVALID_PATH":
 #			print(errs.path.invalid(args[2], settings["language"]))
 #			sys.exit(1)
 #		elif status_msg == "PROJECT_EXISTS":
 #			print(errs.project.exists(args[2], settings["language"]))
 #			sys.exit(1)
 #		else:
 #			print(status_msg)
 # 
 #	else:
 #		print(errs.argument.invalid(args[1], settings["language"]))
 #		sys.exit(1)
