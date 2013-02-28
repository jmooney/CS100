
'''

	Project:	CS100
	Title:		SceneObject

	Author:		John Mooney
	Date:		2/27/2013

	Description:
		Converts basic vertex data into a drawable object
'''

# Imports
import Color
from pyglet.graphics import (vertex_list_indexed, GL_POINTS)


from Object import Object
from Transformable import Transformable

from tools import getDictValue

#------------------------------------------------------#
#
#	- Consider adding \static modifier to vertexList
#
#------------------------------------------------------#


class SceneObject(Transformable):
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._dataSrc = getDictValue(kwArgs, None, ['s', 'src', 'source'])
		if(self._dataSrc):
			vs, vis, ds = self._dataSrc.getVertexData()
		else:
			vs 	= getDictValue(kwArgs, None, ['vs', 'verts', 'vertices'], True)
			vis = list(range(len(vs)))
			ds	= GL_POINTS
			
		color = getDictValue(kwArgs, Color.White, ['c', 'color'])
		
		self._vertices 		= vs
		self._vertexIndices = getDictValue(kwArgs, vis, ['vis', 'vertIndices', 'vertexIndices'])
		self._drawStyle 	= getDictValue(kwArgs, ds, ['ds', 'drawStyle'])
		
		self._numVertices 	= len(vs)
		self._colors	  	= getDictValue(kwArgs, color*self._numVertices, ['cs', 'colors'])

		self._buildVertexList()
		
	
	def __del__(self):
		self._vertexList.delete()
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _buildVertexList(self):
		data = []
		for v in self._vertices:
			data.append(v.x)
			data.append(v.y)
			
		self._vertexList = vertex_list_indexed(self._numVertices, self._vertexIndices,
			('v2f/static', data), ('c3B', self._colors))
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		self._vertexList.draw(self._drawStyle)
		
		
#-----------------------------------------------------#

class VertexDataSource(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		self._drawStyle = GL_POINTS

	def getVertexData(self):
		raise NotImplementedError
