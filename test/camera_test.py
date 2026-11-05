from djitellopy import Tello
import cv2


tello = Tello()
tello.connect()

print("Battery:", tello.get_battery())

tello.streamoff()
tello.streamon()

while True:
    frame = tello.get_frame_read().frame

    # RGB -> BGR để OpenCV hiện màu đúng hơn
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    frame = cv2.resize(frame, (640, 480))

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()