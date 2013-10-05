
'''

	Project:	CS100
	Title:		Resource

	Author:		John Mooney
	Date:		4/20/2013

	Description:
		Provides an interface for loading resources within the game. 
		Resources include external data such as animations, images, etc..
'''

# Imports


#-------------------------------------------------#

class Resource(object):
	
	def __init__(self, filename):
		super().__init__()
		
		self._filename = filename
		
		self._preLoad()
		self._load(self._filename)
		
	
	def _preLoad(self):
		raise NotImplementedError
	def _load(self):
		raise NotImplementedError
