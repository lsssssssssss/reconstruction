#
#  threshold tests
#

import reconstruction.CV2
reload( reconstruction.CV2)
createCV=reconstruction.CV2.createCV


if App.ActiveDocument==None:
	App.newDocument("Unnamed")
	App.setActiveDocument("Unnamed")
	App.ActiveDocument=App.getDocument("Unnamed")
	Gui.ActiveDocument=Gui.getDocument("Unnamed")




import reconstruction
fn=reconstruction.__path__[0] + "/../testdata/bn_990.png"

t=createCV('ImageFile')
t.sourceFile=fn
t.invert=True

t2=createCV('Morphing')
t2.sourceObject=t
t2.filter='dilation'
t2.kernel=12
FreeCAD.ActiveDocument.recompute()

t3=createCV('Skeleton',"Skeleton")
t3.sourceObject=t2
FreeCAD.ActiveDocument.recompute()

t4=createCV('Mixer')
t4.sourceObject=t2
t4.source2Object=t3
t4.inverse2=True
t4.zoom=False
FreeCAD.ActiveDocument.recompute()








for j in [t,t2,t3,t4]:
	try:
		App.activeDocument().recompute()
		j.ViewObject.Proxy.setEdit(j.ViewObject)
	except:
		App.activeDocument().recompute()