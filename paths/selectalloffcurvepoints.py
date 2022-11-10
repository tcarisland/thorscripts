#MenuTitle: Select Off Curve Points
# -*- coding: utf-8 -*-

for p in Glyphs.font.selectedLayers[0].paths:
	for node in p.nodes:
		if node.type == OFFCURVE:
			node.selected = True
