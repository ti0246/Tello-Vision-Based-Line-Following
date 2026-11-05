from djitellopy import Tello
import cv2


class TelloController:
    def __init__(self):
        self.tello = Tello()

    def connect(self):
        print("[INFO] Connecting...")
        self.tello.connect()
        print(f"[INFO] Battery: {self.tello.get_battery()}%")

    def stream_on(self):
        self.tello.streamoff()
        self.tello.streamon()

    def get_frame(self):
        frame = self.tello.get_frame_read().frame

        # Tello frame is RGB, OpenCV uses BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        frame = cv2.resize(frame, (640, 480))
        return frame

    def takeoff(self):
        self.tello.takeoff()

    def land(self):
        self.tello.land()

    def send_rc(self, left_right, forward_backward, up_down, yaw):
        self.tello.send_rc_control(
            left_right,
            forward_backward,
            up_down,
            yaw
        )