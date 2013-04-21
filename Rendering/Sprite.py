
'''

	Project:	CS100
	Title:		Sprite

	Author:		John Mooney
	Date:		3/29/2013

	Description:
		An on screen image instance
'''

# Imports
import pyglet.image
from pyglet.gl import *

from SceneObject import SceneObject
from DiscretePrimitives import DiscreteRect

class Sprite(SceneObject):

	def __init__(self, image, **kwArgs):
		self._texture = image.get_texture()
			
		# Set Sprite-Specific Arguments
		kwArgs['dataSrc'] = DiscreteRect(self._texture.width, self._texture.height)
		kwArgs['ed'] = [('t2f', [0, 0, 1, 0, 1, 1, 0, 1])]
		
		super().__init__(**kwArgs)
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		glEnable(self._texture.target)
		glBindTexture(self._texture.target, self._texture.id)
		
		super().draw()
		glDisable(self._texture.target)
