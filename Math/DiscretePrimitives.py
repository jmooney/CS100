
'''

	Project:	CS100
	Title:		DiscretePrimitives

	Author:		John Mooney
	Date:		1/22/2013

	Description:
		Represents geometric shapes as a set of discrete points
'''


# Imports



#------------------------------------------------------#

class DiscretePrimitive(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._points = []
		self._buildPoints()
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _updatePoints(self):
		raise NotImplementedError

		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _onRotation(self, dif):
		c, s = super()._onRotation(dif)
		
		for p in self._points:
			p.x = p.x*c - p.y*s
			p.y = p.x*s + p.y*c
		
	def _onScale(self, dif):
		super()._onScale(dif)
		
		for p in self._points:
			p*=dif
		

#------------------------------------------------------#

class DiscreteEllipse(DiscretePrimitive, GeometryEllipse):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._triangleCount = getDictValue(kwArgs, 26, ['tc', 'triangleCount'])
		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _buildPoints(self):
		a = self._a;	b = self._b
		
		tAngle 	= 0.0
		tStep	= pi2/self._triangleCount
		tFull	= pi2-tStep
		
		while tAngle < tFull:
			s = math.sin(tAngle)
			c = math.cos(tAngle)

			p = vec(a.x*c + b.x*s, a.y*c + b.y*s)
			self._points.append(p)
			
			tAngle += tStep
			

#------------------------------------------------------#

class DiscreteRect(DiscretePrimitive, GeometricRect):
	def _buildPoints(self):
		self._points[:] = [vec(-w, -h), vec(w, -h), vec(w, h), vec(-w, h)]


class DiscreteCircle(DiscreteEllipse):
	def __init__(self, rad, **kwArgs):
		super().__init__(rad, rad, **kwArgs)
		
