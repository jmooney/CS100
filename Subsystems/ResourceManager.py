
'''

	Author: John Mooney
	Date:	4/8/2013
	
	Description:
		Resource Manager - Handles resource management within CS100. 
			- Maintains referential integrity
			- Ensures 1 allocated resource in memory
			- Provides pre, post initialization and custom resource loading
			
'''

# Imports
from Object import Object
from tools import getDictValue


#------------------------------------------#

class ResourceManager(Object):

	def __init__(self, directory, **kwArgs):
		super().__init__(**kwArgs)
		self._directory = directory
		
		
	def __initP__(self, **kwArgs):
		super().__initP__(**kwArgs)
		
		self._resources = {}
		self._resourceGroups = {}
		self._resourceGroupStack = []
		self._activeResourceGroups = []
		

	''''''''''''''''''''''''''''''''''''''''''''''''
	
	#	request(self, resourceID)
	#		- Object-level resource access
	def request(self, resId):
		pass
		

	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def pushGroup(self, group):
		if groupId isinstance(str):
			self.pushGroup(self.createGroup(groupName = group)):
		else:
			self._resourceGroupStack.append(group)
			self._activeResourceGroups.append(group)
	def popGroup(self):
		self._activeResourceGroups.remove(self._resourceGroupStack.pop())
	
	
	def createGroup(self, groupName):
		pass
	
		
#-------------------------------------------#
	
class ResourceGroup(Object):

	def __initP__(self, **kwArgs):
		super().__initP__(**kwArgs)
		self._resourceIds = []


	''''''''''''''''''''''''''''''''''''''''''''''''
	
	def addResource(self, resFileName):
		pass
	def removeResource(self, resId):
		pass
	
	
	#	Group Creation (Stack Based?)
	#	Group Loading/Removal (Stack Based?)
	#	Resource requests/access
	#	Groups:
	#		Easy loading/saving of resources; Information regarding number of resources allocated
	
