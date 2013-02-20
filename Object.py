
'''

	Project:	CS100
	Title:		Object

	Author:		John Mooney
	Date:		10/24/2012

	Description:
		A custom object super-class that accepts a dictionary list as an init parameter
'''

class Object(object):

	#-----------------------------------------------#
	#		Wrapper for passing kwArgs to super()	#
	#-----------------------------------------------#
	
	def __init__(self, **kwArgs):
		super().__init__()
		self.__initVars__(**kwArgs)
		self.__initData__(**kwArgs)
		
	''''''''''''''''''''''''''''''''''''''
	
	#	Initalizes Variables to default values
	#		- Creates all parent-variables before child-variables 
	def __initVars__(self, **kwArgs):
		pass
		
	#	Sets parent variable data utilizing personal-variables within children		#
	#		- Assumes child personal-variables have a determined value
	#		- A personal-variable is a variable independent of a parent's data
	#		- Can modify child personal-variables;
	#		- Makes no assumptions about child initData's
	def __initData__(self, **kwArgs):
		pass
