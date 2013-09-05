
'''

	Project:	CS100
	Title:		SceneGraph

	Author:		John Mooney
	Date:		2/27/2013, 9/5/2013

	Description:
		Handles all drawing of scene nodes ad objects
		All entities must be organized within a transformation graph
'''


# Imports
import math
from Tree import import TreeModifier
from TransformationGraph import TransformNode
from pyglet.gl import (	glPushMatrix, glPopMatrix,
	glTranslatef, glRotatef, glScalef	)


#------------------------------------------------------#

class SceneGraph(TreeModifier):

	_modifierName = 'SceneNode'
	_modifierCreator = SceneNode
	
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		root = self.getRoot()
		if root._visible:
			root._draw()
	
	
	
#------------------------------------------------------#

class SceneNode(TransformNode):
	
	_modifierName = 'SceneNode'
	_modifierCreator = SceneNode
	
	def __init__(self, baseNode, **kwArgs):
		super().__init__(baseNode, **kwArgs)
		
		self._visible = True
		self._sceneObjects = []
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def _draw(self):
		glPushMatrix()
		
		glTranslatef(self._translate.x, self._translate.y, 0.0)
		glRotatef(math.degrees(self._rotateRads), 0, 0, 1)
		glScalef(self._scale.x, self._scale.y, 1)
		
		for sceneObject in self._sceneObjects:
			if sceneObject._visible
				sceneObject.draw()
		
		for child in self._node._children:
			try:
				sceneNode = child._getModifier(self._modifierName)
				if sceneNode._visible:
					sceneNode._draw()
			except KeyError:
				pass
			
		glPopMatrix()

