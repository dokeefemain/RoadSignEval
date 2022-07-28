# Traffic sign detection model comparison
The purpous of this repository is to compair the preformance of Faster RCNN Inception Resnet V2, YOLO V3 at Traffic Sign Detection.
For Inception Renet V2 and YOLO V3 you can see my training processes [here](https://github.com/dokeefemain/Traffic_sign_detection_Faster_RCNN) and [here](https://github.com/dokeefemain/YOLOV3).

## Evaluation
The evaluation metric I chose to use is mAP. The results are shown below.

| Model  |   mAP    | Compilation Time |
|--------|:--------:|-----------------:|
| IRV2   |   0.88   |             1.59 |
| YOLOV3 |   0.86   |             0.21 |
The mAP for each are very similar. The main difference can be seen when it comes to compilation time. YOLO V3 is 7 and a half times faster than Fast IRV2. This provides a big advantage since it allows for real time detection on almost any system.

This doesn't tell the full story though. YOLO V3 suffers from poor generalization in comparison to Fast IRV2 which can work on almost any image containing a road sign. I suspect that this is the result of the nature of YOLO being that it only looks once.
The best way that I can describe this is that with Faster IRV2 the model is looking for the road sign as a result of it's use of a RPN while YOLO looks at the image as a whole and then decides if it contains a road sign. 
I'm planning on testing this by training IRV2 with a YOLO style output but I'm still in the process of getting that together and will update this after I have it completed. 