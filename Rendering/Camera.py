
'''

	Project:	CS100
	Title:		Camera

	Author:		John Mooney
	Date:		2/27/2013

	Description:
		Manages OpenGL Viewport Projections from a 3D point in the world
		Renders the scene from a given perspective
'''


# Imports
from pyglet.gl import *
from math import (sin, cos)

from Transformable import Transformable


#------------------------------------------------------#

class Camera(Transformable):
	
	def __init__(self, winDimensions, transformable=None):
		super().__init__(transformable)
		self._visible=False
		self._winDimensions = winDimensions


	''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def view(self):
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		p = self.getPosition()
		r = self.getRotation()
		s = self.getScale()
		
		gluLookAt(p.x, p.y, 1.0,
					p.x, p.y, -1.0,
					sin(-r), cos(-r), 0.0)
		glScalef(s.x, s.y, 1)
		
		
	def focus(self):
		w = self._winDimensions[0];		h = self._winDimensions[1]
		glViewport(0,0,w,h)
		
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		
		gluOrtho2D(-self._winDimensions[0]/2., self._winDimensions[0]/2., 
			-self._winDimensions[1]/2., self._winDimensions[1]/2.)


	''''''''''''''''''''''''''''''''''''''''''''''''
