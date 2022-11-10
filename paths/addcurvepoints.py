#MenuTitle: Add Curve Points
# -*- coding: utf-8 -*-
from Foundation import NSPoint

def lerp(t, a, b):
	return NSPoint(int((1-t)*a.x + t*b.x), int((1-t)*a.y + t*b.y))

for p in Glyphs.font.selectedLayers[0].selection[0].paths:
	for idx in range(len(p.nodes) -1, 0, -1):
		node = p.nodes[idx]
		if node.type == LINE:
			prevNode = p.nodes[idx - 1]
			off1 = GSNode(lerp(0.33, prevNode.position, node.position), OFFCURVE)
			off2 = GSNode(lerp(0.66, prevNode.position, node.position), OFFCURVE)
			p.nodes.insert(idx, off2)
			p.nodes.insert(idx, off1)
			node.type = CURVE
			node.connection = GSSMOOTH
