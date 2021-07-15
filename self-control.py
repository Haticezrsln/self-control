import time
from datetime import datetime 
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

filename = datetime.now()
s=time.strftime('%X')
t=time.strftime('%x')
baslangic =  time.strftime('%X')

with open(filename.strftime('%d %B %Y')+".txt","a+") as file:
    file.write("********* YAPILACAK İŞLER ***********\n \t        {0}\n".format(s))  

class first_GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.textbox = QLineEdit(self)
        self.textbox.move(30, 60)
        self.textbox.resize(350,40)
        

        self.label_text = QLabel("Planların ne?:")
        self.label_text.setAlignment(Qt.AlignHCenter)
        self.label_text.setStyleSheet("color: rgb(0,0,0);font-weight: bold; font-size: 13pt")

        pushButton_show7 = QPushButton("Tekrar Giriş")
        pushButton_show7.setMinimumHeight(40)
        pushButton_show7.setStyleSheet("font-weight: bold; font-size: 16pt")
        pushButton_show7.clicked.connect(self.dosyayaYaz)      
        pushButton_show7.clicked.connect(self.dongu1)
        pushButton_show7.clicked.connect(self.close)

        pushButton_show = QPushButton("Kaydet")
        pushButton_show.setMinimumHeight(40)
        pushButton_show.setStyleSheet("font-weight: bold; font-size: 16pt")      
        pushButton_show.clicked.connect(self.dosyayaYaz)
        pushButton_show.clicked.connect(self.gorev)
        pushButton_show.clicked.connect(self.secondPage)
        pushButton_show.clicked.connect(self.close)

        

        pushButton_show2 = QPushButton("Eski Veriler")
        pushButton_show2.setMinimumHeight(40)
        pushButton_show2.setStyleSheet("font-weight: bold; font-size: 16pt")      
        pushButton_show2.clicked.connect(self.eskiveriler)
        

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_text)
        vertical_layout.addWidget(pushButton_show7)
        vertical_layout.addWidget(pushButton_show)
        vertical_layout.addWidget(pushButton_show2)
        

        self.setLayout(vertical_layout)
        self.setWindowTitle("Nasıl Gidiyor")
        self.resize(400,300)

    def dongu1(self):
        self.secondWindo = first_GUI()
        self.secondWindo.show()


    def dosyayaYaz(self):
        with open(filename.strftime('%d %B %Y')+".txt","a+") as file:
            file.write("   >> {0}\n".format(self.textbox.text()))
            


    def secondPage(self):                       
        self.secondWindow = SecondPage()
        self.secondWindow.show()

    def eskiveriler(self):                       
        self.secondWindow1 = Eskiveriler()
        self.secondWindow1.show()

    def gorev(self):
        with open(filename.strftime('%d %B %Y')+".txt","a+") as file:
            file.write("********** YAPILAN İŞLER ***********\n")  

class Eskiveriler(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.veri = QLineEdit(self)
        self.veri.move(40, 60)
        self.veri.resize(310,40)

        self.label_text2 = QLabel("Aradığınız Tarih?:")
        self.label_text2.setAlignment(Qt.AlignHCenter)
        self.label_text2.setStyleSheet("color: rgb(0,0,0);font-weight: bold; font-size: 13pt")

        pushButton_show3 = QPushButton("Ara")
        pushButton_show3.setMinimumHeight(40)
        pushButton_show3.setStyleSheet("font-weight: bold; font-size: 16pt")      
        pushButton_show3.clicked.connect(self.tarih)
        pushButton_show3.clicked.connect(self.close)


        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_text2)
        vertical_layout.addWidget(pushButton_show3)

        self.setLayout(vertical_layout)
        self.setWindowTitle("Nasıl Gidiyor")
        self.resize(400,200)

    def tarih(self):
        with open("{}.txt".format(self.veri.text()), "r+") as file:
            print (file.read())

     

class SecondPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        time.sleep(2)#saniye şeklinde zaman ayarlayabilrisiniz.#
        self.yazi = QLineEdit(self)  
        self.yazi.move(60, 70)
        self.yazi.resize(310,40)

        self.label_text1 = QLabel("Neler Yapıyorsun?")
        self.label_text1.setAlignment(Qt.AlignHCenter)
        self.label_text1.setStyleSheet("color: rgb(0,0,0);font-weight: bold; font-size: 13pt")

        pushButton_show1 = QPushButton("Devam")
        pushButton_show1.setMinimumHeight(40)
        pushButton_show1.setStyleSheet("font-weight: bold; font-size: 16pt")      
        pushButton_show1.clicked.connect(self.yaz)
        pushButton_show1.clicked.connect(self.close)
        pushButton_show1.clicked.connect(self.dongu)
        

               
        pushButton_show4 = QPushButton("Gün Sonu")
        pushButton_show4.setMinimumHeight(40)
        pushButton_show4.setStyleSheet("font-weight: bold; font-size: 16pt")
        pushButton_show4.clicked.connect(self.close)      
        pushButton_show4.clicked.connect(self.son)
        
        
          
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label_text1)
        vertical_layout.addWidget(pushButton_show1)
        vertical_layout.addWidget(pushButton_show4)

        self.setLayout(vertical_layout)
        self.setWindowTitle("Nasıl Gidiyor")
        self.resize(450,250)

    def dongu(self):
        while True:
            self.secondWindow = SecondPage()
            self.secondWindow.show()
            break
        

    def yaz(self):
        with open(filename.strftime('%d %B %Y')+".txt","a+") as file:
            file.write("{0} {1} {2}\n".format(t,s,self.yazi.text()))


    def son(self):
        saniye = time.strftime('%X')
        with open(filename.strftime('%d %B %Y')+".txt","a+") as file:
            file.write("{0} {1} {2}\n".format(t,s,self.yazi.text()))
            file.write("Çalışmaya başlama saati: {}\n".format(baslangic))
            file.write("Çalışma bitirme saati: {} \n".format(saniye))
                
        
app = QApplication([])
widget = first_GUI()
widget.show()
app.exec_()     



