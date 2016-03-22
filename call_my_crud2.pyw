#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Paul Louie L. Tito

import sip
sip.setapi('QVariant',2) #we need to include the sip module to support Python 2; otherwise, we need to use Python 3

import sys
from my_crud2 import Ui_MainWindow #import main class from my_crud.py
from crud_students_2 import Ui_Dialog #import main class from crud_students_2.py
from PyQt4 import QtSql, QtGui, QtCore #import all necessary modules

#set the database connection
def createConnection():
	db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
	db.setHostName('localhost') #enter host name here enclosed in single quotes
	db.setDatabaseName('db_student_info') #enter the name of the database enclosed in single quotes
	db.setUserName('root') #enter the username for the exclusive account you created in Part 1 enclosed in single quotes
	db.setPassword('') #enter password for the exclusive account enclosed in single quotes
	db.open()
	print (db.lastError().text())
	return True

#create main class
class MyCrud(QtGui.QMainWindow):
	recno = 0
	def __init__(self, parent=None):
		super(MyCrud, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)		
		self.model=QtSql.QSqlQueryModel(self)		
		
		self.model.setQuery("select * from tbl_student_info") #complete this query. select all from the tbl_students table
		self.record=self.model.record(0)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtYear.setText (str(self.record.value("year")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtSection.setText(self.record.value("section"))
		
		
		
		
		self.model = QtSql.QSqlTableModel(self)
		self.model.setTable("tbl_student_info")	
		self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.model.select()
		
		#Configure Signals and Slots
		QtCore.QObject.connect(self.ui.actionSearch, QtCore.SIGNAL('triggered()'),self.MyFormShow)
		QtCore.QObject.connect(self.ui.btnFirst, QtCore.SIGNAL('clicked()'),self.dispFirst)
		QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL('clicked()'),self.dispPrevious)
		QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL('clicked()' ),self.dispLast)
		QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL('clicked()' ),self.dispNext)
		QtCorqe.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL('clicked()' ),self.EnableLineEdits)
		QtCore.QObject.connect(self.ui.actionExit_2, QtCore.SIGNAL("triggered()"),self.close)
		QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()' ),self.close)
		QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL('clicked()' ),self.AddRecord)
		QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL('clicked()' ),self.AlertBoxAddRecord)
		QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL('clicked()' ),self.UpdateRecord)
		QtCore.QObject.connect(self.ui.pushButton_8, QtCore.SIGNAL('clicked()' ),self.AlertBoxUpdateRecord)
		QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL('clicked()' ),self.EditRecords)
		QtCore.QObject.connect(self.ui.pushButton_9, QtCore.SIGNAL('clicked()' ),self.AlertBoxDeleteRecord)
	
	#call the search form			
	def MyFormShow(self):
		MyFormShowWindow = FormSearch(self)
		MyFormShowWindow.show()
	
	def EnableLineEdits(self):
		self.ui.txtId.setEnabled(True)
		self.ui.txtFirstName.setEnabled(True)
		self.ui.txtLastName.setEnabled(True)
		self.ui.txtCourse.setEnabled(True)
		self.ui.txtYear.setEnabled(True)
		self.ui.txtSection.setEnabled(True)

	def dispFirst(self):
		MyCrud.recno=0
		self.record=self.model.record(MyCrud.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtYear.setText (str(self.record.value("year")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtSection.setText(self.record.value("section"))
							
	def dispPrevious(self):
		MyCrud.recno-=1
		if MyCrud.recno < 0:
			MyCrud.recno=self.model.rowCount()-1
		self.record=self.model.record(MyCrud.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtYear.setText (str(self.record.value("year")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtSection.setText(self.record.value("section"))

	def dispLast(self):
		MyCrud.recno=self.model.rowCount()-1
		self.record=self.model.record(MyCrud.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtYear.setText (str(self.record.value("year")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtSection.setText(self.record.value("section"))
			
	def dispNext(self):
		MyCrud.recno+=1
		if MyCrud.recno > self.model.rowCount()-1:
			MyCrud.recno=0
		self.record=self.model.record(MyCrud.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtYear.setText (str(self.record.value("year")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtSection.setText(self.record.value("section"))
		
		
	def AddRecord(self):
		studentId = self.ui.txtId.text()
		studentFName = self.ui.txtFirstName.text()
		studentLName = self.ui.txtLastName.text()
		studentCourse = self.ui.txtCourse.text()
		studentYear = self.ui.txtYear.text()
		studentSection = self.ui.txtSectiontext()
			
		self.model.setData(self.model.index(0, 1), studentId)
		self.model.setData(self.model.index(0, 2), studentFName)
		self.model.setData(self.model.index(0, 3), studentLName)
										
	def UpdateRecord(self):
		self.model.submitAll()
	
	def EditRecords(self):
		self.model.insertRows(0,1)

	#research for this delete function. Hint: http://pyqt.sourceforge.net/Docs/PyQt4/qtsql.html#inserting-updating-and-deleting-records
	#def DeleteRecord(self):

		
	def SearchRecord(self):
		self.model.setFilter("fname like '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("lname like '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("student_id like '"+self.ui.txtSearch.text()+"%'")
		
	def CancelChanges(self):
		self.model.revertAll()
		
	def AlertBoxAddRecord(self):       
		#The QWidget widget is the base class of all user interface objects in PyQt4.
		msgBox = QtGui.QWidget(self)
		#Show a message box
		res = QtGui.QMessageBox.information(msgBox, "Message", "new record successfully added!")
		msgBox.show()

	def AlertBoxUpdateRecord(self):       
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, "Message", "new record saved!")
		msgBox.show()
	
	def AlertBoxDeleteRecord(self):
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.question(msgBox, 'Message', "Are you sure you want to continue?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		msgBox.show()

#we include this class so we can call the form generated by crud_students_2.ui		
class FormSearch(QtGui.QDialog):
	def __init__(self, parent=None):
		super(FormSearch, self).__init__(parent)
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)	
		self.model = QtSql.QSqlTableModel(self)		
		self.model.setTable("tbl_student_info")		
		self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.model.removeColumn(0) #this code removes the tbl_id field from showing
		self.model.select()
		
		#set column name of table upon display
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID NUMBER")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "FIRST NAME")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "LAST NAME")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "COURSE")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "YEAR")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "SECTION")
		
		#set the table view "tblSearch" as model
		self.ui.tblSearch.setModel(self.model)		
		QtCore.QObject.connect(self.ui.btnSearch, QtCore.SIGNAL('clicked()' ),self.SearchRecord)
	
	#Try to improve this code by also searching for the other fields aside from student_id	
	def SearchRecord(self):
		self.model.setFilter("student_id like '"+self.ui.txtSearch.text()+"%'")
	
	#Room for improvement: You can try and apply this upon "NO" Option in message boxes		
	#def CancelChanges(self):
		#self.model.revertAll()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

if not createConnection():
	sys.exit(1)

myapp = MyCrud()
myapp.show()
sys.exit(app.exec_())


