
'''
File : help.py  
Desc : Command and usage descriptions.
'''

#
# The output should look something like:
#
# <program> X.X, short description here.
# Usage: <program> [options]...
#
# <category name>:
#     -f,  --flags-here               Description here.
#

import textwrap


class Language:
	'''Base class for descriptions.'''

	def __init__(self, program: str, version: str):
		self.program: str = program
		self.version: str = version
		self.pretty_program: str = program[0].upper() + program[1:].lower()


class Finnish(Language):
	def descriptions(self) -> None:
		descriptions = '''
		{0} {1}, tehokas alustustyökalu.
		Käyttö: {2} [valitsimet]...
		
		Komennot:
			create <nimi>			Luo projekti <nimi>
			
		Valitsimet:
			-h,  --help				Tulosta tämä viesti
			-V,  --version			Tulosta Pinitin versio'''.format(self.pretty_program, self.version, self.program)

		print( textwrap.dedent(descriptions).strip() )

	def usage(self) -> None:
		usage = 'Käyttö: {0} [valitsimet]...'.format(self.program)
		print(usage)


class English(Language):
	def descriptions(self) -> None:
		descriptions = '''
		{0} {1}, efficient initialization tool.
		Usage: {2} [options]...
		
		Commands:
			create <name>			Create project <name>'''.format(self.pretty_program, self.version, self.program)

		print( textwrap.dedent(descriptions) )

	def usage(self) -> None:
		usage = 'Usage: {0} [options]...'.format(self.program)
		print(usage)
