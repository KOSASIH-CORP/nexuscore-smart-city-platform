import numpy as np
import cv2

class ObjectDetection:
    def __init__(self, model_path, config_path):
        self.model_path = model_path
        self.config_path = config_path
        self.net = self.create_net()
    
    def create_net(self):
        # Create object detection network using OpenCV
        net = cv2.dnn.readNetFromDarknet(self.model_path, self.config_path)
        return net
    
    def detect_objects(self, image):
        # Detect objects in image using object detection network
        blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), [0,0,0], 1, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.getOutputsNames(self.net))
        return outs
    
    def getOutputsNames(self, net):
        # Get output layer names of object detection network
        layersNames = net.getLayerNames()
        return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    
    def draw_bounding_boxes(self, image, outs):
        # Draw bounding boxes around detected objects
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > 0.5 and classId == 0:
                    center_x = int(detection[0] * image.shape[1])
                    center_y = int(detection[1] * image.shape[0])
                    w = int(detection[2] * image.shape[1])
                    h = int(detection[3] * image.shape[0])
                    x = center_x - w / 2
                    y = center_y - h / 2
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image
