
'''

	Project:	CS100
	Title:		ScenePrimitives

	Author:		John Mooney
	Date:		1/22/2013

	Description:
		Manages drawing of primitive objects called through the debug facility
'''

# Imports
from Object import Object

import pyglet
import math
import Color

from tools import getDictValue
from Vector import vec
from Vector import XAxisVector

from GeometryPrimitives import *


#------------------------------------------------------#

class _ScenePrimitive(GeometryPrimitive):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._color = getDictValue(kwArgs, Color.White, ['c', 'color'])

		self._numPoints		= 0
		self._points 		= []
		self._pointIndices 	= []
		self._colors 		= []
		self._drawStyle 	= None
		
		self._vertexList 	= None
		
		
	def __initData__(self, **kwArgs):
		super().__initData__(**kwArgs)
		self._colors		= self._color*self._numPoints

		if(self._transform):
			self.updatePoints()
			
			batch = getDictValue(kwArgs, None, ['batch'])
			if(batch):
				self.addToBatch(batch)
			else:
				self.buildVertexList()
		

	''''''''''''''''''''''''''''''
	
	def draw(self):
		self._vertexList.draw(self._drawStyle)
		
	''''''''''''''''''''''''''''''''
	
	def addToBatch(self, batch):
		if(self._vertexList):
			raise ValueError("Must free Vertex_List from Memory")
		self._vertexList = batch.add_indexed(self._numPoints, self._drawStyle, None, self._pointIndices, ('v2f', self._points), ('c3B', self._colors))
	
	def buildVertexList(self):
		if(self._vertexList):
			raise ValueError("Must free Vertex_List from Memory")
		self._vertexList = pyglet.graphics.vertex_list_indexed(self._numPoints, self._pointIndices, ('v2f', self._points), ('c3B', self._colors))
		
	def deleteVertexList(self):
		self._vertexList.delete()
		self._vertexList = None
			
	''''''''''''''''''''''''''''''

	def updatePoints(self):
		raise NotImplementedError
		
	''''''''''''''''''''''''''''''
	
	def _onTransformation(self):
		super()._onTransformation()
		self.updatePoints()


#--------------------------------------------#

class SceneRect(GeometryRect, _ScenePrimitive):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)		
	
		self._numPoints		= 4
		self._pointIndices 	= [0, 1, 2, 3]
		self._drawStyle 	= pyglet.graphics.GL_QUADS
		self._perpDiag		= vec(-self._width/2, self._height/2)
		self._perpDiagRot	= self._perpDiag.getAngleTo(XAxisVector)

	''''''''''''''''''''''''''''''''''''''''''
		
	def updatePoints(self):
		wp 	= self._worldPos
		d	= self._diagonal
		d2 	= self._perpDiag
		
		self._points = [wp.x - d.x, wp.y - d.y, wp.x - d2.x, wp.y - d2.y, wp.x + d.x, wp.y + d.y, wp.x + d2.x, wp.y + d2.y]
		
		if(self._vertexList):
			self._vertexList.vertices = self._points

	''''''''''''''''''''''''''''''''''''''''''
	
	#-----------------------------------#
	#		Data Maintenance			#
	#-----------------------------------#
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
	def _onRotation(self, dif):
		super()._onRotation(dif)
		pr 	= self._worldRot + self._perpDiagRot
		
		self._perpDiag.x = math.cos(pr)*self._dLength
		self._perpDiag.y = math.sin(pr)*self._dLength
	def _onScale(self, dif):
		super()._onScale(dif)
		self._perpDiag *= dif
		
#--------------------------------------------#
	
class SceneEllipse(GeometryEllipse, _ScenePrimitive):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._triangleCount = getDictValue(kwArgs, 26, ['tc', 'triangleCount'])
		self._numPoints		= self._triangleCount+1
		self._pointIndices 	= list(range(self._numPoints)) + [1]
		self._drawStyle 	= pyglet.graphics.GL_TRIANGLE_FAN
		
	''''''''''''''''''''''''''''''''''''
		
	def updatePoints(self):
		wp 	= self._worldPos
		wr  = self._worldRot
		a 	= self._a
		b 	= self._b
		tc 	= self._triangleCount
		
		self._points = ps = [wp.x, wp.y]
		
		Pi2 = math.pi*2
		tAngle = 0.0; 	tStep = Pi2/tc
		
		while tAngle < Pi2-tStep:
			t = tAngle
			
			sT  = math.sin(t)
			csT = math.cos(t)
			
			x = wp.x + a.x*csT + b.x*sT
			y = wp.y + a.y*csT + b.y*sT
		
			ps.append(x); ps.append(y)
			tAngle += tStep
				
		if(self._vertexList):
			self._vertexList.vertices 	= self._points
		
#--------------------------------------------#

class SceneRay(GeometryLine, _ScenePrimitive):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._numPoints 	= 4
		self._pointIndices 	= [0, 1, 1, 2, 1, 3]
		self._drawStyle		= pyglet.graphics.GL_LINES

	''''''''''''''''''''''''''''''''''''
	
	def updatePoints(self):
		start = self._worldPos
		end   = self._end
		
		line 		= end-start
		lineAngle 	= line.getAngleTo(XAxisVector)
		lineLength	= line.length()
		
		Pi4 		= math.pi/4
		length8 	= lineLength/8
		
		p1Angle 	= lineAngle + Pi4
		p1 			= end - vec(math.cos(p1Angle), math.sin(p1Angle))* length8
		
		p2Angle 	= lineAngle - Pi4
		p2 			= end - vec(math.cos(p2Angle), math.sin(p2Angle)) * length8
			
		self._points = [start.x, start.y, end.x, end.y, p1.x, p1.y, p2.x, p2.y]
		if(self._vertexList):
			self._vertexList.vertices = self._points
	
#------------------------------------------------------#

class ScenePoints(_ScenePrimitive):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._vPoints		= getDictValue(kwArgs, None, ['ps', 'points'], True) 
		self._numPoints 	= len(self._vPoints)
		self._pointIndices 	= list(range(self._numPoints))
		self._drawStyle		= pyglet.graphics.GL_POINTS
		
	''''''''''''''''''''''''''''''''''''''''''
	
	def updatePoints(self):
		self._points.clear()
		
		for p in self._vPoints:
			self._points.append(p.x + self._worldPos.y)
			self._points.append(p.y + self._worldPos.y)


	#---------------------------------------#
	#			Data Maintenance			#
	#---------------------------------------#
	
	def _onRotation(self, dif):
		super()._onRotation(dif)
		
		for p in self._vPoints:
			pL 	= p.length()
			
			try:
				angle = p.getAngleTo(XAxisVector) + dif
			except(ZeroDivisionError):
				continue
			
			p.x = math.cos(angle)*pL
			p.y = math.sin(angle)*pL
	
	def _onScale(self, dif):
		super()._onScale(dif)
		
		for point in self._vPoints:
			point *= dif
			
#------------------------------------------------------#