
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
		if isinstance(image, pyglet.image.AbstractImage):
			self._texture = image.get_texture()
		else:
			self._texture = pyglet.image.load(image).get_texture()
		kwArgs['src'] = DiscreteRect(self._texture.width, self._texture.height)

		super().__init__(**kwArgs)
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def draw(self):
		glEnable(self._texture.target)
		glBindTexture(self._texture.target, self._texture.id)
		
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
		
		super().draw()
		glDisable(self._texture.target)
