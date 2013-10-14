
'''

	Project:	CS100
	Title:		AnimationState

	Author:		John Mooney
	Date:		4/7/2013

	Description:
			An instance of an animation. Manages animation playback/pausing etc.
'''


# Imports
from .RenderGroups import TextureGroup

#-----------------------------------------------#
#	AnimationState

class AnimationState(object):

	validStates = ["Idle", "Looping", "Alternating", "Iterating"]

	def __init__(self, animation=None):
		super().__init__()
		
		self._state	= "Idle"

		self._frame			= None
		self._frameIndex 	= 0
		self._animation 	= None
		self._animationDirection = 1
		self._textureGroup = TextureGroup()
		
		if animation:
			self.setAnimation(animation)
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		if self._frame.age(dt):
			self._advanceFrame()
			return True
		return False
		
	def setState(self, state):
		if state not in AnimationState.validStates:
			raise ValueError("Invalid Animation State Argument")
		self._state = state
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _advanceFrame(self):
		if self._state == "Idle":
			return
		
		maxFrameIndex  = self._animation.getFrameCount() - 1
		nextFrameIndex = self._frameIndex + self._animationDirection
		
		#	Check for overflow animation
		if nextFrameIndex > maxFrameIndex:
			#self._dispatchEvent("Finished Animation")
			
			if self._state == "Looping":
				nextFrameIndex = 0
			elif self._state == "Alternating":
				nextFrameIndex = maxFrameIndex-1 if maxFrameIndex > 0 else 0
				self._animationDirection = -self._animationDirection
			else:
				nextFrameIndex = 0
				self._state = "Idle"
				
		#	Check for underflow animation
		if nextFrameIndex < 0:
			#self._dispatchEvent("Finished Animation")
			
			if self._state == "Looping":
				nextFrameIndex = maxFrameIndex
			elif self._state == "Alternating":
				nextFrameIndex = 1 if maxFrameIndex >= 1 else 0
				self._animationDirection = -self._animationDirection
			else:
				nextFrameIndex = 0
				self._state = "Idle"
			
		self.setFrame(nextFrameIndex)
		

	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def setDirection(self, direc):
		self._animationDirection = direc
	
	def setFrame(self, frameIndex):
		self._frame 	 = _FrameState(self._animation.getFrame(frameIndex))
		self._frameIndex = frameIndex
		self._textureGroup.setTexture(self.getImage().get_texture())
		
	def setAnimation(self, animation):
		self._state = "Idle"
		self._animation = animation
		self.setFrame(0)
		
	def getImage(self):
		return self._frame._animationFrame.getImage()
		
	def getTextureGroup(self):
		return self._textureGroup
		
		
		
#-----------------------------------------------------#
#	FrameState

class _FrameState(object):

	def __init__(self, animFrame):
		super().__init__()
		
		self._animationFrame = animFrame
		self._units	= animFrame.getUnits()
		self._timeRemaining = animFrame.getTime()
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	
	def age(self, dt):
		if not self._units:
			return 1
		elif self._units == 'f':
			self._timeRemaining -= 1
		elif self._units == 'm':
			self._timeRemaining -= dt.millis()
		else:
			self._timeRemaining -= dt
		
		return self._timeRemaining <= 0
		
		