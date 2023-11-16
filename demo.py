import torch
import os
path = 'data/images/'
type = 'train'
# type = 'val'
# type = 'test'
xml_path = path + type
total_xml = os.listdir(xml_path)
# print(total_xml)
num = len(total_xml)
list = range(num)
# ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')
# fval = open('data/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    ftrain.write(name)
