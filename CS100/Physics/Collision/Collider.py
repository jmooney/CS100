
'''

	Project:	CS100
	Title:		Collider

	Author:	John Mooney
	Date:		1/23/2014

	Description:
		A collideable entity within the game world
'''


# Imports


#------------------------------------------------------#
#	Collider
class Collider(Transformable, EventListener):
	
	def __init__(self, transform=None, collisionShape = None):
		super().__init__(transform)
		
		self._collisionShape = collisionShape
		self._isCollideable = True
		self._collisionLayer = "Default"
		
		self._eventHandlers = {"ON_COLLISION":self.onCollision, "OFF_COLLISION":self.offCollision, "DURING_COLLISON":self.duringCollision}
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def onCollision(self, collisionInfo):
		pass
	def offCollision(self, collisionInfo):
		pass
	def duringCollision(self, collisionInfo):
		pass
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''