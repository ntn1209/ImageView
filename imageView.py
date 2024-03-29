import sys
import os
try:
    from PyQt6.QtWidgets import (QApplication,
                                 QWidget,
                                 QPushButton,
                                 QLabel,
                                 QLineEdit,
                                 QVBoxLayout,
                                 QHBoxLayout,
                                 QGridLayout,QDesktopWidget)
    from PyQt6.QtCore import Qt,QSize
    from PyQt6.QtGui import QIcon,QIntValidator,QFont,QPixmap
except:
    from PyQt5.QtWidgets import (QApplication,
                                 QWidget,
                                 QPushButton,
                                 QLabel,
                                 QLineEdit,
                                 QVBoxLayout,
                                 QHBoxLayout,
                                 QGridLayout,QDesktopWidget)
    from PyQt5.QtCore import Qt,QSize
    from PyQt5.QtGui import QIcon,QIntValidator,QFont,QPixmap

PhotoPath1 = r"D:\3sept23"

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.showMaximized()
        # self.showFullScreen() #never use
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setWindowTitle("ImageView")
        self.getImageList()
        # print(self.imageList1)
        sizeObject = QDesktopWidget().screenGeometry(-1)
        print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))

        layoutMain = QVBoxLayout()
        layoutMain.setSpacing(10)
        self.setLayout(layoutMain)
        print(self.width() , self.height())
        layout1 = QHBoxLayout()
        if sizeObject.width() >= sizeObject.height():  #convert to flag
            layout2 = QHBoxLayout(self)
        else:
            layout2 = QVBoxLayout(self)

        layoutMain.addLayout(layout1)
        layoutMain.addLayout(layout2)

        self.label1 = QLabel("Image")
        layout1.addWidget(self.label1)

        self.label0 = QLabel()
        self.label0.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout1.addWidget(self.label0,10)

        self.firstImage= 1
        self.currentImage = self.firstImage
        self.lastImage= len(self.imageList1)

        ValidInt = QIntValidator(self.firstImage,self.lastImage,self)
        self.input1 = QLineEdit(self)
        self.input1.setValidator(ValidInt)
        self.input1.setText(str(self.currentImage))
        self.input1.returnPressed.connect(self.goToImagef)
        self.input1.setFixedSize(30,20)
        # self.input1.textChanged.connect(self.goToImage)
        layout1.addWidget(self.input1)


        self.currentLabel = QLabel()
        self.currentLabel.setNum(self.currentImage)

        self.slash = QLabel(" / ")

        self.lastLabel = QLabel(self)
        self.lastLabel.setNum(self.lastImage)

        # self.imageNum = QLabel("we")
        layout1.addWidget(self.currentLabel)
        layout1.addWidget(self.slash)
        layout1.addWidget(self.lastLabel)

        prevButton = QPushButton("Prev")
        prevButton.setFixedWidth(50)
        prevButton.clicked.connect(self.prevImagef)
        layout1.addWidget(prevButton)

        nextButton = QPushButton("Next")
        nextButton.setFixedWidth(50)
        nextButton.clicked.connect(self.nextImagef)
        # nextButton.setStyleSheet("background-color: black")
        layout1.addWidget(nextButton)


        layoutPic1 = QVBoxLayout(self)
        self.pic1Name = QLabel(self)
        self.pic1Name.setText("Image1")
        self.pic1Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pic1Label = QLabel(self)
        self.pic1Label.setFixedSize(800,900)
        layoutPic1.addWidget(self.pic1Name, Qt.AlignmentFlag.AlignRight)
        layoutPic1.addWidget(self.pic1Label, Qt.AlignmentFlag.AlignLeft)
        layoutPic1.addStretch(0)

        layoutPic2 = QVBoxLayout(self)

        self.pic2Name = QLabel(self)
        self.pic2Name.setText("Image2")
        self.pic2Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pic2Label = QLabel(self)
        self.pic2Label.setFixedSize(600, 600)
        self.pic2Bottom = QLabel(self)
        self.pic2Bottom.setFixedHeight(300)
        layoutPic2.addWidget(self.pic2Name,Qt.AlignmentFlag.AlignRight)
        layoutPic2.addWidget(self.pic2Label,Qt.AlignmentFlag.AlignRight)
        layoutPic2.addWidget(self.pic2Bottom,Qt.AlignmentFlag.AlignRight)
        layoutPic2.setAlignment(Qt.AlignmentFlag.AlignRight)
        # layoutPic2.addStretch(0)

        layout2.addLayout(layoutPic1)
        layout2.addLayout(layoutPic2)

        self.showImageDefault()

        

    def showImageDefault(self):
        self.showImageName()
        pixmap = QPixmap(self.imageList1[0])
        self.pic1Label.setPixmap(pixmap.scaled(800,950))
        self.pic2Label.setPixmap( pixmap.scaled(600,900))

    def showImage1(self):
        pixmap = QPixmap(self.imageList1[self.currentImage-1])
        self.pic1Label.setPixmap(pixmap.scaled(800, 950))
        self.pic2Label.setPixmap(pixmap.scaled(600, 900))

    def getImageList(self):
        self.imageList1 =[]
        for file in os.listdir(PhotoPath1):
            if file.endswith(".jpg") or file.endswith(".png"):
                self.imageList1.append(os.path.join(PhotoPath1,file))

    def showImageName(self):
        imgName = self.imageList1[self.currentImage-1].split("\\")[-1]
        print(imgName)
        self.pic1Name.setText(imgName)
        self.pic2Name.setText(imgName)

    def nextImagef(self):
        if self.currentImage >= self.lastImage or self.currentImage <=0:
            self.currentImage = self.firstImage
        else:
            self.currentImage = self.currentImage+1
        self.currentLabel.setNum(self.currentImage)
        self.input1.setText(str(self.currentImage))
        self.showImageName()
        self.showImage1()

        print(self.currentImage)

    def prevImagef(self):
        if self.currentImage <= self.firstImage :
            self.currentImage = self.lastImage
        else:
            self.currentImage = self.currentImage-1
        self.currentLabel.setNum(self.currentImage)
        self.input1.setText(str(self.currentImage))
        self.showImage1()
        self.showImageName()
        print(self.currentImage)

    def goToImagef(self):
        self.currentImage = int(self.input1.text())
        if self.currentImage >self.lastImage or self.currentImage<self.firstImage:
            self.currentImage= self.firstImage
        self.currentLabel.setNum(self.currentImage)
        self.showImage1()
        self.showImageName()
        print(self.currentImage)


app = QApplication(sys.argv)
window = Window()
with open("styles.css","r") as file:
    app.setStyleSheet(file.read())



window.show()
sys.exit(app.exec())


