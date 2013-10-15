
'''

	Project:	CS100
	Title:		RenderGrups

	Author:		John Mooney
	Date:		10/12/2013

	Description:
			A number of common-use pyglet state groups used for rendering
'''

# Imports
from pyglet.gl import (glBindTexture, glEnable, glDisable, GL_TEXTURE_2D)
from pyglet.graphics import (Batch, Group)


#-----------------------------------------------#
#	TextureGroup

class EnableTexturingGroup(Group):
	
	def __init__(self, target, parent=None):
		super().__init__(parent)
		self._texTarget = target
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def set_state(self):
		glEnable(self._texTarget)
	def unset_state(self):
		glDisable(self._texTarget)

Enable2DTexGroup = EnableTexturingGroup(GL_TEXTURE_2D)

#-----------------------------------------------#
#	TextureGroup

class TextureGroup(Group):

	def __init__(self,  texture=None, parent=Enable2DTexGroup,):
		super().__init__(parent)
		self._texture = texture
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def set_state(self):
		glBindTexture(self._texture.target, self._texture.id)
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setTexture(self, texture):
		self._texture = texture

		
#-----------------------------------------------#
#	Create Null Group and Batch

NullBatch = Batch()