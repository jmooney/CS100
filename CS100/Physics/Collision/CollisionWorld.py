
'''

	Project:	CS100
	Title:		CollisionWorld

	Author:	John Mooney
	Date:		1/23/2014

	Description:
		Manages all collision shapes/entities within the game world. Shapes are added here and checked against one another in an efficient manner.
		Queries are also submitted through the collision world
'''


# Imports


#------------------------------------------------------#
# Collision World
class CollisionWorld(object):

	def __init__(self):
		super().__init__()
		self._collisionLayers = {"Default":[]}
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
			
	def testCollisions(self):
		possibleCollisionsPairList = self._AABBCollisionDetection()
		collisionInfoList = self._GJKCollisionDetection(collisionPairList)
		return collisionInfoList

		
	def addShape(self, shape, layer="Default"):
		self._collisionLayers[layer].append(shape)
	def removeShape(self, shape, layer="Default"):
		self._collisionLayers[layer].remove(shape)
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _AABBCollisionDetection(self):
		possibleCollisionsPairList = []
		for layer, colliders in self._collisionLayers:
			
			for i in range(len(colliders)-1):
				for j in range(len(colliders[i+1:])):
					shape1 = colliders[i]
					shape2 = colliders[j]
					
					if self._testAABBCollision(shape1, shape2):
						possibleCollisionsPairList.append( (shape1, shape2) )
		return possibleCollisionsPairList
		
						
	def _GJKCollisionDetection(collisionPairList):
		return []
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _testAABBCollision(self, shape1, shape2):
		AABB1 = shape1.getAABB();	AABB2 = shape2.getAABB()
		
		centerDist = shape1.getPosition() - shape2.getPosition()
		maxWidth = AABB1.right + AABB2.right
		maxHeight = AABB1.top + AABB2.top
		
		if centerDist.x < maxWidth or centerDist.y < maxHeight:
			return True
		return False


