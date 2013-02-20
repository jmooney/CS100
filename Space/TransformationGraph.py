	
'''

	Project:	CS100
	Title:		TransformationGraph
	
	Author:		John Mooney
	Date:		10/22/2012

	Description:
		The Main-Game Transform Graph; Handles all transformations within CS100
		
'''

# Imports
from Object import Object

from Vector import vec
from Vector import ZeroVector
from tools import getDictValue

#--------------------------------------------------#

tg = None
class TransformationGraph(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._rootNode = _Transform()

		
	''''''''''''''''''''''''''''''''''''''''''
	
	#################################
	#		Accessor Methods		#
	#################################
		
	def getRoot(self):
		return self._rootNode

	def newTransform(self, **kwArgs):
		return self._rootNode.createChildNode(**kwArgs)
		
'''
	
	Class:		_Transform
	
	Description:
		A scene graph node; Contains Entity and Transform Data
'''

class _Transform(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		'''	Node and Update Values '''
		self._parent  	= None
		self._children 	= []
		
		'''	Transform Data '''
		self._translate 	= vec()
		self._gTrans		= vec()
		self._rotateRads 	= 0.0
		self._gRotRads      = 0.0
		self._scale			= 1.0
		self._gScale		= 1.0
	
		'''	Transformable Data	'''
		self._transformables  = []
	
	''''''''''''''''''''''''''''''''''''''''''
		
	def destroy(self):
		for transformable in self._transformables:
			transformable.removeTransform()
		for child in self._children:
			child.destroy()
			
		self._transformables = []
		self._children = []
		
		
	#############################
	#		Transforms			#
	#############################

	def translate(self, v):
		self._translate += v
		self._translateDependents()
	def translate2f(self, x, y):
		self._translate += vec(x, y)
		self._translateDependents()
	def setTranslation(self, v):
		self._translate = v
		self._translateDependents()
	def setTranslation2f(self, x, y):
		self._translate = vec(x,y)
		self._translateDependents()
		
	def rotate(self, rads):
		self._rotateRads+=rads
		self._rotateDependents()
	def setRotation(self, rads):
		self._rotateRads = rads
		self._rotateDependents()

	def scale(self, v):
		self._scale *= v
		self._scaleDependents()
	def setScale(self, v):
		self._scale = v
		self._scaleDependents()
		
	#########################
	#		Accessors		#
	#########################
	
	def getTranslation(self):
		return self._translate.copy()
	def getSceneTranslation(self):
		return self._gTrans.copy()
		
	def getRotation(self):
		return self._rotateRads
	def getSceneRotation(self):
		return self._gRotRads
		
	def getScale(self):
		return self._scale
	def getSceneScale(self):
		return self._gScale
		
		
	#################################
	#		Common Node Operations	#
	#################################
	
	def createChildNode(self, **kwArgs):
		node = _Transform()
		node.setParent(self)

		node.translate(getDictValue(kwArgs, vec(), ['t', 'translate']))
		node.rotate(getDictValue(kwArgs, 0.0, ['r', 'rotate']))
		node.scale(getDictValue(kwArgs, 1.0, ['s', 'scale']))
		
		return node
		
		
	'''	Transformable Operations	'''
	def addTransformable(self, d):
		self._transformables.append(d)
		
		d._onTranslation(self._gTrans)
		d._onRotation(self._gRotRads)
		d._onScale(self._gScale)

	def killTransformable(self, d):
		self._transformables.remove(d)
		if not self._transformables:
			self.destroy()
		
	def removeTransformable(self, d):
		self._transformables.remove(d)
		
	#################################
	#		Data Maintenance		#
	#################################
	
	def _translateDependents(self):
		pTrans = ZeroVector
		if(self._parent):
			pTrans = self._parent.getSceneTranslation()
			
		newTranslate = self._translate + pTrans
		oldTranslate = self._gTrans.copy()
		if(newTranslate != oldTranslate):	
			self._gTrans = newTranslate
			
			for transformable in self._transformables:
				transformable._onTranslation(newTranslate-oldTranslate)
			for child in self._children:
				child._translateDependents()
	def _rotateDependents(self):
		pRots = 0.0
		if(self._parent):
			pRots = self._parent.getSceneRotation()
			
		newRot = self._rotateRads + pRots
		oldRot = self._gRotRads
		if(newRot != oldRot):	
			self._gRotRads = newRot
			
			for transformable in self._transformables:
				transformable._onRotation(newRot-oldRot)
			for child in self._children:
				child._rotateDependents()
	def _scaleDependents(self):
		pScale = 1.0
		if(self._parent):
			pScale = self._parent.getSceneScale()
			
		newScale = self._scale * pScale
		oldScale = self._gScale
		if(newScale != oldScale):	
			self._gScale = newScale
			
			for transformable in self._transformables:
				transformable._onScale(newScale/oldScale)
			for child in self._children:
				child._scaleDependents()
				

	def _updateDependents(self):
		self._translateDependents()
		self._rotateDependents()
		self._scaleDependents()
		
		
	#################################
	#		Noding Operations		#
	#################################
	
	def setParent(self, p):
		self.removeParent()
		self._parent = p
		
		p._children.append(self)
		self._updateDependents()
		
	def removeParent(self):
		if(self._parent):
			self._parent._children.remove(self)
			self._updateDependents()
		self._parent = None
