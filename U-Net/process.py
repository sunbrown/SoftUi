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
    print(model)

    model = nn.DataParallel(model, device_ids=[0])

    model.load_state_dict(torch.load('trainmodels.pth'))

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.3301, 0.3301, 0.3301],
                             std=[0.1938, 0.1938, 0.1938])
    ])
    image = Image.open(path).convert('RGB')
    image = image.resize((224, 224), Image.ANTIALIAS)
    image = transform(image)
    n = image.size()
    data = torch.ones(1, 3, n[1], n[2])
    data[0] = image
    
    srcim_tensor = data#保存原图
    
    data = Variable(data.cuda(0))
    with torch.no_grad():
        output = model(data)
    out = torch.reshape(output.cpu(), (n_class, n[1], n[2]))
    pre = torch.max(out, 0)[1]
    out_img_tensor = torch.zeros(3, n[1], n[2])
    out_img_tensor[0, pre == 2] = 1
    out_img_tensor[1, pre == 1] = 1
    #=========================================
    srcim_tensor = torch.reshape(srcim_tensor,(3, n[1], n[2]))
    for i in range(H):
        for j in range(W):
            if out_img_tensor[0, i, j] == 1 or out_img_tensor[1, i, j] == 1:
                        srcim_tensor[:,i,j] = 0
    out_img_tensor = srcim_tensor + out_img_tensor
    #待修改，
    #==========================================
    
    path_filename = osp.split(path)
    filename = path_filename[1]#[0]表示file的路径, [1]表示文件
    pil_trans = transforms.ToPILImage('RGB')
    out_img = pil_trans(out_img_tensor)
    out_img.save('../../segmented_data/filename')
    img1 = QPixmap('../../segmented_data/filename')
    return img1
    
    

if __name__ == '__main__':
    path = r'D:\code\thyroid_nodule\data\img\1.2.250.1.204.5.8373722513.201611101635204868.75.dcm.jpg'
    img = pro(path)
    img.show()
