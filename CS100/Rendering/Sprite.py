
'''

	Project:	CS100
	Title:		Sprite

	Author:		John Mooney
	Date:		3/29/2013

	Description:
		Represents an instance of an image
		Handles drawing/loading and provides an interface to underlying image data
'''

# Imports
import pyglet.image
from pyglet.gl import *

from SceneObject import SceneObject
from AnimationState import AnimationState
from CS100.Space.Transformable import Transformable
from CS100.Subsystems.Resources.Animation import Animation
from CS100.Math.Primitives.DiscretePrimitives import DiscreteRect


class Sprite(Transformable):

	def __init__(self, imageSrc, transform=None, **kwArgs):
		super().__init__(transform)

		#	Set Image/Animation
		if isinstance(imageSrc, Animation):
			self._animation = AnimationState(imageSrc)
			self._texture = self._animation.getImage().get_texture()
		else:
			self._animation = None
			self._texture = imageSrc.get_texture()
			
		#	Create the Scene Object representation
		self._sceneObject = SceneObject(self.getTransform(), dataSrc=DiscreteRect(self._texture.width, self._texture.height),	\
			ed=[('t3f', self._texture.tex_coords)], **kwArgs)
		self._sceneObject.isDrawn = False  
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if self._animation and self._animation.update(dt):
			self._texture = self._animation.getImage().get_texture()
	
	def draw(self):
		glBindTexture(self._texture.target, self._texture.id)
		glEnable(self._texture.target)
		
		self._sceneObject.draw()
		
		glDisable(self._texture.target)

	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getImage(self):
		return self._texture
		
	def setAnimation(self, animState):
		self._animation.setState(animState)
	def getAnimation(self):
		return self._animation
