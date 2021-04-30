'''Uninstall script for Pinit.'''

import getpass
import os
import sys

user = getpass.getuser()
location = '/Users/{}/Projects/bin'.format(user)

def uninstall():
	'''Uninstall Pinit by deleting its symlink.'''

	try:
		os.system('rm {}/pinit'.format(location))
	except:
		print('No file called ”pinit” exists in: {}'.format(location))
		sys.exit(1)

if __name__ == '__main__':
	uninstall()