
'''

	Project:	CS100
	Title:		AbsolutePrimitives

	Author:		John Mooney
	Date:		2/26/2013

	Description:
		Represents geometric shapes as a set of absolute, discrete points
'''


# Imports



#-----------------------------------------------#

class AbsolutePrimitive(Object):

	def __initData__(self, **kwArgs):
		super.__initData__(**kwArgs)
		self.__data = self._points[:]
	
	
	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def _onTranslation(self, dif):
		super()._onTranslation(dif)
		for p in self._points:
			p+=dif
			
	def _onRotation(self, dif):
		super()._onRotation(dif)
		
		c=math.cos(dif);	s=math.sin(dif)
		for v in self.__data:
			v.x = v.x*c - v.y*s
			v.y = v.x*s + v.y*c		

	def _onScale(self, dif):
		super()._onScale(dif)
		for v in self.__data:
			v*=dif
			

#-----------------------------------------------#

class AbsoluteRect(AbsolutePrimitive, DiscreteRect):
	def __initData__(self, **kwArgs):
		super().__initData__(**kwArgs)
		self.__data[:] = self.__data+[self._diagonal]
		
	def _onScale(self, dif):
		super()._onScale(dif)
		self._width *= dif.x
		self._height *= dif.y
		
		
#-----------------------------------------------#

class AbsoluteEllipse(AbsolutePrimitive, DiscreteEllipse):
	def __initData__(self, **kwArgs):
		super().__initData__(**kwArgs)
		self.__data[:] = self.__data+[self._a, self._b]
		
#-----------------------------------------------#

class AbsoluteLine(AbsolutePrimitive, DiscreteLine):
	def __initData__(self, **kwArgs):
		self.__data[:] = self.__data+[self._endVec]
		super().__initData__(**kwArgs)
		