import sys
from PyQt6 import QtWidgets, uic
from itertools import count

from MainWindowC import Ui_Form
from DialogWindow import Ui_Form as Ui_Form_dialog
import Algorithm as al
import Data_prep

class DialogWindow(QtWidgets.QDialog, Ui_Form_dialog):

    def __init__(self, *args, obj=None, **kwargs):
        super(DialogWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class MainWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButtonClicked)

    def setLabels(self):

        self.PopWindow.label_4.setText(self.res[0][30])
        self.PopWindow.label_5.setText(self.res[1][30])
        self.PopWindow.label_6.setText(self.res[2][30])
        self.PopWindow.label_8.setText(self.res[3][30])
        self.PopWindow.label_10.setText(self.res[4][30])

        self.PopWindow.label_2.setText(self.res[0][31])
        self.PopWindow.label_3.setText(self.res[1][31])
        self.PopWindow.label_7.setText(self.res[2][31])
        self.PopWindow.label_9.setText(self.res[3][31])
        self.PopWindow.label_11.setText(self.res[4][31])

    def pushButtonClicked(self):

        self.content_table = []
        self.comboBoxes = [self.comboBox,self.comboBox_2,self.comboBox_3,
                           self.comboBox_4,self.comboBox_5,self.comboBox_6,self.comboBox_7,
                           self.comboBox_8]
        self.checkBoxes = [self.checkBox,self.checkBox_2,self.checkBox_3,self.checkBox_4,self.checkBox_5,
                           self.checkBox_6,self.checkBox_7,self.checkBox_8]
        for key in range(0,8):
            if(self.checkBoxes[key].isChecked()):
                self.content_table.append(self.comboBoxes[key].currentText())
                print(self.comboBoxes[key].currentText())

        self.res = al.reasult(data,data_for,self.content_table)
        self.PopWindow = DialogWindow()
        self.PopWindow.setModal(True)
        self.setLabels()
        self.PopWindow.show()
        self.PopWindow.exec()

data,data_for = Data_prep.Data_prep()
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
