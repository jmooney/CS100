
'''

	Project:	CS100
	Title:		Transformable

	Author:		John Mooney
	Date:		10/22/2012

	Description:
		A Transformable entity within the Game - has a position, rotation, scale in the world
'''

# Imports
from Object import Object

from Vector import vec
from tools import getDictValue

class Transformable(Object):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._worldPos 		= vec()
		self._worldRot 		= 0.0
		self._worldScale 	= vec(1, 1)
		
		self._isTransformed = False
		self._transform 	= None
		
		
	# 			Modifies child-personal variables				#
	def __initData__(self, **kwArgs):
		super().__initData__(**kwArgs)
		
		self._localPos		= getDictValue(kwArgs, vec(), ['lp', 'localPos'])
		self._localRot		= getDictValue(kwArgs, 0.0, ['lr', 'localRot'])
		self._localScale	= getDictValue(kwArgs, vec(1, 1), ['ls', 'localScale'])

		t = getDictValue(kwArgs, None, ['t', 'transform'])
		if(t):
			self.setTransform(t)			

	''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if(self._isTransformed):
			self._onTransformation()
			
	#################################
	#	Transform Setters/Getters	#
	#################################
	

	def getPosition(self):
		return self._worldPos
	def getRotation(self):
		return self._worldRot
	def getScale(self):
		return self._worldScale
	
	
	'''	Setters '''
	
	def translate(self, v):
		self._transform.translate(v)
	def translate2f(self, x, y):
		self._transform.translate2f(x,y)
	def setTranslation(self, v):
		self._transform.setTranslation(v)
	def setTranslation2f(self, x, y):
		self._transform.setTranslation2f(x,y)
		
	def rotate(self, r):
		self._transform.rotate(r)
	def setRotation(self, r):
		self._transform.setRotation(r)
		
	def scale(self, s):
		self._transform.scale(s)
	def scale2f(self, x, y):
		self._transform.scale2f(x, y)
	def setScale(self, s):
		self._transform.setScale(s)
	def setScale2f(self, x, y):
		self._transform.setScale2f(x, y)

		
	#############################
	#		Getters/Setters		#
	#############################

	def getTransform(self):
		return self._transform
	def setTransform(self, node):
		self._transform = node
		node._addTransformable(self)
	def removeTransform(self):
		t = self._transform
		
		self._transform._removeTransformable(self)
		self._transform = None
		
		self._worldPos 		= vec()
		self._worldRot		= 0.0
		self._worldScale	= vec(1,1)
		
		return t
		
		
	#################################
	#		Data Maintenance		#
	#################################

	def _onTranslation(self, dif):
		self._worldPos  	= self._localPos + self._transform.getTranslation()
		self._isTransformed = True
	def _onRotation(self, dif):
		self._worldRot  	= self._localRot + self._transform.getRotation()
		self._isTransformed = True
	def _onScale(self, dif):
		self._worldScale 	= self._localScale * self._transform.getScale()
		self._isTransformed = True
		
