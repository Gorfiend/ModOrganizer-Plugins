# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\src2\plugin\rootbuilder\ui\rootbuilder_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsTabWidget(object):
    def setupUi(self, settingsTabWidget):
        settingsTabWidget.setObjectName("settingsTabWidget")
        settingsTabWidget.resize(620, 420)
        settingsTabWidget.setMinimumSize(QtCore.QSize(620, 420))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(settingsTabWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cacheWidget = QtWidgets.QWidget(settingsTabWidget)
        self.cacheWidget.setObjectName("cacheWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cacheWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cacheCheck = QtWidgets.QCheckBox(self.cacheWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cacheCheck.setFont(font)
        self.cacheCheck.setObjectName("cacheCheck")
        self.verticalLayout_2.addWidget(self.cacheCheck)
        self.cacheLabel = QtWidgets.QLabel(self.cacheWidget)
        self.cacheLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cacheLabel.setWordWrap(True)
        self.cacheLabel.setObjectName("cacheLabel")
        self.verticalLayout_2.addWidget(self.cacheLabel)
        self.verticalLayout_7.addWidget(self.cacheWidget)
        self.backupWidget = QtWidgets.QWidget(settingsTabWidget)
        self.backupWidget.setObjectName("backupWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.backupWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backupCheck = QtWidgets.QCheckBox(self.backupWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backupCheck.setFont(font)
        self.backupCheck.setObjectName("backupCheck")
        self.verticalLayout.addWidget(self.backupCheck)
        self.backupLabel = QtWidgets.QLabel(self.backupWidget)
        self.backupLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.backupLabel.setWordWrap(True)
        self.backupLabel.setObjectName("backupLabel")
        self.verticalLayout.addWidget(self.backupLabel)
        self.verticalLayout_7.addWidget(self.backupWidget)
        self.autobuildWidget = QtWidgets.QWidget(settingsTabWidget)
        self.autobuildWidget.setObjectName("autobuildWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.autobuildWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.autobuildCheck = QtWidgets.QCheckBox(self.autobuildWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.autobuildCheck.setFont(font)
        self.autobuildCheck.setObjectName("autobuildCheck")
        self.verticalLayout_4.addWidget(self.autobuildCheck)
        self.autobuildLabel = QtWidgets.QLabel(self.autobuildWidget)
        self.autobuildLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.autobuildLabel.setWordWrap(True)
        self.autobuildLabel.setObjectName("autobuildLabel")
        self.verticalLayout_4.addWidget(self.autobuildLabel)
        self.verticalLayout_7.addWidget(self.autobuildWidget)
        self.redirectWidget = QtWidgets.QWidget(settingsTabWidget)
        self.redirectWidget.setObjectName("redirectWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.redirectWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.redirectCheck = QtWidgets.QCheckBox(self.redirectWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.redirectCheck.setFont(font)
        self.redirectCheck.setObjectName("redirectCheck")
        self.verticalLayout_3.addWidget(self.redirectCheck)
        self.redirectLabel = QtWidgets.QLabel(self.redirectWidget)
        self.redirectLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.redirectLabel.setWordWrap(True)
        self.redirectLabel.setObjectName("redirectLabel")
        self.verticalLayout_3.addWidget(self.redirectLabel)
        self.verticalLayout_7.addWidget(self.redirectWidget)
        self.installerWidget = QtWidgets.QWidget(settingsTabWidget)
        self.installerWidget.setObjectName("installerWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.installerWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.installerCheck = QtWidgets.QCheckBox(self.installerWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.installerCheck.setFont(font)
        self.installerCheck.setObjectName("installerCheck")
        self.verticalLayout_6.addWidget(self.installerCheck)
        self.installerLabel = QtWidgets.QLabel(self.installerWidget)
        self.installerLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.installerLabel.setWordWrap(True)
        self.installerLabel.setObjectName("installerLabel")
        self.verticalLayout_6.addWidget(self.installerLabel)
        self.verticalLayout_7.addWidget(self.installerWidget)
        self.debugWidget = QtWidgets.QWidget(settingsTabWidget)
        self.debugWidget.setObjectName("debugWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.debugWidget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.debugLevelWidget = QtWidgets.QWidget(self.debugWidget)
        self.debugLevelWidget.setMinimumSize(QtCore.QSize(0, 20))
        self.debugLevelWidget.setMaximumSize(QtCore.QSize(16777215, 20))
        self.debugLevelWidget.setObjectName("debugLevelWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.debugLevelWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.debugTitle = QtWidgets.QLabel(self.debugLevelWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.debugTitle.setFont(font)
        self.debugTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.debugTitle.setWordWrap(False)
        self.debugTitle.setObjectName("debugTitle")
        self.horizontalLayout.addWidget(self.debugTitle)
        self.debugLevelCombo = QtWidgets.QComboBox(self.debugLevelWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugLevelCombo.sizePolicy().hasHeightForWidth())
        self.debugLevelCombo.setSizePolicy(sizePolicy)
        self.debugLevelCombo.setObjectName("debugLevelCombo")
        self.debugLevelCombo.addItem("")
        self.debugLevelCombo.addItem("")
        self.debugLevelCombo.addItem("")
        self.debugLevelCombo.addItem("")
        self.horizontalLayout.addWidget(self.debugLevelCombo)
        self.verticalLayout_5.addWidget(self.debugLevelWidget)
        self.debugLabel = QtWidgets.QLabel(self.debugWidget)
        self.debugLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.debugLabel.setWordWrap(True)
        self.debugLabel.setObjectName("debugLabel")
        self.verticalLayout_5.addWidget(self.debugLabel)
        self.verticalLayout_7.addWidget(self.debugWidget)

        self.retranslateUi(settingsTabWidget)
        QtCore.QMetaObject.connectSlotsByName(settingsTabWidget)

    def retranslateUi(self, settingsTabWidget):
        _translate = QtCore.QCoreApplication.translate
        settingsTabWidget.setWindowTitle(_translate("settingsTabWidget", "Form"))
        self.cacheCheck.setText(_translate("settingsTabWidget", "Cache"))
        self.cacheLabel.setText(_translate("settingsTabWidget", "If cache is enabled, all file hashes for base game files (excluding the data files) are stored and reused during all future builds. The hashes are used to determine if a file has changed. If cache is disabled, changes to base game files cannot be detected."))
        self.backupCheck.setText(_translate("settingsTabWidget", "Backup"))
        self.backupLabel.setText(_translate("settingsTabWidget", "If backup is enabled, a full backup of the base game files (excluding the data files) is taken. This is used to restore any changes to the base game during a clear. If backup is disabled, only files that are about to be overwritten will be backed up."))
        self.autobuildCheck.setText(_translate("settingsTabWidget", "Autobuild"))
        self.autobuildLabel.setText(_translate("settingsTabWidget", "If autobuild is enabled, when an application is launched through Mod Organizer, a build will run. When that application closes (or Mod Organizer is unlocked), a clear will run."))
        self.redirectCheck.setText(_translate("settingsTabWidget", "Redirect"))
        self.redirectLabel.setText(_translate("settingsTabWidget", "If redirect is enabled, when an application is launched through Mod Organizer, if that application is in a valid Root folder, Mod Organizer will instead launch it from its location in the game folder."))
        self.installerCheck.setText(_translate("settingsTabWidget", "Installer"))
        self.installerLabel.setText(_translate("settingsTabWidget", "If installer is enabled, when a mod is installed through Mod Organizer, it will attempt to detect if that mod is a Root mod and repackage it to work with Root Builder. This may incorrectly install some mods."))
        self.debugTitle.setText(_translate("settingsTabWidget", "Debug"))
        self.debugLevelCombo.setItemText(0, _translate("settingsTabWidget", "Debug"))
        self.debugLevelCombo.setItemText(1, _translate("settingsTabWidget", "Info"))
        self.debugLevelCombo.setItemText(2, _translate("settingsTabWidget", "Warning"))
        self.debugLevelCombo.setItemText(3, _translate("settingsTabWidget", "Critical"))
        self.debugLabel.setText(_translate("settingsTabWidget", "Select the level of logging you want Root Builder to produce. This will have no effect unless Mod Organizer\'s log level would also show this level of logging."))
