
'''

	Project:	CS100
	Title:		AnimationState

	Author:		John Mooney
	Date:		4/7/2013

	Description:
			An instance of an animation
'''


# Imports



#-----------------------------------------------#

class AnimationState(Object):

	def __initP__(self, **kwArgs):
		super().__initP__(**kwArgs)
		
		self._state		= None
		self._animation = None
		
		self._fps = None
		self._cFrame = None
		self._frameNum = None
		self._repeatMode = None
		
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def update(self, dt):
		super().update(dt)
		
		self._cFrame[1] -= dt;	self._cFrame[2] -= 1
		if(self._cFrame[1] <= 0 or self._cFrame[2] <= 0):
			self._advanceFrame()
			
	
	''''''''''''''''''''''''''''''''''''''''''''''''
		
	def _advanceFrame(self):
		self._frameNum += self._state
		
		if(self._frameNum >= self._animation.getNumFrames()):
			self.dispatchEvent('Animation_End')
			
			if(self._repeatMode == LOOP):
				self._frameNum = 0
			else:
				self._state = PAUSED
			
		if(self._frameNum < 0):
			self.dispatchEvent('Animation_End')
			
			if(self._repeatMode == LOOP):
				self._frameNum = self._animation.getNumFrames()-1
			else:
				self._state = PAUSED
				
		self._cFrame[0] = self._animation.getImage(self._frameNum)
		self._cFrame[1] = self._animation.getTime(self._frameNum)
		self._cFrame[2] = self._animation.getFrameCount(self._frameNum)
		
			
	def setFrame(self, num):
		self._cFrame 	= [self._animation.getImage(num), self._animation.getTime(num), self._animation.getFrameCount(num)]
		self._frameNum 	= num
		
		
	''''''''''''''''''''''''''''''''''''''''''''''''''

	def setAnimation(self, anim):
		self._animation = anim
		self.setFrame(0)

