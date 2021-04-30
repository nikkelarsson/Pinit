import sys
from settings import language, editor

class EditorNotFoundError:

	# Using english message as a default.
	defaultMessage = 'Editor not found'

	def __init__(self):

		if langugae == 'us':
			message = 'Error: {}: {}'.format(editor, defaultMessage)
		elif language == 'fi':
			message = 'Virhe: {}: Editoria ei löytynyt'.format(editor)
		else:
			message = 'Error: {}: {}'.format(editor, defaultMessage)

		print('{}'.format(message))
		sys.exit(1)
