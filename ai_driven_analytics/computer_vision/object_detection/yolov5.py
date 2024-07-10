import torch
import torch.nn as nn
import torchvision

class YOLOv5(nn.Module):
    def __init__(self, num_classes):
        super(YOLOv5, self).__init__()
        self.backbone = torchvision.models.densenet121(pretrained=True)
        self.neck = nn.Sequential(
            nn.Conv2d(1024, 256, kernel_size=1),
            nn.ReLU(),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.head = nn.Sequential(
            nn.Conv2d(256, num_classes, kernel_size=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.backbone(x)
        x = self.neck(x)
        x = self.head(x)
        return x

class YOLOv5Loss(nn.Module):
    def __init__(self, num_classes):
        super(YOLOv5Loss, self).__init__()
        self.num_classes = num_classes

    def forward(self, output, target):
        loss = 0
        for i in range(self.num_classes):
            loss += nn.BCELoss()(output[:, i], target[:, i])
        return loss
