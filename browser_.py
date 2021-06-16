import sys
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http:/google.com'))
        self.setCentralWidget(self.browser)       
        self.showMaximized()
        
        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back_button
        Back_button = QAction('Back',self)
        Back_button.triggered.connect(self.browser.back)
        navbar.addAction(Back_button)

        # Forward_button
        Forward_button = QAction('Forward',self)
        Forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(Forward_button)

    #     # Relaod_button
        Reload_button = QAction('Relaod',self)
        Reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_button)

    #     # Home_button
        Home_button = QAction('Home',self)
        Home_button.triggered.connect(self.navigate_bar)
        navbar.addAction(Home_button)

        self.Url_bar = QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_Url)
        navbar.addWidget(self.Url_bar)


        self.browser.urlChanged.connect(self.update_Url)

    def navigate_bar(self):
        self.browser.setUrl(QUrl('http://github.com'))

    def navigate_to_Url(self):
        Url = self.Url_bar.text()
        self.browser.setUrl(QUrl(Url))

    def update_Url(self,q):
        self.Url_bar.setText(q.toString())


        
app = QApplication(sys.argv)
QApplication.setApplicationName("Farukh-Hub")
window = MainWindow()
app.exec_()


