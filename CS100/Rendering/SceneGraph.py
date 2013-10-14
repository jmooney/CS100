
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
from CS100.Subsystems.Tree import TreeModifier
from CS100.Space.TransformationGraph import TransformNode

from pyglet.gl import (	glPushMatrix, glPopMatrix,
	glTranslatef, glRotatef, glScalef	)

	
#------------------------------------------------------#

class SceneGraph(TreeModifier):

	activeGraph = None
	
	def __init__(self, baseTree):
		self._nodeModifierName = 'SceneNode'
		self._nodeModifierCreator = SceneNode
		super().__init__(baseTree)
	
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		root = self.getRoot()
		if root._visible:
			root._draw()
	
	
	
#------------------------------------------------------#

class SceneNode(TransformNode):
	
	def __init__(self, baseNode, **kwArgs):
		super().__init__(baseNode, **kwArgs)
		self._modifierName = 'SceneNode'
		self._modifierCreator = SceneNode

		self._visible = True
		self._scenePrimitives = []
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def _draw(self):
		glPushMatrix()
		
		glTranslatef(self._translate.x, self._translate.y, 0.0)
		glRotatef(math.degrees(self._rotateRads), 0, 0, 1)
		glScalef(self._scale.x, self._scale.y, 1)
		
		for scenePrimitive in self._scenePrimitives:
			if scenePrimitive.isVisible():
				scenePrimitive.draw()
		
		for child in self._node._children:
			try:
				sceneNode = child._getModifier(self._modifierName)
				if sceneNode._visible:
					sceneNode._draw()
			except KeyError:
				pass
			
		glPopMatrix()


	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def addScenePrimitive(self, obj):
		self._scenePrimitives.append(obj)
	def removeScenePrimitive(self, obj):
		self._scenePrimitives.remove(obj)
		
		