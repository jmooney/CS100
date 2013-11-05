
'''

	Project:	CS100
	Title:		CollisionWorld

	Author:	John Mooney
	Date:		11/04/2013

	Description:
		Manages all collision shapes/entities within the game world. Shapes are added here and checked against one another in an efficient manner.
		Queries are also submitted through the collision world
'''


# Imports



class CollisionWorld(object):

	def __init__(self):
		super().__init__()

		self._colShapes = []

		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def checkCollisions(self):
		
		# Broad-Phase Detection : Determines 'rough' collisions between objects
		collisionPairsDict = self._testAABBs()
		
		#	Narrow-Phase Detection : Determine specific collisions and collision information
		self._checkDetailCollisions(collisionPairsDict)