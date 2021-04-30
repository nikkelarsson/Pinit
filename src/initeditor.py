import os
from settings import editor
from errors import EditorNotFoundError

def InitEditor(editor=editor):
	'''Open desired text editor.'''
	try:
		os.system('{}'.format(editor))
	except:
		EditorNotFoundError()
