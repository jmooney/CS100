
'''

	Project:	CS100
	Title:		Shape

	Author:	John Mooney
	Date:	10/12/2013

	Description:
		A shape as defined by a set of points;	Can be used for rendering shapes on screen
'''


# Imports
import math
from CS100.Math.Vector import vec
from CS100.Space.Transformable import Transformable
from CS100.Space.TransformationGraph import TransformationGraph


#------------------------------------------------------#
#	Shape

class Shape(object):

	def __init__(self, vertices = [], vertexIndices = []):
		super().__init__()
		
		self._vertices = vertices
		self._vertexIndices = vertexIndices
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getVertices(self):
		return self._vertices, self._vertexIndices



#------------------------------------------------------#
#	TransformableShape

class TransformableShape(Shape, Transformable):
	
	def __init__(self, baseShape, transform=None):
		super().__init__(baseShape._vertices[:], baseShape._vertexIndices[:])

		self._base = baseShape
		self.setTransform(transform)

		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _onTranslation(self, dif):
		pass
		
		
	def _onRotation(self, dif):
		super()._onRotation(dif)
		
		c=math.cos(dif);	s=math.sin(dif)
		for i in range(0, len(self._vertices), 2):
			vx = self._vertices[i]
			vy = self._vertices[i+1]
			
			self._vertices[i] = vx*c - vy*s
			self._vertices[i+1] = vx*s + vy*c		
		
		
	def _onScale(self, dif):
		super()._onScale(dif)
		
		for i in range(0, len(self._vertices), 2):
			self._vertices[i]*=dif.x
			self._vertices[i+1]*=dif.y



#------------------------------------------------------#
#	Creating Shapes

def makeCircle(numDivisions=12):
	
	vertices 		= []
	currentAngle 	= 0.0
	totRadians 	= 2*math.pi
	angleStep 		= totRadians/numDivisions
	
	while currentAngle <= totRadians:
		x = math.cos(currentAngle)
		y = math.sin(currentAngle)
		
		vertices.append(x)
		vertices.append(y)
		
		currentAngle += angleStep
	
	return Shape(vertices, range(len(vertices)))
	

def getRect(width, height):
	return TransformableShape(Rectangle, TransformationGraph.activeGraph.newNode(scale=vec(width, height)))



#------------------------------------------------------#
#	Define some Common Shapes

Rectangle 	= Shape([-1, -1, 1, -1, 1, 1, -1, 1], [0, 1, 2, 3])
Circle		= makeCircle()


