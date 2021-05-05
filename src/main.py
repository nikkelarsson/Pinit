
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

args         : list = sys.argv
commands     : dict = cmds.commands
flags        : dict = cmds.flags
__program__  : str  = cfg.name
__version__  : str  = cfg.version
__language__ : str  = cfg.language

def init_descriptions():
	if __language__ == 'fi':
		descriptions = cmds.help.Finnish(__program__, __version__)
	elif __language__ == 'eng':
		descriptions = cmds.help.English(__program__, __version__)

# TODO: Clean this area up: separate parts into their own modules.
def main():
	init_descriptions()

	if len(args) < 2:
		descriptions.usage()
		sys.exit(1)

	elif len(args) >= 2:
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






# if len(sys.argv) == 2:
# 	if sys.argv[1] == flags['create']['long']:
# 		if language == 'us':
# 			print('Error: argument <NAME> missing')
# 			sys.exit(1)
# 		elif language == 'fi':
# 			print('Virhe: argumentti <NIMI> puuttuu')
# 			sys.exit(1)
# 		else:
# 			print('Error: argument <NAME> missing')
# 			sys.exit(1)

# 	elif sys.argv[1] == flags['help']['short']:
# 		functions.printHelp()

# 	elif sys.argv[1] == flags['help']['long']:
# 		functions.printHelp()

# 	elif sys.argv[1] == flags['version']['short']:
# 		print(banner)
# 		functions.printProgramVersion()

# 	elif sys.argv[1] == flags['version']['long']:
# 		print(banner)
# 		functions.printProgramVersion()

# 	else:
# 		if sys.argv[1] == flags['verbose']['short']:
# 			if language == 'us':
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tarkista ”{}” käyttö käyttämällä joko ”-h” tai ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['verbose']['long']:
# 			if language == 'us':
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tarkista ”{}” käyttö käyttämällä joko ”-h” tai ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['initasgit']['short']:
# 			if language == 'us':
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tarkista ”{}” käyttö käyttämällä joko ”-h” tai ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['initasgit']['long']:
# 			if language == 'us':
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tarkista ”{}” käyttö käyttämällä joko ”-h” tai ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: check usage of ”{}” using either ”-h” or ”--help”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		else:
# 			if language == 'us':
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
# Important stuff to note here!
# In general, there are few important rools that apply throughout this whole code.

# 1. Requesting help and program version is only allowed as ==> pinit -h / pinit -V
# What I mean with this is that these two flags work only by themselves: they cannot
# be used in conjunction with other flags or commands.

# 2. Naming a project with a name that starts with ”-” characters is prohibited.
# This is to generally avoid the accident of creating a project with ”invalid” name.

# 3. Also, project must always have a name so that is checked as well over and over
# through this code.

# 4. Creating duplicate folders with the same name is prohibited.

# The reason this stuff is covered here is because these rules apply over and over.
# There might be some leftover comments laying around here and there though.
# NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE

# if len(sys.argv) == 3:

# 	'''
# 	Create new projects in current working directory or in custom location.
# 	When creating in custom location the syntax is: pinit create path/to/myproject
# 	'''

# 	if sys.argv[1] == flags['create']['long']:
# 		if sys.argv[2] == '':
# 			if language == 'us':
# 				print('Error: argument <NAME> missing')
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: argumentti <NIMI> puuttuu')
# 				sys.exit(1)
# 			else:
# 				print('Error: argument <NAME> missing')
# 				sys.exit(1)

# 		elif sys.argv[2][0] == '-':
# 			if language == 'us':
# 				print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 				sys.exit(1)

# 		elif sys.argv[2][0:1] == '-':
# 			if language == 'us':
# 				print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 				sys.exit(1)

# 		# This is essentially the same check as the previous ones:
# 		# check that no ”-” characters were used in project name.
# 		slashesFound = functions.checkForSlashes(sys.argv[2])

# 		if slashesFound == 1:
# 			pass

# 		else:
# 			projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[2])

# 			if projectnameExtractedFromThePath[0] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif projectnameExtractedFromThePath[0:1] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 					sys.exit(1)

# 		# Final check: make sure no duplicates exist.
# 		if os.path.exists(sys.argv[2]):
# 			if language == 'us':
# 				print('Error: project with a name ”{}” already exists'.format(sys.argv[2]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[2]))
# 				sys.exit(1)
# 			else:
# 				print('Error: project with a name ”{}” already exists'.format(sys.argv[2]))
# 				sys.exit(1)

# 		else:
# 			functions.createFiles(sys.argv[2])

# 	else:
# 		if sys.argv[1] == flags['help']['short']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['help']['long']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['version']['short']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['version']['long']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['verbose']['short']:
# 			if sys.argv[2] == flags['create']['long']:
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 		elif sys.argv[1] == flags['verbose']['long']:
# 			if sys.argv[2] == flags['create']['long']:
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 		elif sys.argv[1] == flags['initasgit']['short']:
# 			if sys.argv[2] == flags['create']['long']:
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 		elif sys.argv[1] == flags['initasgit']['long']:
# 			if sys.argv[2] == flags['create']['long']:
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 		else:
# 			if language == 'us':
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# if len(sys.argv) == 4:
# 	if sys.argv[1] == flags['verbose']['short']:
# 		if sys.argv[2] == flags['create']['long']:
# 			if sys.argv[3] == '':
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 			elif sys.argv[3][0] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			elif sys.argv[3][0:1] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			# This is essentially the same check as the previous ones:
# 			# check that no ”-” characters were used in project name.
# 			slashesFound = functions.checkForSlashes(sys.argv[3])

# 			if slashesFound == 1:
# 				pass

# 			else:
# 				projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[3])

# 				if projectnameExtractedFromThePath[0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif projectnameExtractedFromThePath[0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 			# Final check: make sure no duplicates exist.
# 			if os.path.exists(sys.argv[3]):
# 				if language == 'us':
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 			else:
# 				functions.createFiles(sys.argv[3])
# 				if language == 'us':
# 					print('Created ”{}” successfully.'.format(sys.argv[3]))
# 				elif language == 'fi':
# 					print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[3]))
# 				else:
# 					print('Created ”{}” successfully.'.format(sys.argv[3]))

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['changemdfilescaps']['short']:
# 				if sys.argv[3] == flags['create']['long']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			elif sys.argv[2] == flags['changemdfilescaps']['long']:
# 				if sys.argv[3] == flags['create']['long']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	elif sys.argv[1] == flags['verbose']['long']:
# 		if sys.argv[2] == flags['create']['long']:
# 			if sys.argv[3] == '':
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 			elif sys.argv[3][0] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			elif sys.argv[3][0:1] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			# This is essentially the same check as the previous ones:
# 			# check that no ”-” characters were used in project name.
# 			slashesFound = functions.checkForSlashes(sys.argv[3])

# 			if slashesFound == 1:
# 				pass

# 			else:
# 				projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[3])

# 				if projectnameExtractedFromThePath[0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif projectnameExtractedFromThePath[0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 			# Final check: make sure no duplicates exist.
# 			if os.path.exists(sys.argv[3]):
# 				if language == 'us':
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 			else:
# 				functions.createFiles(sys.argv[3])
# 				if language == 'us':
# 					print('Created ”{}” successfully.'.format(sys.argv[3]))
# 				elif language == 'fi':
# 					print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[3]))
# 				else:
# 					print('Created ”{}” successfully.'.format(sys.argv[3]))

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['changemdfilescaps']['short']:
# 				if sys.argv[3] == flags['create']['long']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			elif sys.argv[2] == flags['changemdfilescaps']['long']:
# 				if sys.argv[3] == flags['create']['long']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	elif sys.argv[1] == flags['changemdfilescaps']['short']:
# 		if sys.argv[2] == flags['create']['long']:
# 			if sys.argv[3] == '':
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 			elif sys.argv[3][0] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			elif sys.argv[3][0:1] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			# This is essentially the same check as the previous ones:
# 			# check that no ”-” characters were used in project name.
# 			slashesFound = functions.checkForSlashes(sys.argv[3])

# 			if slashesFound == 1:
# 				pass

# 			else:
# 				projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[3])

# 				if projectnameExtractedFromThePath[0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif projectnameExtractedFromThePath[0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 			# Final check: make sure no duplicates exist.
# 			if os.path.exists(sys.argv[3]):
# 				if language == 'us':
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 			else:
# 				functions.createFiles(sys.argv[3], capitalizedmarkdownfiles=True)

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['verbose']['short']:
# 				if sys.argv[3] == flags['create']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			elif sys.argv[2] == flags['verbose']['long']:
# 				if sys.argv[3] == flags['create']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	elif sys.argv[1] == flags['changemdfilescaps']['long']:
# 		if sys.argv[2] == flags['create']['long']:
# 			if sys.argv[3] == '':
# 				if language == 'us':
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: argumentti <NIMI> puuttuu')
# 					sys.exit(1)
# 				else:
# 					print('Error: argument <NAME> missing')
# 					sys.exit(1)

# 			elif sys.argv[3][0] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			elif sys.argv[3][0:1] == '-':
# 				if language == 'us':
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 					sys.exit(1)

# 			# This is essentially the same check as the previous ones:
# 			# check that no ”-” characters were used in project name.
# 			slashesFound = functions.checkForSlashes(sys.argv[3])

# 			if slashesFound == 1:
# 				pass

# 			else:
# 				projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[3])

# 				if projectnameExtractedFromThePath[0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif projectnameExtractedFromThePath[0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[3]))
# 						sys.exit(1)

# 			# Final check: make sure no duplicates exist.
# 			if os.path.exists(sys.argv[3]):
# 				if language == 'us':
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[3]))
# 					sys.exit(1)
# 				else:
# 					print('Error: project with a name ”{}” already exists'.format(sys.argv[3]))
# 					sys.exit(1)
# 			else:
# 				functions.createFiles(sys.argv[3], capitalizedmarkdownfiles=True)

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['verbose']['short']:
# 				if sys.argv[3] == flags['create']['long']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			elif sys.argv[2] == flags['verbose']['long']:
# 				if sys.argv[3] == flags['create']['long']:
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	else:
# 		if sys.argv[1] == flags['help']['short']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['help']['long']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['version']['short']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['version']['long']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['create']['long']:
# 			slashesFound = functions.checkForSlashes(sys.argv[2])
# 			if slashesFound == 1:
# 				if sys.argv[2][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)

# 				elif sys.argv[2][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 			else:
# 				projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[2])
# 				if projectnameExtractedFromThePath[0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)

# 				elif projectnameExtractedFromThePath[0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		else:
# 			if language == 'us':
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# if len(sys.argv) == 5:

# 	# Allow mixing short and long flags together.

# 	if sys.argv[1] == flags['verbose']['short']:
# 		if sys.argv[2] == flags['changemdfilescaps']['short']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		elif sys.argv[2] == flags['changemdfilescaps']['long']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['create']['long']:
# 				if sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: options must be presented before commands')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Error: valitsimet on annettava ennen komentoja')
# 						sys.exit(1)
# 					else:
# 						print('Error: options must be presented before commands')
# 						sys.exit(1)

# 				if sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: options must be presented before commands')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Error: valitsimet on annettava ennen komentoja')
# 						sys.exit(1)
# 					else:
# 						print('Error: options must be presented before commands')
# 						sys.exit(1)

# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[4]))
# 						sys.exit(1)
# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	elif sys.argv[1] == flags['verbose']['long']:
# 		if sys.argv[2] == flags['changemdfilescaps']['long']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		elif sys.argv[2] == flags['changemdfilescaps']['short']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	elif sys.argv[1] == flags['changemdfilescaps']['short']:
# 		if sys.argv[2] == flags['verbose']['short']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		elif sys.argv[2] == flags['verbose']['long']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 	elif sys.argv[1] == flags['changemdfilescaps']['long']:
# 		if sys.argv[2] == flags['verbose']['long']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		elif sys.argv[2] == flags['verbose']['short']:
# 			if sys.argv[3] == flags['create']['long']:
# 				if sys.argv[4] == '':
# 					if language == 'us':
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: argumentti <NIMI> puuttuu')
# 						sys.exit(1)
# 					else:
# 						print('Error: argument <NAME> missing')
# 						sys.exit(1)

# 				elif sys.argv[4][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				elif sys.argv[4][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 						sys.exit(1)

# 				# This is essentially the same check as the previous ones:
# 				# check that no ”-” characters were used in project name.
# 				slashesFound = functions.checkForSlashes(sys.argv[4])

# 				if slashesFound == 1:
# 					pass

# 				else:
# 					projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[4])

# 					if projectnameExtractedFromThePath[0] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 					elif projectnameExtractedFromThePath[0:1] == '-':
# 						if language == 'us':
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)
# 						elif language == 'fi':
# 							print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[4]))
# 							sys.exit(1)
# 						else:
# 							print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[4]))
# 							sys.exit(1)

# 				# Final check: make sure no duplicates exist.
# 				if os.path.exists(sys.argv[4]):
# 					if language == 'us':
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: projekti nimellä ”{}” on jo olemassa'.format(sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: project with a name ”{}” already exists'.format(sys.argv[4]))
# 						sys.exit(1)
# 				else:
# 					functions.createFiles(sys.argv[4], capitalizedmarkdownfiles=True)
# 					if language == 'us':
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))
# 					elif language == 'fi':
# 						print('Luotiin ”{}” onnistuneesti.'.format(sys.argv[4]))
# 					else:
# 						print('Created ”{}” successfully.'.format(sys.argv[4]))

# 			else:
# 				if sys.argv[3] == flags['help']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['help']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['short']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 				elif sys.argv[3] == flags['version']['long']:
# 					if language == 'us':
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid use of ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized argument ”{}”'.format(sys.argv[3]))
# 						sys.exit(1)

# 		else:
# 			if sys.argv[2] == flags['help']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['help']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['short']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)

# 			elif sys.argv[2] == flags['version']['long']:
# 				if language == 'us':
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: invalid use of ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 			else:
# 				if language == 'us':
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				elif language == 'fi':
# 					print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 				else:
# 					print('Error: unrecognized argument ”{}”'.format(sys.argv[2]))
# 					sys.exit(1)
# 	else:
# 		if sys.argv[1] == flags['help']['short']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['help']['long']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['version']['short']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['version']['long']:
# 			if language == 'us':
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: valitsimen ”{}” käyttö virheellinen'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: invalid use of ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# 		elif sys.argv[1] == flags['create']['long']:
# 			slashesFound = functions.checkForSlashes(sys.argv[2])
# 			if slashesFound == 1:
# 				if sys.argv[2][0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)

# 				elif sys.argv[2][0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized arguments ”{}” ”{}”'.format(sys.argv[3], sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntemattomat argumentit ”{}” ”{}”'.format(sys.argv[3], sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized arguments ”{}” ”{}”'.format(sys.argv[3], sys.argv[4]))
# 						sys.exit(1)
# 			else:
# 				projectnameExtractedFromThePath = functions.checkForSlashes(sys.argv[2])
# 				if projectnameExtractedFromThePath[0] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)

# 				elif projectnameExtractedFromThePath[0:1] == '-':
# 					if language == 'us':
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: virheellinen nimi ”{}”: merkkien ”-” käyttö etuliittenä kielletty'.format(sys.argv[2]))
# 						sys.exit(1)
# 					else:
# 						print('Error: invalid name ”{}”: using ”-” as prefix is prohibited'.format(sys.argv[2]))
# 						sys.exit(1)
# 				else:
# 					if language == 'us':
# 						print('Error: unrecognized arguments ”{}” ”{}”'.format(sys.argv[3], sys.argv[4]))
# 						sys.exit(1)
# 					elif language == 'fi':
# 						print('Virhe: tuntemattomat argumentit ”{}” ”{}”'.format(sys.argv[3], sys.argv[4]))
# 						sys.exit(1)
# 					else:
# 						print('Error: unrecognized arguments ”{}” ”{}”'.format(sys.argv[3], sys.argv[4]))
# 						sys.exit(1)
# 		else:
# 			if language == 'us':
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			elif language == 'fi':
# 				print('Virhe: tuntematon argumentti ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)
# 			else:
# 				print('Error: unrecognized argument ”{}”'.format(sys.argv[1]))
# 				sys.exit(1)

# # Preserving this setting here for now. When more flags get implemented this can be removed.
# if len(sys.argv) >= 6:
# 	if language == 'us':
# 		print('Error: too many arguments')
# 		sys.exit(1)
# 	elif language == 'fi':
# 		print('Virhe: liikaa argumentteja')
# 		sys.exit(1)
# 	else:
# 		print('Error: too many arguments')
# 		sys.exit(1)
