# hand-detection.PyTorch
Hand detection in PyTorch

### Contents
- [Installation](#installation)
- [Training](#training)
- [Evaluation](#evaluation)
- [References](#references)

## Installation
1. Install [PyTorch-0.4.0](https://pytorch.org/) according to your environment.

2. Clone this repository. We will call the cloned directory as `$HandBoxes_ROOT`.
```Shell
git clone https://github.com/zllrunning/hand-detection.PyTorch.git
```

3. Compile the nms:
```Shell
./make.sh
```

_Note: We currently only support PyTorch-0.4.0 and Python 3+._

## Training
1. Download [EgoHands dataset](http://vision.soic.indiana.edu/projects/egohands/) dataset, place the images under this directory:
  ```Shell
  $HandBoxes_ROOT/data/Hand/images
  ```

2. Train the model using EgoHands dataset:
  ```Shell
  cd $HandBoxes_ROOT/
  python3 train.py
  ```

If you do not wish to train the model, you can download [our pre-trained model](https://drive.google.com/open?id=128m1QasIwQRkrY-Eb5Epi-ShXnrZWUCQ) and save it in `$HandBoxes_ROOT/weights`.


## Evaluation
1. Evaluate the trained model using:
```Shell
# evaluate using GPU
python3 test.py
# evaluate using cpu
python3 test.py --cpu
```
    
## References
- [FaceBoxes.PyTorch](https://github.com/zisianw/FaceBoxes.PyTorch)
- [Official release (Caffe)](https://github.com/sfzhang15/FaceBoxes)
- A huge thank you to SSD ports in PyTorch that have been helpful:
  * [ssd.pytorch](https://github.com/amdegroot/ssd.pytorch), [RFBNet](https://github.com/ruinmessi/RFBNet)

  _Note: If you can not download the converted annotations, the provided images and the trained model through the above links, you can download them through [BaiduYun](https://pan.baidu.com/s/1HoW3wbldnbmgW2PS4i4Irw)._
