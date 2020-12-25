import os
import sys
import argparse
import getpass
from help_messages import *

# Initiate the mainparser. This section covers some basic things for the program.
mainparser = argparse.ArgumentParser(
		prog='pinit',
		add_help=False,
		argument_default=argparse.SUPPRESS,
		formatter_class=argparse.RawDescriptionHelpFormatter,
		usage='%(prog)s [PROJECT]... [OPTIONS]',
		description='''%(prog)s is command line tool designed to make project creation fast and smooth.''',
		epilog='''Hopefully this tool impoves your workflow...''',
		allow_abbrev=False,
		prefix_chars='-/',
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

mainparser.add_argument(
		'-s', '--silent',
		help=argparse.SUPPRESS,
		nargs='?',
		# If --silent is provided as is, silence the output
		const='on',
		# If --silent isn't present, enable verbose output
		default='off',
		)

# Display help for optional args
help_msgs_opt = mainparser.add_argument_group(
		title='optional arguments',
		description=f'''{help_msg}{version_msg}{readme_msg}''',
		)

# Display help for required args
help_msgs_req = mainparser.add_argument_group(
		title='project creation',
		description=f'''{project_msg}''',
		)

# Read arguments from the command line
args = mainparser.parse_args()

# Define 'project' argument actions here
if args.project:
	project = args.project

	# If --silent is used then silence output...
	if 'on' in args.silent:
		try:
			# Create the project folder
			os.mkdir(project[0])
		except:
			print(f'Project [{project[0]}] already exists...')
			sys.exit(1)
	else:
		try:
			# Create the project folder
			os.mkdir(project[0])
			print(f'> Initializing project [{project[0]}]...')
			print(f'> Creating folder for project [{project[0]}]...')
			print(f'> Project folder [{project[0]}] created...')
		except:
			print(f'Project [{project[0]}] already exists...')
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
				print(f'Error occured during README file creation, while tried to change directory to {project[0]}...')
				sys.exit(1)

			if 'on' in args.silent:
				try:
					# Create the README
					with open('README.md', 'w', encoding='utf-8') as f:
						f.write('')
				except UnicodeError:
					print('Error occured when tried to create README file...')
					sys.exit(1)
			else:
				try:
					# Create the README
					with open('README.md', 'w', encoding='utf-8') as f:
						f.write('')
					print('> Creating README.md file...')
					print('> README.md file created...')
					print(f'> [README.md]: Location: [{project[0]}]')
				except UnicodeError:
					print('Error occured when tried to create README file...')
					sys.exit(1)

	elif 'no' in readme:
		if 'on' in args.silent:
			pass
		else:
			print('> Skipping README.md file creation... [YOU CAN CREATE IT LATER!]')

	if 'on' in args.silent:
		pass
	else:
		# Print this at the end of the initialization
		print(f'> Project [{project[0]}] successfully created!')
