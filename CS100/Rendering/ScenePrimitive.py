
'''

	Project:	CS100
	Title:		SceneObject

	Author:	John Mooney
	Date:		10/12/2013

	Description:
		Converts basic vertex data into a drawable object
		Vertex data is pipelined from a dataSrc object
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
	
	def __init__(self, sceneNode=None, dataSrc=None, **kwArgs):
		super().__init__(sceneNode)
		
		self._colors = None
		self._dataSrc = None
		self._vertexList = None
		
		self._group = getDictValue(kwArgs, pGraphics.null_group, ['g', 'group'])
		self._batch = getDictValue(kwArgs, None, ['b', 'batch'])
		self._color = getDictValue(kwArgs, Color.White, ['c', 'color'])
		self._drawStyle = getDictValue(kwArgs, GL_TRIANGLES, ['ds', 'drawStyle'])
		self._arrayListArgs = kwArgs.get('arrayListArgs', [])
		
		if dataSrc:
			self.attachSrc(dataSrc)
	
	
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
			

	def attachSrc(self, dataSrc):
		self.detachSrc()
		self._dataSrc = dataSrc

		vertices, vertexIndices = self._dataSrc.getVertices()
		numVerts = int(len(vertices)/2)
		
		if not self._colors:
			self._colors = list(self._color * numVerts)
		if self._batch:
			self._vertexList = self._batch.add_indexed(numVerts, self._drawStyle, self._group, vertexIndices, ('v2f', vertices), \
					('c3B', self._colors), *self._arrayListArgs)
		else:
			self._vertexList = pGraphics.vertex_list_indexed(numVerts, vertexIndices, ('v2f', vertices), \
					('c3B', self._colors),  *self._arrayListArgs)

			
	def detachSrc(self):
		if self._dataSrc:
			self._vertexList.delete()
			self._vertexList = None
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setSceneNode(self, sceneNode):
		retVal = super().setSceneNode(sceneNode)
		if self._sceneNode:
			self._sceneNode.addScenePrimitive(self)
		return retVal
			
	
	def setColor(self, color):
		self._color = color
		self._colors = list(color*self._numVerts)
	def setColors(self, colors):
		self._color = colors
		for i in range(len(colors)):
			self._colors[i] = colors[i]
			#self._vertexList.colors[i] = colors[i]
			
	def setTexCoords(self, txCordFmt):
		self._vertexList.tex_coords = txCordFmt
	



#-----------------------------------------------------#

class VertexDataSource(object):

	def __init__(self, vertices = [], vertexIndices = []):
		super().__init__()
		
		self._vertices = vertices
		self._vertexIndices = vertexIndices


	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def getVertices(self):
		return self._vertices, self._vertexIndices
	def getDrawData(self):
		return []

