import cv2
import numpy as np
from config import LOWER_ORANGE, UPPER_ORANGE


def detect_line(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array(LOWER_ORANGE)
    upper = np.array(UPPER_ORANGE)

    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) > 0:
        biggest = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(biggest)

        if area > 500:
            x, y, w, h = cv2.boundingRect(biggest)

            cx = x + w // 2
            cy = y + h // 2

            return cx, cy, mask

    return None, None, mask