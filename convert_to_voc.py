# -*- coding: UTF-8 -*-
import codecs
import hashlib
import traceback
import os
import json
import random
import xml2dict
import pandas as pd


def convert_to_voc2007(file_path_1='annotation/annotation1.txt', file_path_2='annotation/annotation2.txt'):
    """转换标注数据为VOC2007格式"""
    # with codecs.open(file_path, mode='r', encoding='utf-8') as file:
    #     lines = file.readlines()
    df_1 = pd.read_csv(file_path_1)
    df_2 = pd.read_csv(file_path_2)
    df = pd.concat([df_1, df_2], axis=0)
    # lines = df.iterrows()
    annotations = dict()
    for index, line in df.iterrows():
        # if line.strip()=='':continue
        # values = line.strip().split(',')
        name = line['filename']
        type = line['class']
        object = dict()
        object['name'] = type
        object['pose'] = 'Unspecified'
        object['truncated'] = 0
        object['difficult'] = 0
        object['bndbox'] = dict()
        object['bndbox']['xmin'] = line['xmin']
        object['bndbox']['ymin'] = line['ymin']
        object['bndbox']['xmax'] = line['xmax']
        object['bndbox']['ymax'] = line['ymax']
        if name not in annotations:
            annotation = dict()
            annotation['folder'] = 'VOC2007'
            annotation['filename'] = name
            annotation['size'] = dict()
            annotation['size']['width'] = line['width']  # 若样本未统一尺寸，请根据实际情况获取
            annotation['size']['height'] = line['height']  # 若样本未统一尺寸，请根据实际情况获取
            annotation['size']['depth'] = 3
            annotation['segmented'] = 0
            annotation['object'] = [object]
            annotations[name] = annotation
        else:
            annotation = annotations[name]
            annotation['object'].append(object)
    names = []
    path = 'annotation/VOC2007/'
    if not os.path.exists(path+'Annotations'):
        os.makedirs(path+'Annotations')
    for annotation in annotations.items():
        filename = annotation[0].split('.')[0]
        names.append(filename)
        dic = {'annotation':annotation[1]}
        convertedXml = xml2dict.unparse(dic)
        xml_nohead = convertedXml.split('\n')[1]
        file = codecs.open(path + 'Annotations/'+filename + '.xml', mode='w', encoding='utf-8')
        file.write(xml_nohead)
        file.close()
    random.shuffle(names)
    if not os.path.exists(path+'ImageSets'):
        os.mkdir(path+'ImageSets')
    if not os.path.exists(path+'ImageSets/Main'):
        os.mkdir(path+'ImageSets/Main')
    file_train = codecs.open(path+'ImageSets/Main/train.txt',mode='w',encoding='utf-8')
    file_test = codecs.open(path + 'ImageSets/Main/test.txt', mode='w', encoding='utf-8')
    file_train_val = codecs.open(path + 'ImageSets/Main/trainval.txt', mode='w', encoding='utf-8')
    file_val = codecs.open(path + 'ImageSets/Main/val.txt', mode='w', encoding='utf-8')
    count = len(names)
    count_1 = 0.25 * count
    count_2 = 0.9 * count
    for i in range(count):
        if i < count_1:
            file_train_val.write(names[i]+'\n')
            file_train.write(names[i] + '\n')
        elif count_1 <= i <count_2:
            file_train_val.write(names[i] + '\n')
            file_val.write(names[i] + '\n')
        else:
            file_test.write(names[i] + '\n')
    file_train.close()
    file_test.close()
    file_train_val.close()
    file_val.close()


if __name__ == '__main__':
    # convert_to_voc2007()
    # train = pd.read_csv('/home/zll/Downloads/projects/hand_det/train/train_labels.csv')
    # test = pd.read_csv('/home/zll/Downloads/projects/hand_det/test/test_labels.csv')
    # all = pd.concat([train, test], axis=0, ignore_index=True)
    # all.to_csv('./label.csv', index=False)
    convert_to_voc2007('./images/train/train_labels.csv', './images/test/test_labels.csv')
