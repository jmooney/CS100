
'''

	Project:	CS100
	Title:		GeometryPrimitives

	Author:		John Mooney
	Date:		1/24/2013

	Description:
		Manages geometric primitives within a transformation space
'''

# Imports
import math

from Transformable import Transformable

from Vector import vec
from Vector import XAxisVector
from tools import getDictValue


#-----------------------------------------------#

class GeometricEllipse(Transformable):

	def __init__(self, a, b):
		self._a = vec(a, 0)
		self._b = vec(0, b)

		super().__init__(**kwArgs)		

		
	''''''''''''''''''''''''''''''''''''''
	
	#################################
	#		Data Maintenance		#
	#################################
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
	
	def _onRotation(self, dif):
		super()._onRotation(dif)
		
		a = self._a;		b = self._b
		c = math.cos(dif);	s = math.sin(dif)
		
		a.x = a.x*c - a.y*s
		a.y = a.x*s + a.y*c
		
		b.x = b.x*c - b.y*s
		b.y = b.x*s + b.y*c
		
		return c, s
		
	def _onScale(self, dif):
		super()._onScale(dif)
		self._a *= dif;	self._b *= dif;


#--------------------------------------------------------#
	
class GeometricRect(Transformable):

	def __init__(self, w, h, **kwArgs):
		self._width 	= w = getDictValue(kwArgs, 1.0, ['w', 'width'])
		self._height 	= h = getDictValue(kwArgs, 1.0, ['h', 'height'])
		self._diagonal 	= vec(w/2, h/2)
		
		super().__init__(**kwArgs)


	''''''''''''''''''''''''''''''''''''''
	
	#################################
	#		Data Maintenance		#
	#################################
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
	
	def _onRotation(self, dif):
		super()._onRotation(dif)
		
		d = self._diagonal
		c = math.cos(dif);	s = math.sin(dif)
		
		d.x = d.x*c - d.y*s
		d.y = d.x*s + d.y*c
		
	def _onScale(self, dif):
		super()._onScale(dif)
		self._diagonal 	*= dif


#------------------------------------------------#

class GeometricCircle(Transformable):
	
	def __init__(self, radius, **kwArgs):
		self._radius = radius
		super().__init__(**kwArgs)
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def _onScale(self, dif):
		super()._onScale(dif)
		self._radius *= dif


#------------------------------------------------#

class GeometricTriangle(Transformable):

	def __init__(self, **kwArgs):
		self._pointVecs = getDictValue(kwArgs, None, ['ps', 'points'], True)
		super().__init__(**kwArgs)
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def _onRotation(self, dif):
		super._onRotation(dif)
		c = math.cos(dif);	s = math.sin(dif)
		
		for p in self._pointVecs:
			p.x = p.x*c - p.x*s
			p.y = p.x*s + p.y*c
		
		
#------------------------------------------------#

class GeometricLine(Transformable):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)

		length 	= getDictValue(kwArgs, None, ['l', 'length'])
		direc  	= getDictValue(kwArgs, None, ['d', 'direc', 'direction'])

		if length and direc:
			self._end = self._worldPos + direc*length
		else:
			self._end = getDictValue(kwArgs, vec(), ['e', 'end'], True)

		
	def __initData__(self, **kwArgs):
		kwArgs['localRot'] = self._end.getAngleTo(XAxisVector)
		super().__initData__(**kwArgs)
		

	''''''''''''''''''''''''''''''''''''''''''
		
	def _onRotation(self, dif):
		super()._onRotation(dif)		
		
		e = self._end
		c = math.cos(dif);	s = math.sin(dif)
		
		e.x = e.x*c - e.y*s
		e.y = e.x*s + e.y*c
		
	def _onScale(self, dif):
		super()._onScale(dif)
		self._end*=dif

#------------------------------------------------#
