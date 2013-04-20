
'''

	Project:	CS100
	Title:		ScenePrimitives

	Author:		John Mooney
	Date:		1/23/2013

	Description:
		Entry point for running a debug CS100 version
'''

# Imports
import pyglet
import sys
import os

from pyglet.graphics import GL_LINES


'''		Set Search Directory	'''
for root, direcs, files in os.walk(os.getcwd()):
	for direc in direcs:
		sys.path.append(os.path.join(root, direc))


# Imports
import Color

from Renderer import Renderer
from TransformationGraph import Transform

from SceneObject import SceneObject
from DiscretePrimitives import *
from Sprite import Sprite
from Vector import vec

#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

rendMan = Renderer(winSize=winDimensions)
sg = rendMan.getSceneGraph()

S = Sprite("C:/Users/John/Pictures/Lake.jpg", t=sg.newTransform())
pyglet.gl.glClearColor(1,1,1,0);

def update(dt):
	S.translate2f(.01, 0)
	
	
@window.event
def on_draw():
	window.clear()
	rendMan.render()

pyglet.clock.schedule(update)
pyglet.app.run()

