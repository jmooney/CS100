
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
from pyglet.gl import GL_QUADS

from CS100.Rendering import Shape
from .SceneObject import SceneObject
from CS100.Rendering import RenderGroups
from .AnimationState import AnimationState
from .ScenePrimitive import ScenePrimitive
from CS100.Subsystems.Resources.Animation import Animation


#------------------------------------------------------#
#	Sprite

class Sprite(SceneObject):

	def __init__(self, imageSrc, sceneNode=None, **kwArgs):
		super().__init__(sceneNode)

		#	Set Image/Animation
		if isinstance(imageSrc, Animation):
			self._animation = AnimationState(imageSrc)
			self._texture = self._animation.getImage().get_texture()
			self._imageGroup = self._animation.getTextureGroup()
			aListArgs = ['t3f']
			
		else:
			self._animation = None
			self._texture = imageSrc.get_texture()
			self._imageGroup = RenderGroups.TextureGroup(self._texture)
			aListArgs = ['t3f']
			
		#	Create the Scene Primitive representation
		self._scenePrimitive = ScenePrimitive(self._sceneNode.createChild(), Shape.getRect(self._texture.width, self._texture.height), \
				group=self._imageGroup, drawStyle=GL_QUADS, arrayListArgs=aListArgs)
		self._scenePrimitive.setTexCoords(self._texture.tex_coords)

			
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if self._animation and self._animation.update(dt):
			self._texture = self._animation.getImage().get_texture()
			self._scenePrimitive.getShape().setScale2f(self._texture.width, self._texture.height)
			self._scenePrimitive.setTexCoords(self._texture.tex_coords)


	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getImage(self):
		return self._texture
		
	def setAnimation(self, animState):
		self._animation.setState(animState)
	def getAnimation(self):
		return self._animation
		
	def setVisible(self, v):
		super().setVisible(v)
		self._scenePrimitive.setVisible(v)

