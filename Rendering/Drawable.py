
'''

	Project:	CS100
	Title:		Drawable

	Author:		John Mooney
	Date:		11/25/2012

	Description:
		A Drawable entity within the Game - must define a 'draw' method
'''

# Imports
from Object import Object

#--------------------------------------------------#

class Drawable(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._visible = True
		
	'''	Drawing Methods	'''
	
	def draw(self):	
		raise NotImplementedError("Class " + type(self).__name__ + " inherits Drawable, but does not implement draw()")
		
		
	'''	Getters and Setters '''
	def isVisible(self):
		return self._visible
	def setVisible(self, b):
		self._visible = b
		