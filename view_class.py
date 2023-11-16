import os
import xml.etree.ElementTree as ET
import glob


def count_num(indir):
    label_list = []
    # 提取xml文件列表
    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations) + '*.xml')

    dict = {}
    for i, file in enumerate(annotations):
        in_file = open(file, encoding='utf-8')
        tree = ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            name = obj.find('name').text
            if (name in dict.keys()):
                dict[name] += 1  # 如果标签不是第一次出现，则+1
            else:
                dict[name] = 1  # 如果标签是第一次出现，则将该标签名对应的value初始化为1
    print("各类标签的数量分别为：")
    for key in dict.keys():
        print(key + ': ' + str(dict[key]))
        label_list.append(key)
    print("标签类别如下：")
    print(label_list)


if __name__ == '__main__':
    indir = 'data/Annotations/val'
    count_num(indir)

