
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

import Color
import DebugDrawingManager

from Transformable import Transformable

from Vector import vec
from Vector import XAxisVector
from tools import getDictValue


#------------------------------------------------------#

class GeometryPrimitive(Transformable):
	pass


#--------------------------------------------------------#
	
class GeometryRect(GeometryPrimitive):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._width = w = getDictValue(kwArgs, 1.0, ['w', 'width'])
		self._height = h = getDictValue(kwArgs, 1.0, ['h', 'height'])
		
		#	A diagonal crossing from the center to the top-right
		self._diagonal 		= vec(w/2, h/2)
		self._diagonalRot 	= self._diagonal.getAngleTo(XAxisVector)
		self._dLength 		= self._diagonal.length()
		
		
	''''''''''''''''''''''''''''''''''''''
	
	#################################
	#		Data Maintenance		#
	#################################
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
	def _onRotation(self, dif):
		super()._onRotation(dif)
		dr = self._worldRot+self._diagonalRot

		self._diagonal.x = math.cos(dr)*self._dLength
		self._diagonal.y = math.sin(dr)*self._dLength
	def _onScale(self, dif):
		super()._onScale(dif)
		self._diagonal 	*= dif
		self._dLength	*= dif

#-----------------------------------------------#

class GeometryEllipse(GeometryPrimitive):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		a = getDictValue(kwArgs, 1.0, ['a', 'x', 'major'])
		b = getDictValue(kwArgs, 1.0, ['b', 'y', 'minor'])
	
		self._a = vec(a, 0);	self._aLength = a
		self._b = vec(0, b);	self._bLength = b
		
		
	''''''''''''''''''''''''''''''''''''''
	
	#################################
	#		Data Maintenance		#
	#################################
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
	def _onRotation(self, dif):
		super()._onRotation(dif)
		wr = self._worldRot
		
		al = self._aLength
		self._a.x = math.cos(wr)*al
		self._a.y = math.sin(wr)*al
		
		bl = self._bLength
		bRot = wr+math.pi/2
		self._b.x = math.cos(bRot)*bl
		self._b.y = math.sin(bRot)*bl
	def _onScale(self, dif):
		super()._onScale(dif)
		self._a *= dif;	self._aLength*=dif
		self._b *= dif;	self._bLength*=dif
		

		
#------------------------------------------------#

class GeometryLine(GeometryPrimitive):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)

		length 	= getDictValue(kwArgs, None, ['l', 'length'])
		direc  	= getDictValue(kwArgs, None, ['d', 'direc', 'direction'])

		if length and direc:
			self._length = length
			self._end = self._worldPos + direc*length
		else:
			self._end = getDictValue(kwArgs, vec(), ['e', 'end'], True)
			self._length = (self._end-self._worldPos).length()
		
		
	def __initData__(self, **kwArgs):
		kwArgs['localRot'] = self._end.getAngleTo(XAxisVector)
		super().__initData__(**kwArgs)
		

	''''''''''''''''''''''''''''''''''''''''''
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
		self._end += dif
	def _onRotation(self, dif):
		super()._onRotation(dif)
		wr = self._worldRot
		
		self._end.x = math.cos(wr)*self._length + self._worldPos.x
		self._end.y = math.sin(wr)*self._length + self._worldPos.y
	def _onScale(self, dif):
		super()._onScale(dif)
		self._length	*= dif
		self._end 		= (self._end - self._worldPos)*dif + self._worldPos

#------------------------------------------------#
