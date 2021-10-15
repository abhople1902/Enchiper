import sys
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowIcon(QtGui.QIcon('IMG\www.png'))
        self.setGeometry(200,150,1500,800)

        #Tab Bar
        self.TabBar = QTabWidget() 
        self.setCentralWidget(self.TabBar)

        #Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        BackBtn = QAction("←",self)
        BackBtn.triggered.connect(lambda:self.TabBar.currentWidget().back())
        BackBtn.setStatusTip("Go Back...")
        navbar.addAction(BackBtn)

        FwdBtn = QAction("→",self)
        FwdBtn.triggered.connect(lambda:self.TabBar.currentWidget().forward())
        FwdBtn.setStatusTip("Go Forward...")
        navbar.addAction(FwdBtn)


        #URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setStatusTip("Enter url...")
        
        # Creating First tab---------
        self.Add_New_Tab(QUrl('http://www.google.com'), 'New Tab')
        self.show()
        # Creating First tab---------

   
    # Add New Tab
    def Add_New_Tab(self,qurl = None,label = "New Tab"):
        if qurl == None:
            qurl = 'http://www.google.com'

        browser = QWebEngineView()
        browser.setUrl(QUrl('http://127.0.0.1:5000'))

        i = self.TabBar.addTab(browser, label) 
        self.TabBar.setCurrentIndex(i)
        browser.urlChanged.connect(lambda browser=browser:self.url_update(browser))
        browser.loadProgress.connect(lambda _, i = i ,browser = browser:self.TabBar.setTabText(i,browser.page().title()))
        browser.loadStarted.connect(self.LoadingStrt)
        browser.loadFinished.connect(self.LoadingFin)
    
    #Loding Color Start
    def LoadingStrt(self):
        self.statusBar().setStyleSheet("background-color : blue")

    #Loding Color End
    def LoadingFin(self):
        self.statusBar().setStyleSheet("background-color : white")

    # Open Tab //Double click
    def Open_New_Tab(self,i):
        if i == -1: 
            self.Add_New_Tab("New Tab") 
        
    # Change Tab
    def Change_Tab(self,i):
        qurl = self.TabBar.currentWidget().url()
        self.url_update(qurl)

 
  

    def navigate_to_url(self):
        url = self.url_bar.text()
        print(len(url))
        if url == "":
            self.TabBar.currentWidget().setUrl(QUrl(f"http://pyycoders.unaux.com/"))
        elif (url.endswith(".com")  or url.endswith(".com/") or "www." in url):
            self.TabBar.currentWidget().setUrl(QUrl(url))
      
        else:
            self.TabBar.currentWidget().setUrl(QUrl(f"http://{url}.com/"))
    
    def url_update(self,q):
        self.url_bar.setText(q.toString())

 

app = QApplication(sys.argv)
QApplication.setApplicationName('WellEazy - Your Personal Health Assistant')
window = MainWindow()
    
app.exec_() 
   