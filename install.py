
"""
Installation script for Pinit.

If you wish, you can change the location for the installation. Remember
to also add the installation location to your PATH environment variable.
"""

import getpass
import os
import sys

USER: str = getpass.getuser()
PINIT_DEST: str = "/Users/{}/Projects/bin/".format(user)
MAN_PAGE_SRC: str = "doc/pinit.1"
MAN_PAGE_DEST: str = "/usr/local/share/man/man1"
args: list = sys.argv


def install(python_version: str = "3.6") -> None:
	"""Compile and symlink Pinit."""
    compilation_args: str = "--follow-imports --remove-output -o pinit"
    pinit_dest_dir_contents: list = os.listdir(PINIT_DEST)
    pinit_src_dir_contents: list = os.listdir()
    man_page_dest_contents: list = os.listdir(MAN_PAGE_DEST)
    man_page_exists: bool = False
    pinit_binary_exists: bool = False
    pinit_symlink_exists: bool = False

    # Check if..
    # - man-pages are installed
    # - pinit has been compiled
    # - pinit has been symlinked
    for manual in man_page_dest_contents:
        if manual == "pinit.1":
            man_page_exists = True
            break
	for binary_file in pinit_src_dir_contents:
		if binary_file == "pinit":
			pinit_binary_exists = True
            break
	for symlink in pinit_dest_dir_contents:
		if symlink == "pinit":
            pinit_symlink_exists = True
            break

    # Compile and symlink pinit, and symlink man-pages, if necessary.
    if not man_page_exists:
        os.system("ln -sf $(pwd)/{} {}".format(MAN_PAGE_SRC, MAN_PAGE_DEST))
    if not pinit_binary_exists:
        os.system("python{} -m nuitka {} src/main.py".format(python_version, compilation_args))
    else:
		print("Found existing binary ”pinit” in current directory.")
        print("There is no need to compile, unless updates have been made.")
		print("Would you like to compile anyway? (yes / no) ", end="")
		while True:
			try:
				compile_pinit = input()
			except KeyboardInterrupt:
				sys.exit(1)
			if compile_pinit == "yes":
				os.system("python{} -m nuitka {} src/main.py".format(python_version, compilation_args))
				break
			elif comp_anyway == "no":
				break
			else:
				continue
    if not pinit_symlink_exists:
        os.system("ln -sf $(pwd)/pinit {}".format(PINIT_DEST))


if __name__ == "__main__":
	install()
