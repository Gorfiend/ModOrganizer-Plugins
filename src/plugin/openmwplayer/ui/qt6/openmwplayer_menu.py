# Form implementation generated from reading ui file 'D:\Repos\ModOrganizer-Plugins\src\plugin\openmwplayer\ui\openmwplayer_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OMWPMenu(object):
    def setupUi(self, OMWPMenu):
        OMWPMenu.setObjectName("OMWPMenu")
        OMWPMenu.resize(600, 400)
        OMWPMenu.setMinimumSize(QtCore.QSize(600, 400))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(OMWPMenu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentSplitter = QtWidgets.QSplitter(parent=OMWPMenu)
        self.contentSplitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.contentSplitter.setObjectName("contentSplitter")
        self.tabList = QtWidgets.QTabWidget(parent=self.contentSplitter)
        self.tabList.setObjectName("tabList")
        self.optionsTab = QtWidgets.QWidget()
        self.optionsTab.setObjectName("optionsTab")
        self.tabList.addTab(self.optionsTab, "")
        self.archivesTab = QtWidgets.QWidget()
        self.archivesTab.setObjectName("archivesTab")
        self.tabList.addTab(self.archivesTab, "")
        self.groundcoverTab = QtWidgets.QWidget()
        self.groundcoverTab.setObjectName("groundcoverTab")
        self.tabList.addTab(self.groundcoverTab, "")
        self.openmwcfgTab = QtWidgets.QWidget()
        self.openmwcfgTab.setObjectName("openmwcfgTab")
        self.tabList.addTab(self.openmwcfgTab, "")
        self.settingscfgTab = QtWidgets.QWidget()
        self.settingscfgTab.setObjectName("settingscfgTab")
        self.tabList.addTab(self.settingscfgTab, "")
        self.updateTab = QtWidgets.QWidget()
        self.updateTab.setObjectName("updateTab")
        self.tabList.addTab(self.updateTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.tabList.addTab(self.helpTab, "")
        self.verticalLayout_2.addWidget(self.contentSplitter)

        self.retranslateUi(OMWPMenu)
        self.tabList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OMWPMenu)

    def retranslateUi(self, OMWPMenu):
        _translate = QtCore.QCoreApplication.translate
        OMWPMenu.setWindowTitle(_translate("OMWPMenu", "Form"))
        self.tabList.setTabText(self.tabList.indexOf(self.optionsTab), _translate("OMWPMenu", "Options"))
        self.tabList.setTabText(self.tabList.indexOf(self.archivesTab), _translate("OMWPMenu", "Archives"))
        self.tabList.setTabText(self.tabList.indexOf(self.groundcoverTab), _translate("OMWPMenu", "Groundcover"))
        self.tabList.setTabText(self.tabList.indexOf(self.openmwcfgTab), _translate("OMWPMenu", "OpenMW.cfg"))
        self.tabList.setTabText(self.tabList.indexOf(self.settingscfgTab), _translate("OMWPMenu", "Settings.cfg"))
        self.tabList.setTabText(self.tabList.indexOf(self.updateTab), _translate("OMWPMenu", "Update"))
        self.tabList.setTabText(self.tabList.indexOf(self.helpTab), _translate("OMWPMenu", "Help"))
