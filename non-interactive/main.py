import os
import sys
import argparse
import getpass

# Initiate the mainparser. This section covers some basic things for the program.
mainparser = argparse.ArgumentParser(
		prog='pinit',
		add_help=False,
		argument_default=argparse.SUPPRESS,
		formatter_class=argparse.RawDescriptionHelpFormatter,
		usage='%(prog)s [PROJECT]... [OPTIONS]',
		description='''
%(prog)s is command line tool designed to make project creation fast and smooth.
		''',
		epilog='''
Hopefully this tool impoves your workflow...
		''',
		allow_abbrev=False,
		)

# Override default --help
mainparser.add_argument(
		'-h', '--help',
		action='help',
		help=argparse.SUPPRESS,
		default=argparse.SUPPRESS,
		)

mainparser.add_argument(
		'-V', '--version',
		help=argparse.SUPPRESS,
		action='version',
		version='%(prog)s 0.1',
		)

mainparser.add_argument(
		'project',
		type=str,
		help=argparse.SUPPRESS,
		nargs=1,
		)

mainparser.add_argument(
		'-R', '--add-readme',
		help=argparse.SUPPRESS,
		nargs='?',
		choices=['yes', 'no', ''],
		# If --add-readme is present without arguments, then create readme
		const='yes',
		# If --add-readme isn't present, don't create readme
		default='no',
		)

help_menu_optional_arguments_parser = mainparser.add_argument_group(
		title='optional arguments',
		description='''
-h, --help\t\t\t\t\tshow this message and exit
-V, --version\t\t\t\t\tprint program version and exit
		''',
		)

help_menu_required_arguments_parser = mainparser.add_argument_group(
		title='project creation',
		description='''
NAME\t\t\t\t\t\t\tdefine name for the project
-R, --add-readme\t\t\t\tcreate README.md file
		''',
		)

# Read arguments from the command line
args = mainparser.parse_args()

# Define 'project' argument actions here
if args.project:
	project = args.project
	try:
		# Create the project folder
		os.mkdir(project[0])
		print(f'> Initializing project [{project[0]}]...')
		print(f'> Creating folder for project [{project[0]}]...')
		print(f'> Project folder [{project[0]}] created...')
	except:
		print(f'Project [{project[0]}] alreaedy exists...')
		sys.exit(1)

# Define '--add-readme' actions here
if args.add_readme:

	readme = args.add_readme

	if 'yes' in readme:
		# Check that folder's been created
		if project:
			
			try:
				# Go to the created folder
				os.chdir(project[0])
			except RuntimeError:
				print('Error occured during runtime, exiting...')
				sys.exit(1)

			try:
				# Create the README
				with open('README.md', 'w', encoding='utf-8') as f:
					f.write('')
				print('> Creating README.md file...')
				print('> README.md file created...')

			except UnicodeError:
				print('Unicode related error occured...')
				sys.exit(1)

	elif 'no' in readme:
		print('> Skipping README.md file creation... [YOU CAN CREATE IT LATER!]')

	# Print this at the end of the initialization
	print(f'> Project [{project[0]}] successfully created!')
