
'''
File : main.py
Desc : Body for the main program.
'''

# Imports are sorted alphabetically here.
import cmds
import cfg
import errs
import os
import requests
import sys

args     : list = sys.argv
commands : dict = cmds.commands
flags    : dict = cmds.flags

PROGRAM  : str  = cfg.name
VERSION  : str  = cfg.version
LANGUAGE : str  = cfg.language

def init_descriptions() -> None:
	if LANGUAGE == 'fi':
		descriptions = cmds.help.Finnish(PROGRAM, VERSION)
	elif LANGUAGE == 'eng':
		descriptions = cmds.help.English(PROGRAM, VERSION)


def main(arguments: list = args) -> None:

	init_descriptions()

	if len(arguments) < 2:
		descriptions.usage()
		sys.exit(1)

	# TODO: Move this stuff to a separate file / files, and then import that / them here.
	# Why? Let's keep this file clean and concise.
	elif len(arguments) >= 2:
		if args[1] == flags['version']['short']:
			if args[2:]: sys.exit(1)
			cmds.version.get(__program__, __version__)
		elif args[1] == flags['version']['long']:
			if args[2:]: sys.exit(1)
			cmds.version.get(__program__, __version__)
		elif args[1] == flags['help']['short']:
			if args[2:]: sys.exit(1)
			descriptions.descriptions()
		elif args[1] == flags['help']['long']:
			if args[2:]: sys.exit(1)
			descriptions.descriptions()

		elif args[1] == flags['verbose']['short']:
			if args[2:]:
				if args[2] == commands['create']['long']:
					if args[3:]:
						verbose_message = cmds.create.files(args[3:], __language__, verbose=True)
						if verbose_message == 'INVALID_FILENAME':
							errs.file.invalid_filename(args[3], __language__)
							sys.exit(1)
						elif verbose_message == 'FILE_ALREADY_EXISTS':
							errs.file.exists(args[3], __language__)
							sys.exit(1)
						elif verbose_message == 'FILE_NOT_FOUND':
							errs.file.not_found(path=args[3], language=__language__)
							sys.exit(1)
						else:
							print(verbose_message)
					else:
						errs.file.name_missing(language=__language__)
						sys.exit(1)
				else:
					errs.command.is_invalid(cmd=args[2], language=__language__)
					sys.exit(1)
			else:
				sys.exit(1)

if __name__ == '__main__':
	main()
