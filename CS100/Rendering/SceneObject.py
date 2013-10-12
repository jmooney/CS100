
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
	
	def __init__(self, sceneNode=None, dataSrc=None, **kwArgs):
		super().__init__(sceneNode.asType('TransformNode'))
		self._sceneNode = sceneNode
		self._visible = True


	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def isVisible(self):
		return self._visible
	def getSceneNode(self):
		return self._sceneNode