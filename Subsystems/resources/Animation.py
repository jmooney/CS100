
'''

	Project:	CS100
	Title:		Animation

	Author:		John Mooney
	Date:		4/7/2013

	Description:
		An animation:
			- A series of image regions and timing information
'''


# Imports



#-----------------------------------------------#

class Animation(Resource):

	def __initP__(self, **kwArgs):
		super().__initP__(**kwArgs)
		
		self._identifier = ""
		
		self._frames = []
		self._delays = []
		self._repeatMode = None
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def load(self, filename):
		pass
		
		