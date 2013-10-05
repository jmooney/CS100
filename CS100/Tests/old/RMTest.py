
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

import CS100 as Src
import Src.Rendering.Color
from Src.Rendering.Renderer import Renderer
from Src.Subsystems.Tree import Tree
from Src.Rendering.SceneGraph2 import SceneGraph
from Src.Space.TransformationGraph2 import TransformationGraph

from pyglet.graphics import GL_LINES


# Imports
import Color

from Vector import vec
from Sprite import Sprite
from Renderer import Renderer
from Animation import Animation
from TransformationGraph import Transform
from ResourceManager import ResourceManager

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

anim1 = rm.request("CharizardEvolve.anim")
anim2 = rm.request("PShip.anim")

s1 = Sprite(anim1, sg.newTransform())
s2 = Sprite(anim2, sg.newTransform(t=vec(-200,100)))

s1.setAnimation("Alternating")
s2.setAnimation("Looping")


print("")
rm.debugDisplay()
print("")


def update(dt):
	s1.update(dt)
	s2.update(dt)

	
	
@window.event
def on_draw():
	window.clear()
	rendMan.render()

pyglet.clock.schedule(update)
pyglet.app.run()

