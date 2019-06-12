from myui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import process
import os
import torch
from PyQt5.QtGui import QPixmap
from torch import nn
from unet import UNet


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushBt_reset_10.clicked.connect(self.open_all)  # 打开图像文件路径
        self.pushBt_up_10.clicked.connect(self.pre)
        self.pushBt_dwn_10.clicked.connect(self.next)
        self.pushBt_cntinu_10.clicked.connect(self.continu)
        # n_class = 3
        # model = UNet(n_channels=3, n_classes=n_class)
        # model = nn.DataParallel(model, device_ids=[0])
        # model.load_state_dict(torch.load('trainmodels.pth'))


    # def open_one(self):  # 处理单张图像
    #     file_name = QFileDialog.getOpenFileName()
    #     path = file_name[0]  # [0]是完整路径，[1]是‘All files *’
    #     #        print(path)
    #     self.label_10_response(path)

    def open_all(self):  # 批量处理图像
        self.label_10.setStyleSheet('font: 28pt "Agency FB"')
        self.label_10.setStyleSheet('color: rgb(255, 0, 0)')
        # self.label_10.setText("开始读入图像文件,请稍等......")
        try:
            self.directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
            self.file_list = []  # 存储所有文件的文件名
            path_list = os.listdir(self.directory)
            for file_name in path_list:
                if os.path.splitext(file_name)[1] == ".jpg":
                    self.file_list.append(file_name)
            self.im_idx = 0
            self.file_num = len(self.file_list)
            # self.label_imNum_10.setStyleSheet('font: 20pt "Agency FB"')
            # self.label_imNum_10.setStyleSheet('color: rgb(0, 0, 0)')
            strIm_num = "图像总数: " + str(self.file_num)
            self.label_imNum_10.setText(strIm_num)
            strIm_num = "处理第 " + str(self.im_idx + 1) + " 张"
            self.label_i_10.setText(strIm_num)
            pathImg = self.directory + "/" + self.file_list[self.im_idx]
            self.label_10_response(pathImg)
        except Exception:
            pass

    def pre(self):
        try:
            if self.im_idx < 0:
                return
            else:
                self.im_idx -= 1
                pathImg = self.directory + "/" + self.file_list[self.im_idx]
                # self.label_i_10.setStyleSheet('font: 20pt "Agency FB"')
                # self.label_i_10.setStyleSheet('color: rgb(0, 0, 0)')
                strIm_num = "处理第 " + str(self.im_idx + 1) + " 张"
                self.label_i_10.setText(strIm_num)
                self.label_10_response(pathImg)
        except Exception:
            pass

    def next(self):
        try:
            if self.im_idx >= self.file_num - 1:
                return
            else:
                self.im_idx += 1
                pathImg = self.directory + "/" + self.file_list[self.im_idx]
                # print(pathImg)
                # self.label_i_10.setStyleSheet('font: 26pt "Agency FB"')
                # self.label_i_10.setStyleSheet('color: rgb(0, 0, 0)')
                strIm_num = "处理第 " + str(self.im_idx + 1) + " 张"
                self.label_i_10.setText(strIm_num)
                self.label_10_response(pathImg)
        except Exception as e:
            print(e)

    def continu(self):
        if self.count:
            img = QPixmap(self.fp2)
            self.label_10.setPixmap(img)
            self.count = 0
        else:
            img = QPixmap(self.fp1)
            self.label_10.setPixmap(img)
            self.count = 1

    def label_10_response(self, pathImg):
        (fp1, fp2, results) = process.pro(pathImg)
        self.count = 1
        self.fp1 = fp1
        self.fp2 = fp2
        w = self.label_10.width()
        h = self.label_10.height()
        img = QPixmap(fp1)
        img = img.scaled(w, h)
        self.label_10.setScaledContents(True)  # 让图片自适应label大小
        self.label_10.setPixmap(img)
        if results == '良性':
            self.label_res_10.setStyleSheet('color: rgb(0, 0, 127)')
        else:
            self.label_res_10.setStyleSheet('color: rgb(254, 0, 0)')
        self.label_res_10.setText('预测结果为：' + results)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    app.exec_()
