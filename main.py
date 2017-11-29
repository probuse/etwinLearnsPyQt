"shows how to work with main menu in PyQt"

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    "class to define a window"
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle("etwinz window")
        self.setWindowIcon(QtGui.QIcon("analytics.png"))

        # controls main menu item
        quitAction = QtGui.QAction("&Quit now!", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip("This closes the app")
        quitAction.triggered.connect(self.close_application)

        saveFileAction = QtGui.QAction("&Save File", self)
        saveFileAction.setShortcut("Ctrl+S")
        saveFileAction.setStatusTip("Saves file")
        saveFileAction.triggered.connect(self.save_file)

        # adding editor
        editorAction = QtGui.QAction("&Editing", self)
        editorAction.setShortcut("ctrl+E")
        editorAction.setStatusTip("open editor")
        editorAction.triggered.connect(self.editor)

        # opening a file
        openFileAction = QtGui.QAction("&Open File", self)
        openFileAction.setShortcut("Ctrl+O")
        openFileAction.setStatusTip("Opening a file")
        openFileAction.triggered.connect(self.open_file)

        # adding a setting action
        settingAction = QtGui.QAction("&Settings!!", self)
        settingAction.setShortcut("A")
        settingAction.setStatusTip("This is the settings button")

        self.statusBar()

        # controls main menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(quitAction)
        fileMenu.addAction(saveFileAction)
        fileMenu.addAction(openFileAction)

        settingMenu = mainMenu.addMenu("&Save")
        settingMenu.addAction(settingAction)

        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(editorAction)

        self.home()

    def home(self):
        "method to maniulate features on home window"
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(350, 200)

        # adding a toolBar
        # quittingAction
        quittingAction = QtGui.QAction(QtGui.QIcon("analytics.png"), "Quit Right now", self)
        quittingAction.triggered.connect(self.close_application)
        self.quittingToolBar = self.addToolBar("Quitting")
        self.quittingToolBar.addAction(quittingAction)

        # adding etwinAction
        etwinAction = QtGui.QAction(QtGui.QIcon("history.png"), "Hello etwin", self)
        etwinAction.triggered.connect(self.print_hello)
        self.etwinToolBar = self.addToolBar("Greetings")
        self.etwinToolBar.addAction(etwinAction)

        # fontChoice Action
        fontChoiceAction = QtGui.QAction("Font", self)
        fontChoiceAction.triggered.connect(self.font_choice)
        self.fontToolBar = self.addToolBar("Font")
        self.fontToolBar.addAction(fontChoiceAction)

        # adding a color picker
        color = QtGui.QColor(0, 0, 0)
        fontColorAction = QtGui.QAction("Font bg color", self)
        fontColorAction.triggered.connect(self.color_picker)
        self.fontColorBar = self.addToolBar("Color")
        self.fontColorBar.addAction(fontColorAction)

        # adding a calender widget
        calender = QtGui.QCalendarWidget(self)
        calender.move(500, 400)
        calender.resize(200, 200)   

        # adding a checkbox
        checkBox = QtGui.QCheckBox("Enlarge", self)
        checkBox.move(0, 200)
        checkBox.stateChanged.connect(self.enlarge_window)

        # adding a progress bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        # adding comboBox
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("etwin", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        self.styleChoice.move(50, 230)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def save_file(self):
        "saves a file to disk"
        name = QtGui.QFileDialog.getSaveFileName(self, "save File")
        my_file = open(name, 'w')
        text = self.textEdit.toPlainText()
        my_file.write(text)
        my_file.close()

    def open_file(self):
        "opens a file"
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        my_file = open(name, 'r')

        self.editor()

        with my_file:
            text = my_file.read()
            self.textEdit.setText(text)

    def editor(self):
        "renders an editor window"
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def color_picker(self):
        "selects a color"
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s }" % color.name())
    
    def font_choice(self):
        "selects a font"
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        "selects a style choice"
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        "mimics downloading"
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed) 

    def enlarge_window(self, state):
        "enlarges window size"
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 800)
        else:
            self.setGeometry(50, 50, 800, 500)

    def close_application(self):
        "closes window when button is pressed"
        choice = QtGui.QMessageBox.question(
            self, 
            "Quiting",
            "Are you sure you want to quit?",
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("We are supposed to quit")
            sys.exit()
        else:
            pass

    def print_hello(self):
        "prints hello nimar when button is pressed"
        print("Hello nimar")

def run():
    "main loop to run the application"
    app = QtGui.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
