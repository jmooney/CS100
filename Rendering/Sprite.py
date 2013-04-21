
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
from AnimationState import AnimationState
from Animation import Animation
from DiscretePrimitives import DiscreteRect

class Sprite(SceneObject):

	def __init__(self, imageSrc, **kwArgs):
		if isinstance(imageSrc, Animation):
			self._animation = AnimationState(imageSrc)
			self._animation.setState("Looping")
			self._texture = self._animation.getImage().get_texture()
		else:
			self._animation = None
			self._texture = image.get_texture()
			

		# Set Sprite-Specific Rect-Creation Arguments
		kwArgs['dataSrc'] = DiscreteRect(self._texture.width, self._texture.height)
		kwArgs['ed'] = [('t2f', [0, 0, 1, 0, 1, 1, 0, 1])]
		
		super().__init__(**kwArgs)
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if self._animation and self._animation.update(dt):
			self._texture = self._animation.getImage().get_texture()
	
	def draw(self):
		glEnable(self._texture.target)
		glBindTexture(self._texture.target, self._texture.id)
		
		super().draw()
		
		glDisable(self._texture.target)
