
'''

	Project:	CS100
	Title:		Transformable

	Author:		John Mooney
	Date:		10/22/2012

	Description:
		A Transformable entity within the Game - has a position, rotation, scale in the world
		Manages data consistency using various function interfaces on________()
'''

# Imports
from CS100.Tools import getDictValue
from CS100.Math.Vector import vec


#--------------------------------------------------#

class Transformable(object):
	
	def __init__(self, transform=None):
		super().__init__()
		
		self._lastTransformation = [False, [0,0,0]]
		
		self.isDrawn = True
		self._transform = None
		self.setTransform(transform)

		

	''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if self._lastTransformation[0]:
			self._onTransformation(self._lastTransformation[1])
			
			
	''''''''''''''''''''''''''''''''''''''''''

	def getPosition(self):
		return self._transform.getTranslation()
	def getRotation(self):
		return self._transform.getRotation()
	def getScale(self):
		return self._transform.getScale()
	
	
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

		
	''''''''''''''''''''''''''''''''''''''''''

	def getTransform(self):
		return self._transform

	def setTransform(self, node):
		if node and not self._transform:
			self._transform = node
			node._addTransformable(self)
			self._onTransformation(self._lastTransformation[1])
			return True
		return False
		
	def removeTransform(self):
		t = self._transform
		
		self._transform._removeTransformable(self)
		self._transform = None
		
		return t
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def _onTransformation(self, transformations):
		self._lastTransformation[0] = False;	self._lastTransformation[1] = [0,0,0]
		
		
	def _onTranslation(self, dif):
		self._lastTransformation[0] = True;	self._lastTransformation[1][0] = dif
	def _onRotation(self, dif):
		self._lastTransformation[0] = True;	self._lastTransformation[1][1] = dif
	def _onScale(self, dif):
		self._lastTransformation[0] = True;	self._lastTransformation[1][2] = dif
