# Intel Scene Classification Challenge

The problem statement is available on [analytics vidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-intel-scene-classification-challe/). The problem is to classify scene depicted in the image. An example is given below

![Example image](example.png)

## Download the pretrained model

Download the pretrained model from [this link](https://drive.google.com/open?id=1Q6e9wwovM0cACbiINI2crL9rgcbPtiSf). I have used RESNET-50 architecture and added two fully-connected layers at the end of the architecture.

## Key step

Remove the mislabeled and confusing images from the dataset to increase the accuracy of the classifying the scenes.
