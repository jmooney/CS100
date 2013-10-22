
'''

	Project:	CS100
	Title:		DiscretePrimitives

	Author:		John Mooney
	Date:		1/22/2013

	Description:
		Represents geometric shapes as a set of discrete localPoints
'''


# Imports
import math
from CS100.Tools.Constants import twoPi
from GeometricPrimitives import *
from CS100.Rendering.SceneObject import VertexDataSource
from pyglet.gl import (GL_TRIANGLE_FAN, GL_QUADS, GL_TRIANGLES, GL_LINES,  GL_POINTS)


#------------------------------------------------------#

class DiscretePrimitive(VertexDataSource):

	def __init__(self, *args):
		super().__init__(*args)
		
		self._localPoints = []
		self._buildPoints()
		self._buildVIS()
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def _buildPoints(self):
		raise NotImplementedError
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def getVertexData(self):
		return len(self._localPoints), self._drawStyle, self._vis, self._buildVLD()
	

	''''''''''''''''''''''''''''''''''''''''''
	
	def _buildVIS(self):
		if not self._vis:
			self._vis = list(range(len(self._localPoints)))
			
	def _buildVLD(self):
		data = []
		for p in self._localPoints:
			data.append(p.x)
			data.append(p.y)
		return [('v2f', data)]
	
		
#------------------------------------------------------#

class DiscreteEllipse(DiscretePrimitive, GeometricEllipse):
	
	def __init__(self, a, b, tc=26):
		super().__init__(a, b)
		self._triangleCount = tc

		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _buildPoints(self):
		self._drawStyle = GL_TRIANGLE_FAN
		self._localPoints.append(vec())
		
		a = self._a;	b = self._b
		
		tAngle 	= 0.0
		tStep	= twoPi/self._triangleCount
		tFull	= twoPi-tStep
		
		while tAngle < tFull:
			s = math.sin(tAngle)
			c = math.cos(tAngle)

			p = vec(a.x*c + b.x*s, a.y*c + b.y*s)
			self._localPoints.append(p)
			
			tAngle += tStep
		self._vis = list(range(len(self._localPoints))) + [1]
	
		
#------------------------------------------------------#

class DiscreteRect(DiscretePrimitive, GeometricRect):

	def _buildPoints(self):
		self._drawStyle = GL_QUADS

		w = self._width;	h=self._height
		self._localPoints[:] = [vec(-w/2, -h/2), vec(w/2, -h/2), vec(w/2, h/2), vec(-w/2, h/2)]
		
	def resize(self, w, h):
		self._width = w
		self._height = h
		
		self._buildPoints()
		self._sceneObject._updateData()
		

class DiscreteCircle(DiscreteEllipse):
	def __init__(self, rad, tc=26):
		super().__init__(rad, rad, tc)
		
class DiscreteTriangle(DiscretePrimitive, GeometricTriangle):
	def _buildPoints(self):
		self._drawStyle = GL_TRIANGLES
		self._localPoints[:] = [self._pVecs[0].copy(), self._pVecs[1].copy(), self._pVecs[2].copy()]
		
class DiscreteLine(DiscretePrimitive, GeometricLine):
	def _buildPoints(self):
		self._drawStyle = GL_LINES
		self._localPoints[:] = [vec(), self._endVec.copy()]

