
'''

	Project:	CS100
	Title:		CollisionPrimitives

	Author:		John Mooney
	Date:		2/2/2013

	Description:
		Manages collision detection between geometric primitives
'''

# Imports
import DebugDrawingManager

from GeometryPrimitives import *
from tools import nearEq

#------------------------------------------------------#

class CollisionRect(GeometryRect):

	INTERSECTION	= 1
	CONTAINMENT 	= 2
	PARTITION		= 3

	#--------------------------------------------------#
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)

		self._borders		= []
		self._endPoints 	= []

		self._squaredRadii 	= 0.0
		
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, t):
		if(self._isTransformed):
			self._updateBorders()
			self._updateEndPoints()
			
	def testCollision(self, r2):
		if not self._testDistance(r2):
			return None

		if(self.isAxisAligned()):
			return self._testAACollision(r2)
		else:
			return self._testVectorizedCollision(r2)
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _testDistance(self, r2):
		squaredDist = (r2.getPosition() - self._worldPos).squaredLength()
		return squaredDist < r2._squaredRadii + self._squaredRadii
		
		
	def _testAACollision(self, r2):
		left 	= self._borders[0]
		right 	= self._borders[1]
		bot 	= self._borders[2]
		top 	= self._borders[3]

		DebugDrawingManager.ddm.drawRay(self._worldPos.copy(), self._diagonal.copy())
		DebugDrawingManager.ddm.drawRay(r2._worldPos.copy(), r2._diagonal.copy())
		
		DebugDrawingManager.ddm.drawPoints(self.getPoints(), vec(), c=Color.Blue)
		DebugDrawingManager.ddm.drawPoints(r2.getPoints(), vec(), c=Color.Orange)
		
		collidedPoints = []
		for point in r2.getPoints():
			if (point.x > left and point.x < right \
			and point.y > bot and point.y < top):
				collidedPoints.append(point)
			
		return self._getCollisionInfo(collidedPoints, r2)
	
	
	def _testVectorizedCollision(self, r2):
		collidedPoints = []
		for point in r2.getPoints():
			v 	= point-self._worldPos
			DebugDrawingManager.ddm.drawRay(self._worldPos.copy(), v.copy(), c=Color.Orange)
			
			vL	= v.length()
			vU	= v/vL
			
			DebugDrawingManager.ddm.drawRay(self._worldPos.copy(), vU*40, c=Color.Yellow)
			
			DpUL = self._diagonal.dotP(vU)
			DpU  = vU*DpUL
			
			DebugDrawingManager.ddm.drawRay(self._worldPos, DpU.copy(), c=Color.Blue)
			if(vL < DpUL):
				collidedPoints.append(point)
				
		return self._getCollisionInfo(collidedPoints, r2)
				
				
	''''''''''''''''''''''''''''''''''''''''''''''''''''''

	def _getCollisionInfo(self, collidedPoints, r2):
		
		nCP = len(collidedPoints)
		if	(nCP == len(r2.getPoints())):
			return True#CollisionInfo(CONTAINMENT, collidedPoints)
		elif(nCP > 0):
			return True#CollisionInfo(INTERSECTION, collidedPoints)
		else:
			return None
			

	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	
	def isAxisAligned(self):
		return nearEq(self._worldRot%math.pi/2, 0)
	def getPoints(self):
		ps = []
		for i in range(0, len(self._endPoints), 2):
			ps.append(vec(self._endPoints[i], self._endPoints[i+1]))
			
		return ps
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	#---------------------------------------------------#
	#				Data Maintenance					#
	#---------------------------------------------------#
	
	def _onScale(self, dif):
		super()._onScale(dif)
		self._squaredRadii = self._dLength*self._dLength
	
	
	def _updateBorders(self):
		self._borders = [self._worldPos.x - self._diagonal.x, self._worldPos.x + self._diagonal.x, \
		self._worldPos.y - self._diagonal.y, self._worldPos.y + self._diagonal.y]
	def _updateEndPoints(self):
		wp 	= self._worldPos
		d	= self._diagonal

		pr 	= self._worldRot + math.pi - self._diagonalRot
		d2 	= vec(math.cos(pr)*self._dLength, math.sin(pr)*self._dLength)
		
		self._endPoints = [wp.x - d.x, wp.y - d.y, wp.x - d2.x, wp.y - d2.y, wp.x + d.x, wp.y + d.y, wp.x + d2.x, wp.y + d2.y]

		
#-----------------------------------------------------------------#

