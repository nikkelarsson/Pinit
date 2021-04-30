'''Installation script for Pinit.

If you wish, you can change the location for the installation. Remember
to also add the installation location to your PATH environment variable.'''

import getpass
import os
import sys

user = getpass.getuser()
install_location = '/Users/{}/Projects/bin/'.format(user)
args = sys.argv

def install(python_version='3.6'):
	'''Compile and symlink Pinit.'''
	
	comp_args = '--follow-imports --remove-output -o pinit'
	bin_dir_contents = os.listdir(install_location)
	src_dir_contents = os.listdir()
	src_dir_count = 0
	bin_dir_count = 0

	# Check if pinit is already compiled into cwd.
	# Reason: If a binary already exists it's not necessary to re-compile
	# (unless changes has been made to the program and new version would like
	# to be compiled). In this case the installation location
	# /Users/<username>/Projects/bin/ is scanned, and if no symlink to the
	# binary is found there then one can be created. In situation where
	# binary inside cwd isn't found, compiling can be done, followed by symlinking:
	# this symlinking can be performed by forcing it.
	for i in src_dir_contents:
		if i == 'pinit':
			src_dir_count += 1

	if src_dir_count == 0:
		os.system('python{} -m nuitka {} src/main.py'.format(python_version, comp_args))

	elif src_dir_count == 1:
		print('Found existing binary ”pinit” in current directory.')
		print('Would you like to compile anyway? (yes / no)')
		while True:
			try:
				comp_anyway = input('>>> ')
			except KeyboardInterrupt:
				sys.exit(1)

			if comp_anyway == 'yes':
				os.system('python{} -m nuitka {} src/main.py'.format(python_version, comp_args))
				break
			elif comp_anyway == 'no':
				break
			else:
				continue

	for i in bin_dir_contents:
		if i == 'pinit':
			bin_dir_count += 1

	if bin_dir_count == 0:
		os.system('ln -sf "$(pwd)/pinit" {}'.format(install_location))

	elif bin_dir_count == 1:
		#os.system('ln -sf "$(pwd)/pinit" {}'.format(install_location))
		pass

if __name__ == '__main__':
	install()
