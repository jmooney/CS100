
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


class Sprite(SceneObject):

	def __init__(self, imageSrc, sceneNode=None, **kwArgs):
		super().__init__(sceneNode)

		#	Set Image/Animation
		if isinstance(imageSrc, Animation):
			self._animation = AnimationState(imageSrc)
			self._texture = self._animation.getImage().get_texture()
		else:
			self._animation = None
			self._texture = imageSrc.get_texture()
			
		#	Create the Scene Primitive representation
		self._scenePrimitive = ScenePrimitive(self._sceneNode.createChild(), DiscreteRect(self._texture.width, self._texture.height))
		self._scenePrimitive.setTexCoords(self._texture.tex_coords)
			
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if self._animation and self._animation.update(dt):
			self._texture = self._animation.getImage().get_texture()
	
	def draw(self):
		glBindTexture(self._texture.target, self._texture.id)
		glEnable(self._texture.target)
		
		self._sceneObject.draw()
		
		glDisable(self._texture.target)

	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def getImage(self):
		return self._texture
		
	def setAnimation(self, animState):
		self._animation.setState(animState)
	def getAnimation(self):
		return self._animation

		