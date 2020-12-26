import os
import sys
import argparse
#import getpass
from help_messages import *
#from functions import *

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
        '--add-readme',
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
        # If --silent is provided as is (or with argument 'on'), silence the output
        const='on',
        # If --silent isn't present, enable verbose output
        default='off',
        )

mainparser.add_argument(
        '--add-gitignore',
        help=argparse.SUPPRESS,
        nargs='?',
        choices=['yes', 'no', ''],
        # If --add-gitignore is provided as is or with arg 'yes', then create .gitignore
        const='yes',
        # If --add-gitignore isn't present, or it is --add-gitignore=no
        # then don't create .gitignore
        default='no',
        )

# Display help for optional args
help_msgs_opt = mainparser.add_argument_group(
        title='optional arguments',
        description=f'''{help_msg}{version_msg}{readme_msg}{gitign_msg}''',
        )

# Display help for required args
help_msgs_req = mainparser.add_argument_group(
        title='project creation',
        description=f'''{project_msg}''',
        )

# Read arguments from the command line
args = mainparser.parse_args()

# When flag 'project' is used, then...
if args.project:
    # Save it to a variable
    project = args.project
    # If --silent is used then silence output...
    if 'on' in args.silent:
        try:
            # Create the project folder
            os.mkdir(project[0])
        except:
            print(f'Project [{project[0]}] already exists...')
            sys.exit(1)

    # If --silent isn't used or user assings 'off' as argument to it, in that case
    # let the output be verbose...
    else:
        try:
            # Create the project folder
            print(f'> Attempting to create folder [{project[0]}]...')
            os.mkdir(project[0])
            print(f'> Folder [{project[0]}] succesfully created!')
        except:
            print(f'Project [{project[0]}] already exists...')
            sys.exit(1)

# If --add-readme is invoked, then...
if args.add_readme:
    # Save it into a variable
    readme = args.add_readme
    # If --add-readme or --add-readme=yes is used...
    if 'yes' in readme:
        # Check that folder's been created
        if project:
            # If --silent or --silent=on is used, don't enable verbose output...
            if 'on' in args.silent:
                try:
                    # Go to the created folder
                    os.chdir(project[0])
                except RuntimeError:
                    print(f'Error occured during README file creation, while tried to change directory to {project[0]}...')
                    sys.exit(1)
                try:
                    # Create the README
                    with open('README.md', 'w', encoding='utf-8') as f:
                        f.write('')
                        # Save the state of README existence into a variable...
                        readme_exists = True
                except UnicodeError:
                    print('Error occured when tried to create README file...')
                    sys.exit(1)
            # If --silent isn't used or it is used as --silent=off
            else:
                try:
                    # Go to the created folder first before trying to create the README.md...
                    print(f'> Trying to access [{project[0]}] in order to create file(s)...')
                    os.chdir(project[0])
                    print(f'> Accessed [{project[0]}]!')
                except RuntimeError:
                    print(f'Error occured during README.md creation, while tried to change dir to {project[0]}...')
                    sys.exit(1)
                try:
                    # Create the README
                    print(f'> Attempting to create README.md...')
                    with open('README.md', 'w', encoding='utf-8') as f:
                        f.write('')
                        # Save the state of README existence into a variable...
                        readme_exists = True
                    print('> README.md successfully created!')
                except UnicodeError:
                    print('Error occured when tried to create README.md...')
                    sys.exit(1)

    # If --add-readme isn't present or it is --add-readme=no
    elif 'no' in readme:
        # If --silent is used, silence output...
        if 'on' in args.silent:
            pass
        else:
            print('> Skipping README.md creation... [YOU CAN CREATE IT LATER!]')

# When --add-gitignore is used...
if args.add_gitignore:
    # Save it into a variable
    gitign = args.add_gitignore
    # Check if --add-gitignore or --add-gitignore=yes is present...
    if 'yes' in gitign:
        # Make sure that project folder exists...
        if project:
            # Keep output silent if --silent has been provided...
            if 'on' in args.silent:
                try:
                    # If readme is already created, it means that cwd should already be
                    # 'project', in the case of which cd'ing into project isn't possible...
                    if readme_exists == True:
                        pass
                    else:
                        # Go to the created folder
                        os.chdir(project[0])
                except RuntimeError:
                    print(f'Error occured during .gitignore creation, while tried to change directory to {project[0]}...')
                    sys.exit(1)
                try:
                    # Create the .gitignore
                    with open('.gitignore', 'w', encoding='utf-8') as f:
                        f.write('')
                except UnicodeError:
                    print('Error occured when tried to create .gitignore...')
                    sys.exit(1)
            # Enable verbose output when --silent isn't present
            if 'off' in args.silent:
                try:
                    # If readme is already created, it means that cwd should already be
                    # 'project', in the case of which cd'ing into project isn't possible...
                    if readme_exists == True:
                        pass
                    else:
                        # Go to project folder
                        print(f'> Trying to access [{project[0]}] in order to create file(s)...')
                        os.chdir(project[0])
                        print(f'> Accessed [{project[0]}]!')
                except RuntimeError:
                    print(f'Error occured during .gitignore creation, while tried to change directory to {project[0]}...')
                    sys.exit(1)
                try:
                    print(f'> Attempting to create .gitignore...')
                    with open('.gitignore', 'w', encoding='utf-8') as f:
                        f.write('')
                    print(f'> .gitignore successfully created!')
                except UnicodeError:
                    print('Error occured when tried to create .gitignore...')
                    sys.exit(1)
    
    # If --add-gitignore isn't present or is present as --add-gitignore=no...
    if 'no' in gitign:
        # Silence output if --silence was present...
        if 'on' in args.silent:
            pass
        else:
            print(f'> Skipping .gitignore creation... [YOU CAN CREATE IT LATER!]')

# If --silent is used, don't print succession message at the end...
if 'on' in args.silent:
        pass
else:
        # Print this at the end of the initialization
        print(f'> Project [{project[0]}] successfully created!')
