
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
from Renderer import Renderer
from TransformationGraph import Transform
from ResourceManager import ResourceManager

from Sprite import Sprite
from Animation import Animation


#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

rendMan = Renderer(winSize=winDimensions)
sg = rendMan.getSceneGraph()

rm = ResourceManager("Tests\\data")
ResourceManager.activeManager = rm
rm.registerExtension(".jpg", "img", ["img"], pyglet.image.load)
rm.registerExtension(".bmp", "img", ["img"], pyglet.image.load)
rm.registerExtension(".anim", "anim", ["anim"], Animation)

anim = rm.request("PShip.anim")
rm.debugDisplay()

'''		Variable Set-Up		'''
s1 = Sprite(anim, t=sg.newTransform())

def update(dt):
	s1.update(dt)
	
	
@window.event
def on_draw():
	window.clear()
	rendMan.render()

pyglet.clock.schedule(update)
pyglet.app.run()
