
'''

	Project:	CS100
	Title:		GeometricPrimitives

	Author:		John Mooney
	Date:		2/26/2013

	Description:
		Geometric primitive representations and data
'''


# Imports
from Vector import vec
from tools import getDictValue


#------------------------------------------------------#

class GeometricEllipse(object):

	def __init__(self, a, b):
		super().__init__()
		
		self._a = vec(a, 0)
		self._b = vec(0, b)
		
		

#------------------------------------------------------#

class GeometricRect(object):
	
	def __init__(self, w, h):
		super().__init__()
		
		self._width 	= w
		self._height 	= h
		self._diagonal 	= vec(w/2, h/2)
		
		

#------------------------------------------------------#

class GeometricCircle(object):

	def __init__(self, radius):
		super().__init__()
		self._radius = radius
		

#------------------------------------------------------#

class GeometricTriangle(object):

	def __init__(self, points):
		super().__init__()
		self._pVecs	= points
		

#------------------------------------------------------#

class GeometricLine(object):

	def __init__(self, eVec):
		super().__init__()
		self._endVec = eVec
