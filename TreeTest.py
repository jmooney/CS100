
'''

	Project:	CS100
	Title:		TreeTest

	Author:		John Mooney
	Date:		1/23/2013

	Description:
		Entry point for running a debug CS100 version - Tree
'''

# Imports
import pyglet
import sys
import os


'''		Set Search Directory	'''
for root, direcs, files in os.walk(os.getcwd()):
	for direc in direcs:
		sys.path.append(os.path.join(root, direc))


# Imports
from Tree import Tree
from SceneGraph2 import SceneGraph
from TransformationGraph2 import TransformationGraph



#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph(baseTree)
transformationGraph = TransformationGraph(baseTree)

node2 = baseTree.newNode()
baseTree.debugPrint();	print()
sceneGraph.debugPrint();	print()
transformationGraph.debugPrint();	print()
print('------------------------------------\n')

sceneNode3 = sceneGraph.newNode()
baseTree.debugPrint();	print()
sceneGraph.debugPrint();	print()
transformationGraph.debugPrint();	print()
print('------------------------------------\n')

sn4 = sceneNode3.createChild()
sn5 = sn4.createChild()
baseTree.debugPrint();	print()
sceneGraph.debugPrint();	print()
transformationGraph.debugPrint();	print()
print('------------------------------------\n')


def update(dt):
	pass
	
@window.event
def on_draw():
	window.clear()
	

pyglet.clock.schedule(update)
pyglet.app.run()

