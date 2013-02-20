
'''

	Project:	CS100
	Title:		DebugDrawingManager

	Author:		John Mooney
	Date:		1/22/2013

	Description:
		Manages drawing of primitive objects called through the debug facility
'''

# Imports
from Object import Object

import pyglet
from queue import PriorityQueue

import TransformationGraph
from ScenePrimitives import *
from Vector import vec
from tools import getDictValue


ddm = None

#-----------------------------------------------------#

class DebugDrawingManager(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._debugDrawBatch 	= pyglet.graphics.Batch()
		self._dataList			= []
	
	''''''''''''''''''''''''''''''

	def update(self, dt):
		tempList = []
		for debugObject in self._dataList:
			if(debugObject.age(dt)):
				tempList.append(debugObject)
			else:
				debugObject.destroy()
		
		self._dataList = tempList


	def draw(self):
		self._debugDrawBatch.draw()
	
	
	''''''''''''''''''''''''''''''	

	def _drawPrimitive(self, primCreator, kwArgs):
		kwArgs['batch'] = self._debugDrawBatch
		
		p 	= primCreator(**kwArgs)
		dd 	= _DebugDrawData(p, **kwArgs)
		
		self._dataList.append(dd)
		
	def drawRect(self, center, width, height, **kwArgs):
		if not 't' in kwArgs:
			kwArgs['t'] = TransformationGraph.tg.newTransform(t = center)
		kwArgs['w']		= width
		kwArgs['h']		= height
		
		self._drawPrimitive(SceneRect, kwArgs)
		
	def drawEllipse(self, center, a, b, **kwArgs):
		if not 't' in kwArgs:
			kwArgs['t'] = TransformationGraph.tg.newTransform(t = center)
		kwArgs['a']		= a
		kwArgs['b']		= b
		
		self._drawPrimitive(SceneEllipse, kwArgs)
		
	def drawRay(self, start, vector, **kwArgs):
		if not 't' in kwArgs:
			kwArgs['t'] = TransformationGraph.tg.newTransform(t = start)
		kwArgs['e']		= vector

		self._drawPrimitive(SceneRay, kwArgs)
		
	def drawPoints(self, points, center, **kwArgs):
		if not 't' in kwArgs:
			kwArgs['t'] = TransformationGraph.tg.newTransform(t = center)	
		kwArgs['ps'] 	= points

		self._drawPrimitive(ScenePoints, kwArgs)

#---------------------------------------------------#

class _DebugDrawData(Object):

	def __init__(self, primitive, **kwArgs):
		kwArgs['p'] = primitive
		super().__init__(**kwArgs)
		
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._lifeTime 	= getDictValue(kwArgs, 0.0, ['lt', 'lifetime', 'lifeTime'])
		self._drawOrder = getDictValue(kwArgs, 0, ['do', 'drawOrder'])
		self._primitive = kwArgs['p']

	''''''''''''''''''''''''''''''''''''''''''
	
	def age(self, dt):
		self._lifeTime -= dt
		return self._lifeTime > 0.0
		
	def destroy(self):
		self._primitive.killTransform()
		self._primitive.deleteVertexList()
				
#---------------------------------------------------#

