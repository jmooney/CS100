
'''

	Project:	CS100
	Title:		Renderer

	Author:		John Mooney
	Date:		2/26/2013

	Description:
		Handles rendering of the main display
		Utilizes the active camera and scene graphs for rendering
'''


# Imports
from pyglet.gl import (glClear, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT)

from Camera import Camera
from tools import getDictValue
from SceneGraph import SceneGraph
from TransformationGraph import Transform


#------------------------------------------------------#

class Renderer(object):

	activeRenderer = None
	
	def __init__(self, windowSize):
		super().__init__()
		
		self._sceneGraph 	= SceneGraph()
		self._camera 		= Camera(windowSize, Transform())

		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def render(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		self._camera.focus()
		self._camera.view()
		self._sceneGraph.draw()
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	@classmethod
	def getRenderer(cls):
		return cls.activeRenderer

		
	def setSceneGraph(self, sg):
		self._sceneGraph = sg
	def getSceneGraph(self):
		return self._sceneGraph
		
	def setCamera(self, c):
		self._camera = c
	def getCamera(self):
		return self._camera

