from PyQt5.QtGui import*
from texteditorKel3Gui import*


def additionalUi(self):
    self.label.setWordWrap(True) 
    self.label.setAutoFillBackground(True)
    self.textEdit.setText(self.label.text())
    self.fontComboBox.setFontFilters(self.fontComboBox.AllFonts)
    self.fontComboBox.lineEdit().setReadOnly(True)
    self.horizontalSlider_1.setTickPosition(self.horizontalSlider_1.TicksAbove) 
    self.horizontalSlider_1.setRange(8, 32) 
    self.horizontalSlider_1.setSingleStep(2)
    self.horizontalSlider_1.setTickInterval(2)
    self.horizontalSlider_1.setValue(12)
    self.spinBox_1.setRange(8, 32) 
    self.spinBox_1.setSingleStep(2)
    self.spinBox_1.setValue(12)
    self.horizontalSlider_2.setRange(0, 255) 
    self.horizontalSlider_2.setValue(0)
    self.spinBox_2.setRange(0, 255) 
    self.spinBox_2.setValue(0)
    self.horizontalSlider_3.setRange(0, 255) 
    self.horizontalSlider_3.setValue(0)
    self.spinBox_3.setRange(0, 255) 
    self.spinBox_3.setValue(0)
    self.horizontalSlider_4.setRange(0, 255) 
    self.horizontalSlider_4.setValue(0)
    self.spinBox_4.setRange(0, 255) 
    self.spinBox_4.setValue(0)
    
def signals(self):
    self.textEdit.textChanged.connect(self.textChanged)
    
    self.fontComboBox.currentFontChanged.connect(self.fontChanged) 
    self.spinBox_1.valueChanged.connect(lambda i: self.fontChanged("spin-box"))
    self.horizontalSlider_1.valueChanged.connect(lambda i: self.fontChanged("slider"))
    
    self.checkBox_1.stateChanged.connect(lambda i: self.modifierChanged("skip", ""))
    self.checkBox_2.stateChanged.connect(lambda i: self.modifierChanged("skip", ""))
    self.checkBox_3.stateChanged.connect(lambda i: self.modifierChanged("skip", ""))
    self.checkBox_4.stateChanged.connect(lambda i: self.modifierChanged("skip", ""))
    
    self.spinBox_2.valueChanged.connect(lambda i: self.modifierChanged("spin-box", "red"))
    self.spinBox_3.valueChanged.connect(lambda i: self.modifierChanged("spin-box", "green"))
    self.spinBox_4.valueChanged.connect(lambda i: self.modifierChanged("spin-box", "blue"))
    self.horizontalSlider_2.valueChanged.connect(lambda i: self.modifierChanged("slider", "red"))
    self.horizontalSlider_3.valueChanged.connect(lambda i: self.modifierChanged("slider", "green"))
    self.horizontalSlider_4.valueChanged.connect(lambda i: self.modifierChanged("slider", "blue"))
    print("setup signals done")
    
def textChanged(self):
    self.label.setText(self.textEdit.toPlainText()) 
    
def fontChanged(self, eventTrigger):
    if eventTrigger == "spin-box": 
        self.horizontalSlider_1.setValue(self.spinBox_1.value())
    elif eventTrigger == "slider":
        self.spinBox_1.setValue(self.horizontalSlider_1.value())
    self.label.setFont(QFont(self.fontComboBox.currentText(), self.spinBox_1.value()))
        
def modifierChanged(self, eventTrigger, colour):
    styleSheets = [] 
    styleSheetsConcate = ""

    if self.checkBox_1.checkState(): 
        styleSheets.append("font-weight: bold")
    if self.checkBox_2.checkState():
        styleSheets.append("font-style: italic")
    if self.checkBox_3.checkState():
        styleSheets.append("text-decoration: underline")
    if self.checkBox_4.checkState():
        styleSheets.append("text-decoration: line-through")

    color  = QtGui.QColor(self.horizontalSlider_2.value(), self.horizontalSlider_3.value(), self.horizontalSlider_4.value())
    alpha  = 255
    values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
    styleSheets.append("color: rgba(" + values + ")")
    
    if eventTrigger != "skip" or colour == "": 
        if eventTrigger == "spin-box" and colour == "red": 
            self.horizontalSlider_2.setValue(self.spinBox_2.value())
        elif eventTrigger == "slider" and colour == "red":
            self.spinBox_2.setValue(self.horizontalSlider_2.value())             
        elif eventTrigger == "spin-box" and colour == "green": 
            self.horizontalSlider_3.setValue(self.spinBox_3.value())
        elif eventTrigger == "slider" and colour == "green":
            self.spinBox_3.setValue(self.horizontalSlider_3.value())  
        elif eventTrigger == "spin-box" and colour == "blue": 
            self.horizontalSlider_4.setValue(self.spinBox_4.value())
        elif eventTrigger == "slider" and colour == "blue":
            self.spinBox_4.setValue(self.horizontalSlider_4.value())  
        
    for x in styleSheets: 
        styleSheetsConcate = styleSheetsConcate + x + ";"

    styleSheetsConcate = "*{" + styleSheetsConcate + "}"
    self.label.setStyleSheet(styleSheetsConcate)


Ui_MainWindow.additionalUi = additionalUi
Ui_MainWindow.signals = signals
Ui_MainWindow.textChanged = textChanged
Ui_MainWindow.fontChanged = fontChanged
Ui_MainWindow.modifierChanged = modifierChanged



if __name__ == "__main__":              
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)
    ui.additionalUi()
    ui.signals()
    MainWindow.show() 
    sys.exit(app.exec_()) 