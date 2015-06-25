
import cv2

try:
    from picamera.array import PiRGBArray
    from picamera import PiCamera

except Exception as e:
    class Camera():
        def __init__(self, (xdim, ydim)):
            self.video_capture = cv2.VideoCapture(0)
            self.video_capture.set(3,xdim)
            self.video_capture.set(4,ydim)
        def update(self):
            self.frame = self.video_capture.read()[1]
        def release(self):
            self.video_capture.release()

else:
    class Camera():
        def __init__(self, (xdim, ydim)):
            self.mCamera = PiCamera()
            self.mCamera.resolution = (xdim, ydim)
            self.mCamera.framerate = 16
            self.mStream = PiRGBArray(self.mCamera)
            time.sleep(2.0)
        def update(self):
            self.mStream.truncate(0)
            self.mCamera.capture(self.mStream, format="bgr")
            self.frame = self.mStream.array
        def release(self):
            pass
