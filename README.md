# hand-detection.PyTorch
Hand detection in PyTorch

<p align="center">
	<a href="https://github.com/zllrunning/hand-detection.PyTorch">
    <img class="page-image" src="https://github.com/zllrunning/hand-detection.PyTorch/blob/master/data/video/saveVideo.gif" >
	</a>
</p>

### Contents
- [Installation](#installation)
- [Training](#training)
- [Demo](#Demo)
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

1. Prepare training data:
```
	-- download EgoHands dataset
	-- generate bounding boxes and visualize them to ensure correctness
	-- convert bbox file to VOC format
```

```Shell
cd $HandBoxes_ROOT/
sh prepare_data.sh
```

2. Train the model using EgoHands dataset:
```Shell
python3 train.py
```

If you do not wish to train the model, you can download [our pre-trained model](https://drive.google.com/open?id=1eFSwZoSfVVroAy7LiGYybW6F8ErshoZW) and save it in `$HandBoxes_ROOT/weights`.


## Demo
1. Evaluate the trained model using:
```Shell
# evaluate using GPU
python test.py --video data/video/hand.avi
# evaluate using cpu
python test.py --image data/video/CARDS_OFFICE_H_T_frame_1085.jpg --cpu
```
    
## References
This project is based on [FaceBoxes.PyTorch](https://github.com/zisianw/FaceBoxes.PyTorch)
- [handtracking](https://github.com/victordibia/handtracking)
- [od-annotation](https://github.com/hzylmf/od-annotation)
