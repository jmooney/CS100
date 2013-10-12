
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
import Color
import pyglet.graphics as pGraphics
from CS100.Tools import getDictValue
from SceneObject import SceneObject


#------------------------------------------------------#

class ScenePrimitive(SceneObject):
	
	def __init__(self, transform=None, dataSrc=None, **kwArgs):
		super().__init__(transform)
		
		self._dataSrc = None
		if dataSrc:
			self.attachSrc(dataSrc)
		
		self._group = getDictValue(kwArgs, None, ['g', 'group'])
		self._batch = getDictValue(kwArgs, None, ['b', 'batch'])
		self._color = getDictValue(kwArgs, Color.White, ['c', 'color'])
		self._drawStyle = getDictValue(kwArgs, GL_TRIANGLES, ['ds', 'drawStyle'])
		self._arrayListArgs = kwArgs.get('arrayListArgs', [])
	
	
	def __del__(self):
		self._vertexList.delete()
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		if self._batch:
			raise Exception("Batched SceneObject Erroneously Drawn Directly")
		self._vertexList.draw(self._drawStyle)


	def attachSrc(self, dataSrc):
		self.detachSrc()
		self._dataSrc = dataSrc

		vertices, vertexIndices = self._dataSrc.getVertices()
		if not self._colors:
			self._colors = self._color * len(vertices)
	
		if self._batch:
			self._vertexList = self._batch.add_indexed(len(vertices), self._drawStyle, self._group, vertices, vertexIndices, ('c3B', self._colors), *self._dataSrc.getDrawData())
		else:
			self._vertexList = pGraphics.vertex_list_indexed(len(vertices), vertices, vertexIndices, ('c3B', self._colors), *self._dataSrc.getDrawData())

			
	def detachSrc(self):
		if self._dataSrc:
			self._vertexList.delete()
			self._vertexList = None
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setColor(self, color):
		self._color = color
		self._colors = color*self._numVerts
	def setColors(self, colors):
		self._color = colors
		for i in range(len(colors)):
			self._colors = colors[i]
			
			
	def setTexCoords(self, txCordFmt):
		self._vertexList.tex_coords = txCordFmt
	



#-----------------------------------------------------#

class VertexDataSource(object):

	def __init__(self, *args):
		super().__init__(*args)
		
		self._vertices = []
		self._vertexIndices = []


 	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def getVertices(self):
		return self._vertices, self._vertexIndices
	def getDrawData(self):
		return []

