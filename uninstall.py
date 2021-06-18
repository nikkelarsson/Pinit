
"""Uninstall script for Pinit."""

import getpass
import os
import sys

USER: str = getpass.getuser()
PINIT_DEST_LOCATION: str = "/Users/{}/Projects/bin".format(user)
MAN_PAGE_DEST: str = "/usr/local/share/man/man1"


def uninstall() -> None:
	"""Uninstall Pinit and all the associated
    files by deleting their symlinks."""
	try:
        print("Attempting to uninstall pinit...")
		os.system("rm {}/pinit".format(location))
	except:
		sys.exit("”Pinit” is not installed.")
    try:
        os.system("rm {}/pinit.1".format(MAN_PAGE_DEST))
    except:
        pass


if __name__ == "__main__":
	uninstall()
