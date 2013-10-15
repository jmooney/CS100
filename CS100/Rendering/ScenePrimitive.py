
'''

	Project:	CS100
	Title:		SceneObject

	Author:	John Mooney
	Date:		10/12/2013

	Description:
		Converts basic vertex data into a drawable object
		Vertex data is pipelined from a shape object
'''

# Imports
import pyglet.graphics as pGraphics
from pyglet.gl import GL_TRIANGLES

from .RenderGroups import NullBatch
from CS100.Tools import getDictValue
from .SceneObject import SceneObject
import CS100.Rendering.Color as Color


#------------------------------------------------------#
#	Scene Primitive

class ScenePrimitive(SceneObject):
	
	def __init__(self, sceneNode=None, shape=None, **kwArgs):
		self._colors = None
		self._shape = None
		self._vertexList = None
		
		self._batch = NullBatch
		self._group = getDictValue(kwArgs, pGraphics.null_group, ['g', 'group'])
		self._color = getDictValue(kwArgs, Color.White, ['c', 'color'])
		self._drawStyle = getDictValue(kwArgs, GL_TRIANGLES, ['ds', 'drawStyle'])
		self._arrayListArgs = kwArgs.get('arrayListArgs', [])

		super().__init__(sceneNode)		
		if shape:
			self.attachShape(shape)
			
	
	def __del__(self):
		if self._vertexList:
			self._vertexList.delete()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setBatch(self, batch):
		if not batch:
			batch = getDefaultBatch()
		if self._vertexList:
			self._batch.migrate(self._vertexList, self._drawStyle, self._group, batch)
		self._batch = batch
			

	def attachShape(self, shape):
		self.detachShape()
		self._shape = shape
		self._shape.addListener(self)

		vertices, vertexIndices = self._shape.getVertices()
		numVerts = int(len(vertices)/2)
		self._colors = list(self._color * numVerts)
		
		self._vertexList = self._batch.add_indexed(numVerts, self._drawStyle, self._group, vertexIndices, ('v2f', vertices), \
				('c3B', self._colors), *self._arrayListArgs)
	
			
	def detachShape(self):
		if self._shape:
			self._vertexList.delete()
			self._vertexList = None
			self._shape.removeListener(self)
			self._shape = None
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def updateVertices(self, newVertices, startIndex=0, endIndex=None):
		vertices, _ = self._shape.getVertices()
		if not endIndex:
			endIndex = len(vertices)
		self._vertexList.vertices[startIndex:endIndex] = vertices
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setSceneNode(self, sceneNode):
		retVal = super().setSceneNode(sceneNode)
		if self._sceneNode:
			self._sceneNode.addScenePrimitive(self)
		return retVal
			
	
	def setColor(self, color):
		self._color = color
		self._colors = list(color*self._numVerts)
		self._vertexList.colors=self._colors
	def setColors(self, colors):
		self._color = Color.White
		for i in range(len(colors)):
			self._colors[i] = colors[i]
			self._vertexList.colors[i] = colors[i]
			
	def setTexCoords(self, txCordFmt):
		self._vertexList.tex_coords = txCordFmt
		
	def getShape(self):
		return self._shape

