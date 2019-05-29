import os
import torch
import cv2 as cv
import numpy as np
from torch.autograd import Variable
from PyQt5.QtGui import QPixmap
from torch import nn
from PIL import Image
from torchvision import transforms
from unet import UNet
from os import path as osp

os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3'


def pro(path):
    n_class = 3
    model = UNet(n_channels=3, n_classes=n_class)
    model = nn.DataParallel(model, device_ids=[0])
    model.load_state_dict(torch.load('trainmodels.pth'))
    tensor2pil = transforms.ToPILImage('RGB')
    img2tensor = transforms.ToTensor()
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.3301, 0.3301, 0.3301],
                             std=[0.1938, 0.1938, 0.1938])
    ])
    image = Image.open(path).convert('RGB')
    image = image.resize((224, 224), Image.ANTIALIAS)
    in_img_tensor = transform(image)
    in_img_origin = img2tensor(image)
    n = in_img_tensor.size()
    data = torch.ones(1, 3, n[1], n[2])
    data[0] = in_img_tensor
    in_img_origin = torch.squeeze(in_img_origin)  # 保存原图
    data = Variable(data.cuda(0))
    with torch.no_grad():
        output = model(data)  # 把图片输入模型处理
    out = torch.reshape(output.cpu(), (n_class, n[1], n[2]))
    pre = torch.max(out, 0)[1]
    out_img_tensor = torch.zeros(3, n[1], n[2])
    out_img_tensor[0, pre == 2] = 1
    out_img_tensor[1, pre == 1] = 1
    if torch.sum(out_img_tensor[0]) - torch.sum(out_img_tensor[1]) > 0:
        out_img_tensor[0] += out_img_tensor[1]
        out_img_tensor[1] = 0
        results = '恶性'
    else:
        out_img_tensor[1] += out_img_tensor[0]
        out_img_tensor[0] = 0
        results = '良性'  # 判断良恶性
    out_img_ndarray = cv.cvtColor(np.asarray(tensor2pil(out_img_tensor)), cv.COLOR_RGB2BGR)
    image_cv = cv.cvtColor(np.asarray(image), cv.COLOR_RGB2BGR)
    out_img_ndarray = contours(out_img_ndarray, image_cv, results)

    #  =========================================
    # for i in range(n[1]):
    #     for j in range(n[2]):
    #         if out_img_tensor[0, i, j] == 1 or out_img_tensor[1, i, j] == 1:
    #             in_img_origin[:, i, j] = 0
    #
    #
    # out_img_tensor = in_img_origin + out_img_tensor
    # ==========================================
    path_filename = osp.split(path)
    f_name = os.path.splitext(path_filename[1])[0]
    filename = path_filename[1]  # [0]表示file的路径, [1]表示文件
    out_img_pil = Image.fromarray(cv.cvtColor(out_img_ndarray, cv.COLOR_BGR2RGB))
    fp = path_filename[0] + '/res/'
    if not os.path.exists(fp):
        os.mkdir(fp)
    fp1 = fp + f_name + '.png'
    fp2 = fp+'tmp.png'
    out_img_pil.save(fp1)
    image.save(fp + 'tmp.png')
    return fp1, fp2, results


def contours(mask, src, results):
    dst = cv.GaussianBlur(mask, (3, 3), 0)
    # 转换为灰度图像
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    # 转换为二值图像
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("bi", binary)
    if results == '良性':
        color = (0, 255, 255)
    else:
        color = (0, 0, 255)
    clone_img, contour_lines, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contour_lines):
        cv.drawContours(src, contour_lines, i, color, 1)
    # cv.imshow("contours", src)
    return src


if __name__ == '__main__':
    path = r'./28_0.9782.jpg'
    img = pro(path)
    img.show()
