# -*- coding: utf-8 -*-
from myui import Ui_MainWindow
from PyQt5 import  QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap
import os
#import process
import numpy as np
from skimage import exposure
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushBt_reset_10.clicked.connect(self.open_all)#打开图像文件路径
        self.pushBt_up_10.clicked.connect(self.pre)
        self.pushBt_dwn_10.clicked.connect(self.next)
        self.pushBt_cntinu_10.clicked.connect(self.open_one)
    def open_one(self):#处理单张图像
        file_name = QFileDialog.getOpenFileName()
        path = file_name[0]#[0]是完整路径，[1]是‘All files *’
#        print(path)
        self.label_10_response(path)
        
    def open_all(self):#批量处理图像
#        file,ok=QFileDialog.getOpenFileName(self,"打开",None,"*.jpg;;*.png;;*.tif;;*.bmp")
        print("开始读入图像文件......")
        self.label_10.setStyleSheet('font: 28pt "Agency FB"')
        self.label_10.setStyleSheet('color: rgb(255, 0, 0)')
        self.label_10.setText("开始读入图像文件,请稍等......")
        self.directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(self.directory)  # 打印文件夹路径
        self.file_list = []#存储所有文件的文件名
        path_list = os.listdir(self.directory)
        for file_name in path_list:
            if os.path.splitext(file_name)[1] == ".jpg":
#                print(file_name)
                self.file_list.append(file_name)
#        img = cv2.imread(self.directory + "/" + self.file_list[0])
        self.im_idx = 0;
        self.file_num = len(self.file_list)
        self.label_imNum_10.setStyleSheet('font: 20pt "Agency FB"')
        self.label_imNum_10.setStyleSheet('color: rgb(0, 0, 0)')
        strIm_num = "图像总数: " +  str(self.file_num)
        self.label_imNum_10.setText(strIm_num)
        pathImg = self.directory + "/" + self.file_list[self.im_idx]
        self.label_10_response(pathImg)
        
    def pre(self):
        print("pre start...")
        if self.im_idx < 0:
            return
        self.im_idx -= 1
        print(self.im_idx)
        pathImg = self.directory + "/" + self.file_list[self.im_idx]
        print(pathImg)
        self.label_i_10.setStyleSheet('font: 20pt "Agency FB"')
        self.label_i_10.setStyleSheet('color: rgb(0, 0, 0)')
        strIm_num = "正则处理第 " +  str(self.im_idx + 1) + " 张..."
        self.label_i_10.setText(strIm_num)
        self.label_10_response(pathImg)
        print("pre end...")
        
    def next(self):
        print("next start...")
        if self.im_idx > self.file_num:
            return
        self.im_idx += 1
        pathImg = self.directory + "/" + self.file_list[self.im_idx]
        print(pathImg)
        self.label_i_10.setStyleSheet('font: 20pt "Agency FB"')
        self.label_i_10.setStyleSheet('color: rgb(0, 0, 0)')
        strIm_num = "正则处理第 " +  str(self.im_idx) + " 张..."
        self.label_i_10.setText(strIm_num)
        self.label_10_response(pathImg)
        print("next end...")
        
    def continu(self):
        return ""
    
    def label_10_response(self, pathImg):
        img = self.process(pathImg)
        w = self.label_10.width()
        h = self.label_10.height()
        img = img.scaled(w,h)
        self.label_10.setScaledContents (True)#让图片自适应label大小
        self.label_10.setPixmap(img)
        
    def process(self, path):
        print("process...")
        return QPixmap(path)
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    app.exec_()
