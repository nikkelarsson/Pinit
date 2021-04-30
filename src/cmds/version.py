'''
file : version.py  
desc : Management of printing Pinit's version.
'''

def get(pname, version):
	'''Print Pinit's current version.'''
	
	print('{} {}'.format( pname[0].upper() + pname[1:].lower(), version ))