
'''

	Project:	CS100
	Title:		EventTest

	Author:		John Mooney
	Date:		1/16/2014

	Description:
		Entry point for running a debug CS100 version - Event
'''

# Imports
import pyglet
from pyglet.gl import GL_TRIANGLE_FAN

import random
from CS100.Rendering import Color
from CS100.Math.Vector import vec
from CS100.Subsystems.Tree import Tree
from CS100.Math.Shape import Shape, Circle
from CS100.Rendering.Renderer import Renderer
from CS100.Rendering.SceneGraph import SceneGraph
from CS100.Rendering.ScenePrimitive import ScenePrimitive
from CS100.Subsystems.Events import *

from pyglet.graphics import (GL_LINES, GL_TRIANGLES)


#--------------------------------------------------------#
#	DebugEventNode

class DebugEventListener(EventListener, EventSource):

	def __init__(self, sceneNode, sendTime, changeTime):
		super().__init__()

		self._scenePrimitive = ScenePrimitive(sceneNode, Circle, color = Color.Yellow, drawStyle = GL_TRIANGLE_FAN)
		
		self._timeElapsed = 0.01
		self._sTime = sendTime
		self._cTime = changeTime
		self._currentColor = 'Y'
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		self._timeElapsed+=dt
		
		if (self._timeElapsed % self._sTime < 0.015):
			self.sendEvent(0, self._currentColor, "")
			print("Sending " + self._currentColor + "...")

		if (self._timeElapsed % self._cTime < 0.015):
			print("Changing Color... ")
			c = random.randint(0, 4)
			
			if c==0:
				self._scenePrimitive.setColor(Color.Yellow)
				self._currentColor = 'Y'
			elif c==1:
				self._scenePrimitive.setColor(Color.Red)
				self._currentColor = 'R'
			elif c==2:
				self._scenePrimitive.setColor(Color.White)
				self._currentColor = 'W'
			elif c==3:
				self._scenePrimitive.setColor(Color.Black)
				self._currentColor = 'B'
			elif c==4:
				self._scenePrimitive.setColor(Color.Teal)
				self._currentColor = 'T'
				
		if self._timeElapsed > 100000:
			self._timeElapsed = 0
				
		self.processEvents()
	
	def processEvent(self, event):
		e = event.description
		
		if e=='Y':	
			self._scenePrimitive.setColor(Color.Yellow)
			self._currentColor = 'Y'
		elif e=='R':
			self._scenePrimitive.setColor(Color.Red)
			self._currentColor = 'R'
		elif e=='W':
			self._scenePrimitive.setColor(Color.White)
			self._currentColor = 'W'
		elif e=='B':
			self._scenePrimitive.setColor(Color.Black)
			self._currentColor = 'B'
		elif e=='T':
			self._scenePrimitive.setColor(Color.Teal)
			self._currentColor = 'T'
			
	
		
#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph.activeGraph = SceneGraph(baseTree)

renderer = Renderer(winDimensions, sceneGraph)


#-------------------------------------------------------#

sceneNode1 = sceneGraph.newNode(t=vec(0, 200), s=vec(30, 30))
sceneNode2 = sceneGraph.newNode(t=vec(-100, 0), s=vec(30, 30))
sceneNode3 = sceneGraph.newNode(t=vec(100, 0), s=vec(30, 30))
sceneNode4 = sceneGraph.newNode(t=vec(-200, -200), s=vec(30, 30))
sceneNode5 = sceneGraph.newNode(t=vec(200, -200), s=vec(30, 30))

eventListener1 = DebugEventListener(sceneNode1, 0,0)
eventListener2 = DebugEventListener(sceneNode2, 0,0)
eventListener3 = DebugEventListener(sceneNode3, 0,0)
eventListener4 = DebugEventListener(sceneNode4, 5, 3)
eventListener5 = DebugEventListener(sceneNode5, 5, 3)

eventListener5.addListener(eventListener3)
eventListener4.addListener(eventListener2)
eventListener3.addListener(eventListener1)
eventListener2.addListener(eventListener1)


def update(dt):
	eventListener1.processEvents()
	eventListener2.processEvents()
	eventListener3.processEvents()
	eventListener4.update(dt)
	eventListener5.update(dt)
	
	
@window.event
def on_draw():
	window.clear()
	renderer.render()
	

pyglet.clock.schedule(update)
pyglet.app.run()

