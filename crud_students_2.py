# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crud_students_2.ui'
#
# Created: Fri Mar 18 13:13:57 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(532, 135)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.txtSearch = QtGui.QLineEdit(Dialog)
        self.txtSearch.setObjectName(_fromUtf8("txtSearch"))
        self.horizontalLayout.addWidget(self.txtSearch)
        self.btnSearch = QtGui.QPushButton(Dialog)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.horizontalLayout.addWidget(self.btnSearch)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.tblSearch = QtGui.QTableView(Dialog)
        self.tblSearch.setObjectName(_fromUtf8("tblSearch"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.tblSearch)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "ID number:", None))
        self.btnSearch.setText(_translate("Dialog", "Search", None))

