#!/usr/bin/env bash

python egohands_dataset_clean.py

mkdir -p data/Hand/images
mv images/train/*.jpg data/Hand/images
mv images/test/*.jpg data/Hand/images

python convert_to_voc.py

mv annotation/VOC2007/* data/Hand/

rm -r annotation/
rm -r egohands/
rm -r images/

