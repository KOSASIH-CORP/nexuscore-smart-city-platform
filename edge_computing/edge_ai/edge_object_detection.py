import cv2

class EdgeObjectDetection:
    def __init__(self, model_path):
        self.model = cv2.dnn.readNetFromDarknet(model_path)

    def detect_objects(self, image):
        blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), [0,0,0], 1, crop=False)
        self.model.setInput(blob)
        outputs = self.model.forward(self.model.getUnconnectedOutLayersNames())
        return outputs
