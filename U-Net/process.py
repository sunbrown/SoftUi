import os
import torch
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
        output = model(data)
    out = torch.reshape(output.cpu(), (n_class, n[1], n[2]))
    pre = torch.max(out, 0)[1]
    out_img_tensor = torch.zeros(3, n[1], n[2])
    out_img_tensor[0, pre == 2] = 1
    out_img_tensor[1, pre == 1] = 1
    if torch.sum(out_img_tensor[0])-torch.sum(out_img_tensor[1]) > 0:
        out_img_tensor[0] = out_img_tensor[0] + out_img_tensor[1]
        out_img_tensor[1] = 0
        results = '恶性'
    else:
        out_img_tensor[1] = out_img_tensor[0] + out_img_tensor[1]
        out_img_tensor[0] = 0
        results = '良性'
    #  =========================================
    for i in range(n[1]):
        for j in range(n[2]):
            if out_img_tensor[0, i, j] == 1 or out_img_tensor[1, i, j] == 1:
                in_img_origin[:, i, j] = 0


    out_img_tensor = in_img_origin + out_img_tensor
    # ==========================================
    path_filename = osp.split(path)
    f_name = os.path.splitext(path_filename[1])[0]
    filename = path_filename[1]  # [0]表示file的路径, [1]表示文件
    out_img_pil = tensor2pil(out_img_tensor)
    # os.mkdir(path_filename[0] + '/res/')
    out_img_pil.save(path_filename[0] + '/res/' + f_name + '.png')
    return_img = QPixmap(path_filename[0] + '/res/' + f_name + '.png')
    return return_img, results


if __name__ == '__main__':
    path = r'D:\code\thyroid_nodule\data\img\1.2.250.1.204.5.8373722513.201611101635204868.75.dcm.jpg'
    img = pro(path)
    img.show()
