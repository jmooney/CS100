
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
import pyglet.graphics as pGraphics

from CS100.Subsystems.Tree import TreeModifier
from CS100.Space.TransformationGraph import TransformNode
from CS100.Tools.Errors import InvalidStateError

from pyglet.gl import (	glPushMatrix, glPopMatrix,
	glTranslatef, glRotatef, glScalef	)
	
	
#------------------------------------------------------#
#	Define Freeze-Function Decorators (SceneGraph and ScenePrimitive)

def snFreezeable(fn):
	def wrapper(self, *args):
		if self._frozen:
			raise InvalidStateError("Calling Method: " + str(fn) + " From Frozen SceneNode")
		fn(self, *args)
	return wrapper

def spFreezeable(fn):
	def wrapper(self, *args):
		if self.getSceneNode() and self.getSceneNode()._frozen:
			raise InvalidStateError("Calling Method: " + str(fn) + " From Frozen ScenePrimitive")
		fn(self, *args)
	return wrapper
	
	
	
#------------------------------------------------------#
#	SceneGraph

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
#	SceneNode

class SceneNode(TransformNode):
	
	def __init__(self, baseNode, **kwArgs):
		super().__init__(baseNode, **kwArgs)
		self._modifierName = 'SceneNode'
		self._modifierCreator = SceneNode

		self._batch = None
		self._frozen = False
		self._visible = True
		self._scenePrimitives = []
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''

	@snFreezeable
	def _draw(self):
		glPushMatrix()
		
		glTranslatef(self._translate.x, self._translate.y, 0.0)
		glRotatef(math.degrees(self._rotateRads), 0, 0, 1)
		glScalef(self._scale.x, self._scale.y, 1)
		
		if self._batch:
			self._batch.draw()
		
		for sceneNode in self.getChildren():
			if sceneNode._visible and not sceneNode._frozen:
				sceneNode._draw()

		glPopMatrix()


	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def freeze(self):
		self._frozen = True
	def unfreeze(self):
		self._frozen = False
	
	'''	Consider 'freeze decorators' '''
	@snFreezeable
	def batchSubTree(self):
		for child in self.getChildren():
			for primitive in child._getSubTreePrimitives():
				primitive.setBatch(self._batch)
			child.freeze()
	
	def _getSubTreePrimitives(self):
		prims = self._scenePrimitives
		for child in self.getChildren():
			prims.extend(child._getSubTreePrimitives())
		return prims
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	@snFreezeable
	def addScenePrimitive(self, primitive):
		if not self._batch:
			self._batch = pGraphics.Batch()
		self._scenePrimitives.append(primitive)		
		primitive.setBatch(self._batch)
	
	@snFreezeable
	def removeScenePrimitive(self, primitive):
		self._scenePrimitives.remove(primitive)
		primitive.setBatch(None)

