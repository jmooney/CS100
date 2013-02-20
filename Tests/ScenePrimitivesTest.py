
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

'''		Set Search Directory	'''
for root, direcs, files in os.walk(os.getcwd()):
	for direc in direcs:
		sys.path.append(os.path.join(root, direc))


# Local Imports
import TransformationGraph
import DebugDrawingManager
import ScenePrimitives
import Color

from Vector import vec

#-------------------------------------------------------#
	

window 	= pyglet.window.Window()
tg 		= TransformationGraph.tg = TransformationGraph.TransformationGraph()
ddm 	= DebugDrawingManager.ddm = DebugDrawingManager.DebugDrawingManager()


t1 = tg.newTransform(t=vec(100, 150))
t2 = t1.createChildNode(t=vec(200, 0))
t3 = t2.createChildNode(t=vec(200, 0))

c1 = Color.Red
c2 = Color.Green
c3 = Color.Blue

sr = ScenePrimitives.SceneRect
rs = [sr(t=t1, w=100, h=100, c=c1), sr(t=t2, w=100, h=100, c=c2), sr(t=t3, w=100, h=100, c=c3)]
	
sra = ScenePrimitives.SceneRay
ras = [sra(t=t1, d=vec(1.0, 1.0), l=100, c=c1), sra(t=t2, d=vec(-1.0, 1.0), l=100, c=c2), sra(t=t3, d=vec(1.0, -1.0), l=100, c=c3)]

se = ScenePrimitives.SceneEllipse
ses = [se(t=t1, a=50, b=100, c=c1), se(t=t2, a=50, b=100, c=c2), se(t=t3, a=50, b=100, c=c3)]
sf		= 1.001
sDif	= .001

tDif 	= .01
direc 	= vec(0, 0.01)

theList = ses

def update(dt):
	ddm.update(dt)
	
	global sf, tDif, direc, sDif
	for item in theList:
		item.update(dt)
		
	theList[0].translate(direc)
	theList[1].rotate(.01)
	theList[2].scale(sf)

	DebugDrawingManager.ddm.drawEllipse(vec(100, 100), 20, 30, c=Color.Purple) 
	
	if(abs(direc.y) > 1.0):
		tDif = -tDif
	if(abs(1.0 - theList[2]._worldScale) > 0.5):
		sDif = -sDif
	
	sf = 1 + sDif
	direc.y += tDif


@window.event
def on_draw():
	window.clear()
	for item in theList:
		item.draw()
		
	ddm.draw()
	

pyglet.clock.schedule(update)
pyglet.app.run()
