'''

	Author: John Mooney
	Date:	12/19/2012
	
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
	
	def __initVars__(self, **kwArgs):
		super().__initVars__(**kwArgs)
		
		self._resources 		= {}
		self._resourceBuilds 	= {}
	
	###################################
	###################################

	def request(self, resFileName):
		if(resFileName in self._resources.keys()):
			return self._resources[resFileName]
		else:
			return self._loadResource(resFileName)
		
	def free(self, res):
		maxRefCount = 1 + 1 + 1 + 1
		if(sys.getrescount(res) <= maxRefCount):
			del(self._resources[res.filename])

	###################################
	###################################
	
	def _loadResource(self, resFileName):
		resType = FileManager.getFileType(resFileName)
		resource = self._resourceBuilds[resType](resFileName)
		resource.load()
		
		self._resources.append(resource)
		return resource

		
#------------------------------------------#

class Resource(Object):

	def __initVars__(self, **kwArgs):
		super().__initVars__(self, **kwArgs)
		self.filename = getDictValue(kwArgs, "", ['f', 'filename'], True)
		
	################################
	################################
	
	def load(self):
		raise NotImplementedError()
