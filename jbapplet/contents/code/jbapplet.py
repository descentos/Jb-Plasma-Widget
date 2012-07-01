#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  JB main.py
#  
#  Copyright 2012 Brian Manderville <brian@descentos.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# I haven't tested this at all, so I don't know if it even works
# So test it and commit code fixes if you find issues, please!
#

import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsLinearLayout
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyQt4.QtWebkit import *


class JBApplet(plasmascript.Applet):
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self,parent)
		
	def init(self):
		self.setHasConfigurationInterface(True)
		self.setAspectRatioMode(Plasma.Rectangle)
		self.theme = Plasma.Svg(self)
		self.theme.setImagePath("widgets/background")
		self.setBackgroundHints(Plasma.Applet.DefaultBackground)
		
		self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
		label= Plasma.Label(self.applet)
		label.setText("Jupiter Broadcasting")
		self.layout.addItem(label)
		self.applet.setLayout(self.layout)
		self.resize(640, 480)

		app = QApplication(sys.argv)
		web = QWebView()
		web.load(QUrl("http://jb.cdn.scaleengine.net/jw/jwplayer.swf"))
		web.show()

	def CreateApplet(parent):
		return JBApplet(parent)
		
		
