
'''

	Project:	CS100
	Title:		SceneObject

	Author:	John Mooney
	Date:		10/12/2013

	Description:
		A drawable object within a scene
'''

# Imports
from CS100.Space.Transformable import Transformable

#------------------------------------------------------#

class SceneObject(Transformable):
	
	def __init__(self, sceneNode=None):
		super().__init__()

		self._visible = True
		self.setSceneNode(sceneNode)
			

	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setSceneNode(self, sceneNode):
		retVal = super().setTransform(sceneNode)
		self._sceneNode = self._transform
		return retVal
	def removeSceneNode(self):
		super().removeTransform()
		self._sceneNode = self._transform

		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getSceneNode(self):
		return self._sceneNode
	
	def isVisible(self):
		return self._visible
	def setVisible(self, v):
		self._visible = v
		