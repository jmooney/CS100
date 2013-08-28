
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
from ResourceManager import ResourceManager

from Vector import vec
from Sprite import Sprite
from Animation import Animation

#-------------------------------------------------------#	

window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

rendMan = Renderer(winDimensions)
Renderer.activeRenderer = rendMan

sg = rendMan.getSceneGraph()

rm = ResourceManager("Tests\\data")
ResourceManager.activeManager = rm
rm.registerExtension(".jpg", "img", ["img"], pyglet.image.load)
rm.registerExtension(".bmp", "img", ["img"], pyglet.image.load)
rm.registerExtension(".png", "img", ["img"], pyglet.image.load)
rm.registerExtension(".anim", "anim", ["anim"], Animation)

im = rm.request("C:/Users/Bonsackjohn/Pictures/Misc/Triforce.jpg")

sp = pyglet.sprite.Sprite(im, x=im.width/8, y=-im.height/2)
sp2 = Sprite(im, sg.newTransform(t=vec(-im.width*5/8, 0)))

pyglet.gl.glClearColor(1,1,1,0);
def update(dt):
	pass
	
	
@window.event
def on_draw():
	window.clear()
	rendMan.render()
	sp.draw()

pyglet.clock.schedule(update)
pyglet.app.run()

