# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RemoteDebug
                                 A QGIS plugin
 Plugin to connect different IDE remote debugger
                              -------------------
        begin                : 2012-07-30
        copyright            : (C) 2012 by Dr. Horst Düster / Pirmin Kalberer /Sourcepole AG
        email                : horst.duester@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog

class RemoteDebug:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # Create the dialog and keep reference
#        self.dlg = RemoteDebugDialog()
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/remotedebug"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
       
        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/remotedebug_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
   

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/remotedebug/icon.png"), "Remote Debug", self.iface.mainWindow())
#        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.startDebugging)
#
#        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
#        self.iface.addPluginToMenu(u"&Remote Debug", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
#        self.iface.removePluginMenu(u"&Remote Debug",self.action)
       self.iface.removeToolBarIcon(self.action)

    def startDebugging(self):
        try:
           from dbg_client.DebugClient import DebugClient
           DBG=DebugClient()
           DBG.startDebugger(host= 'localhost',filename = '', port= 42424,exceptions=True, enableTrace=True ,redirect=True)
        except:
           pass
        
    def stopDebugging(self):
        pass        
    # run method that performs all the real work
    def run(self):
            pass