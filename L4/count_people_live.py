import cv2
from ultralytics import YOLO


def main():
    vision_model = YOLO("yolo11n.pt")
    person_class_id = 0
    confidence_threshold = 0.35
    camera = cv2.VideoCapture(0) # Try to open the second webcam if exists
    # camera = cv2.VideoCapture(1) # Try to open the second webcam if exists

    if not camera.isOpened():
        camera.release()
        raise RuntimeError("Could not open webcam 0. Check its connection and permissions.")

    try:
        print("Press q in the video window to quit.")
        while True:
            frame_read, frame = camera.read()
            if not frame_read:
                print("Could not read a frame from the webcam.")
                break

            image_predictions = vision_model.predict(
                source=frame,
                classes=[person_class_id],
                conf=confidence_threshold,
                verbose=False,
            )
            image_result = image_predictions[0]
            people_count = len(image_result.boxes)
            annotated_frame = image_result.plot()

            label = f"Detected people: {people_count}"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.8
            thickness = 2
            (text_width, text_height), baseline = cv2.getTextSize(
                label, font, font_scale, thickness
            )
            cv2.rectangle(
                annotated_frame,
                (10, 10),
                (20 + text_width, 20 + text_height + baseline),
                (0, 0, 0),
                cv2.FILLED,
            )
            cv2.putText(
                annotated_frame,
                label,
                (15, 15 + text_height),
                font,
                font_scale,
                (255, 255, 255),
                thickness,
                cv2.LINE_AA,
            )

            cv2.imshow("People counter", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()