
'''

	Project:	CS100
	Title:		DiscretePrimitives

	Author:		John Mooney
	Date:		1/22/2013

	Description:
		Represents geometric shapes as a set of discrete points
'''


# Imports
import math

from pyglet.gl import (GL_TRIANGLE_FAN, GL_QUADS, GL_TRIANGLES, GL_LINES,  GL_POINTS)
from SceneObject import VertexDataSource
from GeometricPrimitives import *

from tools import twoPi

#------------------------------------------------------#

class DiscretePrimitive(VertexDataSource):

	def __initP__(self, **kwArgs):
		super().__initP__(**kwArgs)
		self._points 	= []
		
		self._vis = []
		self._drawStyle = None
		
		
	def __initC__(self, **kwArgs):
		self._buildPoints()
		self._buildVIS()
		super().__initC__(**kwArgs)
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def _buildPoints(self):
		raise NotImplementedError
		
	
	''''''''''''''''''''''''''''''''''''''''''
	
	def getVertexData(self):
		return len(self._points), self._drawStyle, self._vis, self._buildVLD()
	

	''''''''''''''''''''''''''''''''''''''''''
	
	def _buildVIS(self):
		if not self._vis:
			self._vis = list(range(len(self._points)))
			
	def _buildVLD(self):
		data = []
		for p in self._points:
			data.append(p.x)
			data.append(p.y)
		return [('v2f', data)]
	
		
#------------------------------------------------------#

class DiscreteEllipse(DiscretePrimitive, GeometricEllipse):
	
	def __initP__(self, **kwArgs):
		super().__initP__(**kwArgs)
		self._triangleCount = getDictValue(kwArgs, 26, ['tc', 'triangleCount'])

		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _buildPoints(self):
		self._drawStyle = GL_TRIANGLE_FAN
		self._points.append(vec())
		
		a = self._a;	b = self._b
		
		tAngle 	= 0.0
		tStep	= twoPi/self._triangleCount
		tFull	= twoPi-tStep
		
		while tAngle < tFull:
			s = math.sin(tAngle)
			c = math.cos(tAngle)

			p = vec(a.x*c + b.x*s, a.y*c + b.y*s)
			self._points.append(p)
			
			tAngle += tStep
		self._vis = list(range(len(self._points))) + [1]
	
		
#------------------------------------------------------#

class DiscreteRect(DiscretePrimitive, GeometricRect):
	def _buildPoints(self):
		self._drawStyle = GL_QUADS

		w = self._width;	h=self._height
		self._points[:] = [vec(-w, -h), vec(w, -h), vec(w, h), vec(-w, h)]
		

class DiscreteCircle(DiscreteEllipse):
	def __init__(self, rad, **kwArgs):
		super().__init__(rad, rad, **kwArgs)
		
class DiscreteTriangle(DiscretePrimitive, GeometricTriangle):
	def _buildPoints(self):
		self._drawStyle = GL_TRIANGLES
		self._points[:] = [self._pVecs[0].copy(), self._pVecs[1].copy(), self._pVecs[2].copy()]
		
class DiscreteLine(DiscretePrimitive, GeometricLine):
	def _buildPoints(self):
		self._drawStyle = GL_LINES
		self._points[:] = [vec(), self._endVec.copy()]
		
