
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

from CS100.Tools import getDictValue
from .SceneObject import SceneObject
import CS100.Rendering.Color as Color


#------------------------------------------------------#
#	Scene Primitive

class ScenePrimitive(SceneObject):
	
	def __init__(self, sceneNode=None, shape=None, **kwArgs):
		super().__init__(sceneNode)
		
		self._colors = None
		self._shape = None
		self._vertexList = None
		
		self._group = getDictValue(kwArgs, pGraphics.null_group, ['g', 'group'])
		self._batch = getDictValue(kwArgs, None, ['b', 'batch'])
		self._color = getDictValue(kwArgs, Color.White, ['c', 'color'])
		self._drawStyle = getDictValue(kwArgs, GL_TRIANGLES, ['ds', 'drawStyle'])
		self._arrayListArgs = kwArgs.get('arrayListArgs', [])
		
		if shape:
			self.attachShape(shape)
	
	def __del__(self):
		if self._vertexList:
			self._vertexList.delete()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		if self._batch:
			raise Exception("Batched SceneObject Erroneously Drawn Directly")
		if self._vertexList:
			self._group.set_state()
			self._vertexList.draw(self._drawStyle)
			self._group.unset_state()
			

	def attachShape(self, shape):
		self.detachShape()
		self._shape = shape
		self._shape.setOwner(self)

		vertices, vertexIndices = self._shape.getVertices()
		numVerts = int(len(vertices)/2)
		
		if not self._colors:
			self._colors = list(self._color * numVerts)
		if self._batch:
			self._vertexList = self._batch.add_indexed(numVerts, self._drawStyle, self._group, vertexIndices, ('v2f', vertices), \
					('c3B', self._colors), *self._arrayListArgs)
		else:
			self._vertexList = pGraphics.vertex_list_indexed(numVerts, vertexIndices, ('v2f', vertices), \
					('c3B', self._colors),  *self._arrayListArgs)

			
	def detachShape(self):
		if self._shape:
			self._vertexList.delete()
			self._vertexList = None
			self._shape.setOwner(None)
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
		self._color = colors
		for i in range(len(colors)):
			self._colors[i] = colors[i]
			self._vertexList.colors[i] = colors[i]
			
	def setTexCoords(self, txCordFmt):
		self._vertexList.tex_coords = txCordFmt
	def getShape(self):
		return self._shape

