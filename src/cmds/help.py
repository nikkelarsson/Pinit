
"""
 *  File: help.py  
 *  Desc: Command and usage descriptions.
 *  Auth: Niklas Larsson
"""

# TODO: Update English descriptions at some point.

#
# The output should look something like:
#
# <program> X.X, short description here.
# Usage: <program> [options]...
#
# <category name>:
#     -f,  --flags-here...............Description here.
#

import sys
import textwrap


class Language:
	"""Base class for descriptions."""

	def __init__(self, program: str, version: str):
		self.program: str = program
		self.version: str = version
		self.pretty_program: str = program.title()


class Finnish(Language):
	def descriptions(self) -> None:
		descriptions: str = """
		{0} {1}, tehokas alustustyökalu.
		Käyttö: {2} [valitsimet]...
		
		Komennot:
			create <nimi>...........Luo projekti nimellä <nimi>.
			
		Valitsimet:
			-h,  --help.............Tulosta tämä viesti.
			-V,  --version..........Tulosta Pinitin versio.
			-s,  --silent...........Hiljennä kaikki output, paitsi virheviestit.
			                        (HUOM: Tätä valitsinta ei ole vielä implementoitu.)
			-S,  --summary..........Näytä yhteenveto kaikista tiedostoista, kun
									uusi projekti on luotu. (HUOM: Tätä valitsinta ei
									ole vielä implementoitu.)
		""".format(self.pretty_program, self.version, self.program)
		print(textwrap.dedent(descriptions).strip())

	def usage(self) -> None:
		usage: str = "Käyttö: {0} [valitsimet]...".format(self.program)
		print(usage)
		sys.exit(1)


class English(Language):
	def descriptions(self) -> None:
		descriptions: str = """
		{0} {1}, efficient initialization tool.
		Usage: {2} [options]...
		
		Commands:
			create <name>			Create project <name>
		""".format(self.pretty_program, self.version, self.program)
		print(textwrap.dedent(descriptions))

	def usage(self) -> None:
		usage: str = "Usage: {0} [options]...".format(self.program)
		print(usage)
		sys.exit(1)
