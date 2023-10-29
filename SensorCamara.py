import cv2
import base64

class SensorCamara:

    def __init__(self):
        pass

    def tomar_fotografia(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            # Codificar la imagen en formato base64
            _, buffer = cv2.imencode(".jpg", frame)
            imagen_base64 = base64.b64encode(buffer).decode("utf-8")
            return imagen_base64

        else:
            print("Sin cámara")
            return None