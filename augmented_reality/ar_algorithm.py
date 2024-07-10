import cv2

class ARAlgorithm:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def detect_marker(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250))
        return corners, ids

    def draw_augmented_reality(self, frame, corners, ids):
        cv2.drawContours(frame, [corners], -1, (0, 255, 0), 2)
        cv2.putText(frame, f'Marker ID: {ids[0][0]}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        return frame
