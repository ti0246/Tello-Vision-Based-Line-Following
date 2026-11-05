import cv2

from modules.tello_controller import TelloController
from modules.line_detection import detect_line
from modules.pid_controller import PID

from config import *


def draw_ui(frame, is_flying, error=None):
    """
    Draw realtime UI on screen
    """

    # Drone status
    status = "FLYING" if is_flying else "LANDED"

    color = (0, 255, 0) if is_flying else (0, 0, 255)

    cv2.putText(
        frame,
        f"Status: {status}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    # Controls
    cv2.putText(
        frame,
        "Controls:",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "[T] Takeoff",
        (40, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "[F] Land",
        (40, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "[Q] Quit",
        (40, 210),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    # PID Error
    if error is not None:
        cv2.putText(
            frame,
            f"PID Error: {error}",
            (20, 270),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )


def main():

    drone = TelloController()

    drone.connect()
    drone.stream_on()

    pid = PID(KP, KI, KD)

    is_flying = False

    print("[INFO] Press T to takeoff")
    print("[INFO] Press F to land")
    print("[INFO] Press Q to quit")

    while True:

        frame = drone.get_frame()

        cx, cy, mask = detect_line(frame)

        error = None

        # Detect line
        if cx is not None:

            error = cx - FRAME_WIDTH // 2

            control = pid.update(error)

            control = max(
                -MAX_SPEED,
                min(MAX_SPEED, int(control))
            )

            # Follow line only when flying
            if is_flying:
                drone.send_rc(
                    left_right=control,
                    forward_backward=FORWARD_SPEED,
                    up_down=0,
                    yaw=0
                )

            # Draw center point
            cv2.circle(
                frame,
                (cx, cy),
                10,
                (0, 255, 0),
                -1
            )

            # Draw center line
            cv2.line(
                frame,
                (FRAME_WIDTH // 2, 0),
                (FRAME_WIDTH // 2, FRAME_HEIGHT),
                (255, 0, 0),
                2
            )

        # Draw UI
        draw_ui(frame, is_flying, error)

        # Show windows
        cv2.imshow("Tello Camera", frame)
        cv2.imshow("Mask", mask)

        key = cv2.waitKey(1) & 0xFF

        # TAKEOFF
        if key == ord('t'):

            if not is_flying:
                drone.takeoff()
                is_flying = True

        # LAND
        elif key == ord('f'):

            if is_flying:
                drone.land()
                is_flying = False

        # QUIT
        elif key == ord('q'):

            if is_flying:
                drone.land()

            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()