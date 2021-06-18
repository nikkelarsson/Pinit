
"""
 *  File: main.py  
 *  Desc: Pinit – Handy project creation tool.
 *  Auth: Niklas Larsson <nikke.larsson@gmail.com>
"""

# Imports are sorted alphabetically here.
import cfg
import globs
import routing
import sys

args: list = sys.argv
def main(arguments: list=args) -> None:
	routing.route(arguments, globs.SETTINGS)


if __name__ == '__main__':
	main()
