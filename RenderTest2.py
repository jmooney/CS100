
'''

	Project:	CS100
	Title:		SpriteTest

	Author:		John Mooney
	Date:		10/13/2013

	Description:
		Entry point for running a debug CS100 version - Rendering Test
'''

# Imports
import pyglet
from pyglet.gl import GL_QUADS

from CS100.Rendering import Shape
from CS100.Math.Vector import vec
from CS100.Rendering import Color
from CS100.Subsystems.Tree import Tree
from CS100.Rendering.Sprite import Sprite
from CS100.Rendering import RenderGroups
from CS100.Rendering.Renderer import Renderer
from CS100.Rendering.SceneGraph import SceneGraph
from CS100.Rendering.ScenePrimitive import ScenePrimitive
from CS100.Subsystems.Resources.Animation import Animation
from CS100.Subsystems.ResourceManager import ResourceManager
from CS100.Space.TransformationGraph import TransformationGraph


#-------------------------------------------------------#	


#	Set up Window/Rendering
window 			= pyglet.window.Window(800, 600)
winDimensions 	= [800, 600]

baseTree = Tree()
sceneGraph = SceneGraph.activeGraph = SceneGraph(baseTree)
transformGraph = TransformationGraph.activeGraph = TransformationGraph(baseTree)

renderer = Renderer(winDimensions, sceneGraph)


#	Set up Resources
rm = ResourceManager("data")
ResourceManager.activeManager = rm
rm.registerExtension(".jpg", "img", ["img"], pyglet.image.load)
rm.registerExtension(".bmp", "img", ["img"], pyglet.image.load)
rm.registerExtension(".png", "img", ["img"], pyglet.image.load)
rm.registerExtension(".anim", "anim", ["anim"], Animation)


#	Create Objects
sprite1 = Sprite(rm.request("CharizardEvolve.png"), sceneGraph.newNode())
sprite2 = Sprite(rm.request("CharizardEvolve.anim"), sceneGraph.newNode(t=vec(0, 200)))
sprite3 = Sprite(rm.request("PShip.anim"), sceneGraph.newNode(t=vec(0, -200)))

sprite2.getAnimation().setState("Looping")
sprite3.getAnimation().setState("Looping")

RenderGroups.Enable2DTexGroup.set_state()

#	Define Funcs

def update(dt):
	sprite1.update(dt)
	sprite2.update(dt)
	sprite3.update(dt)

@window.event
def on_draw():
	window.clear()
	renderer.render()


pyglet.clock.schedule(update)
pyglet.app.run()

