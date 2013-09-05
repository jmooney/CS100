	
'''

	Project:	CS100
	Title:		TransformationGraph
	
	Author:		John Mooney
	Date:		10/22/2012

	Description:
		The Main-Game Transform Graph; Handles all transformations within CS100
		using a tree structure.
			
	Refactoring:
		- Implement a single tree hierarchy, where this is a component on top of the underlying system 
		
'''

# Imports
from Vector import vec
from Vector import ZeroVector
from tools import getDictValue
from Tree import (TreeModifier, NodeModifier)


#--------------------------------------------------#

class TransformationGraph(TreeModifier):

	_nodeModifierName = 'TransformNode'
	_nodeModifierCreator = TransformNode
	
		
	''''''''''''''''''''''''''''''''''''''''''
	
	def newNode(self, **kwArgs):
		return self.getRoot().createChild(**kwArgs)
	def newTransform(self, **kwArgs):
		return self.newNode(**kwArgs)
	
	
#--------------------------------------------------#

class TransformNode(TreeNodeModifier):

	_modifierName = 'TransformNode'
	_modifierCreator = TransformNode

	def __init__(self, baseNode, **kwArgs):
		super().__init__(baseNode)
		
		'''	Transform Data '''
		self._translate 	= getDictValue(kwArgs, vec(), ['t', 'translate'])
		self._rotateRads 	= getDictValue(kwArgs, 0.0, ['r', 'rotate'])
		self._scale			= getDictValue(kwArgs, vec(1,1), ['s', 'scale'])
		self._gTrans		= self._translate.copy()
		self._gRotRads      = self._rotateRads
		self._gScale		= self._scale.copy()
	
		'''	Transformable Data	'''
		self._transformables  = []

	
	''''''''''''''''''''''''''''''''''''''''''

	def translate(self, v):
		self._translate += v
		self._translateDependents()
	def translate2f(self, x, y):
		self._translate.x += x
		self._translate.y += y
		self._translateDependents()
	def setTranslation(self, v):
		self._translate = v
		self._translateDependents()
	def setTranslation2f(self, x, y):
		self._translate.x = x
		self._translate.y = y
		self._translateDependents()
		
	def rotate(self, rads):
		self._rotateRads+=rads
		self._rotateDependents()
	def setRotation(self, rads):
		self._rotateRads = rads
		self._rotateDependents()

	def scale(self, v):
		self._scale.x *= v.x
		self._scale.y *= v.y
		self._scaleDependents()
	def scale2f(self, x, y):
		self._scale.x *= x
		self._scale.y *= y
		self._scaleDependents()
	def setScale(self, v):
		self._scale = v
		self._scaleDependents()
	def setScale2f(self, x, y):
		self._scale.x = x
		self._scale.y = y
		self._scaleDependents()
	

	''''''''''''''''''''''''''''''''''''''''''
	
	def getTranslation(self):
		return self._gTrans.copy()
	def getLocalTranslation(self):
		return self._translate.copy()
		
	def getRotation(self):
		return self._gRotRads
	def getLocalRotation(self):
		return self._rotateRads
		
	def getScale(self):
		return self._gScale.copy()
	def getLocalScale(self):
		return self._scale.copy()
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _addTransformable(self, d):
		self._transformables.append(d)
		
		d._onTranslation(self._gTrans)
		d._onRotation(self._gRotRads)
		d._onScale(self._gScale)

	def _removeTransformable(self, d):
		self._transformables.remove(d)
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _translateDependents(self):
		parent = self.getParent()
		
		pTrans = vec()
		if parent:
			pTrans = parent.getTranslation()
			
		newTranslate = self._translate + pTrans
		oldTranslate = self._gTrans.copy()
		if(newTranslate != oldTranslate):	
			self._gTrans = newTranslate
			
			for transformable in self._transformables:
				transformable._onTranslation(newTranslate-oldTranslate)
			for child in self.getChildren():
				child._translateDependents()
	def _rotateDependents(self):
		parent = self.getParent()
		
		pRots = 0.0
		if parent:
			pRots = parent.getRotation()
			
		newRot = self._rotateRads + pRots
		oldRot = self._gRotRads
		if(newRot != oldRot):	
			self._gRotRads = newRot
			
			for transformable in self._transformables:
				transformable._onRotation(newRot-oldRot)
			for child in self.getChildren():
				child._rotateDependents()
	def _scaleDependents(self):
		parent = self.getParent()
		
		pScale = vec(1.0, 1.0)
		if parent:
			pScale = parent.getScale()
			
		newScale = self._scale * pScale
		oldScale = self._gScale
		
		if(newScale != oldScale):
			self._gScale = newScale
			
			for transformable in self._transformables:
				transformable._onScale(newScale/oldScale)
			for child in self.getChildren():
				child._scaleDependents()
				

	def _updateDependents(self):
		self._translateDependents()
		self._rotateDependents()
		self._scaleDependents()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''
		
	def setParent(self, p):
		super().setParent(p)
		self._updateDependents()
		
	def removeParent(self):
		super().setParent(None)
		self._updateDependents()
		
