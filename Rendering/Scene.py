
'''

	Project:	CS100
	Title:		Scene

	Author:		John Mooney
	Date:		11/25/2012

	Description:
		Handles drawing of a single scene with CS100
'''

# Imports
from Object import Object


#---------------------------------------#

class Scene(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._entities = []

	'''		Draw the Scene		'''
	def draw(self):
		for e in self._entities:
			if(e.isVisible()):
				e.draw()

	
	#############################
	#		Entity Handles		#
	#############################
	
	def addEntity(self, e):
		self._entities.append(e)
	def removeEntity(self, e):
		self._entities.remove(e)
		
