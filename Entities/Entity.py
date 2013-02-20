
'''

	Project:	CS100
	Title:		Entity

	Author:		John Mooney
	Date:		10/22/2012

	Description:
		A Transformable Entity within the Game - has a position in the world
'''

# Imports
from Transformable import Transformable


#--------------------------------------------------#

class Entity(Transformable):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._transform = TransformationGraph.tg.newTransform()
		self._transform.addTransformable(self)
		
	''''''''''''''''''''''''''''''''''''''''''

