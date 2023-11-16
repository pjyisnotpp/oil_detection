# oil_detection
方向实践第二次作业
一些参数设置
修改成自己的路径，在控制台输入即可

结果在labels.rar中

ultralytics.rar为改动后的ultralytics库,添加了注意力机制,增加了两个v8的yaml配置,训练时可以直接使用这个配置

#yolo task=detect mode=train model=C:\Users\89597\.conda\envs\pytorch\Lib\site-packages\ultralytics\cfg\models\v8\yolov8-p2.yaml data=oil.yaml batch=4 epochs=500 imgsz=800 workers=1 device=0 lr0=0.01 lrf=0.01 augment=true


#yolo task=detect mode=train model=runs/detect/train45/weights/last.pt data=oil.yaml batch=6 epochs=300 imgsz=640 workers=1 device=0 lr0=0.0005 lrf=0.01 augment=true

#yolo task=detect mode=val model=runs/detect/train7/weights/best.pt data=oil.yaml device=cpu nms=true imgsz=800 conf=0.4 iou=0.5 达到0.86


#yolo task=detect mode=val model=runs/detect/train45/weights/best.pt data=oil.yaml device=cpu nms=true imgsz=640


#yolo task=detect mode=predict model=runs/detect/train7/weights/best.pt source=data/images/test device=0 save_txt=true save_conf=true conf=0.4 iou=0.5 nms=true
