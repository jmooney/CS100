
'''

	Project:	CS100
	Title:		DiscretePrimitives

	Author:		John Mooney
	Date:		1/22/2013

	Description:
		Represents geometric shapes as a set of discrete points
'''


# Imports



#------------------------------------------------------#

class DiscretePrimitive(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._points = []

		