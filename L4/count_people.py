from pathlib import Path

import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO


def main():
    local_picture = Path(__file__).with_name("people.jpg")
    image_source = (
        str(local_picture)
        if local_picture.exists()
        else "https://ultralytics.com/images/bus.jpg"
    )

    vision_model = YOLO("yolo11n.pt")
    person_class_id = 0
    confidence_threshold = 0.35
    print("Class to count:", vision_model.names[person_class_id])
    print("Image source:", image_source)

    image_predictions = vision_model.predict(
        source=image_source,
        classes=[person_class_id],
        conf=confidence_threshold,
        verbose=False,
    )
    image_result = image_predictions[0]
    people_count = len(image_result.boxes)
    print(f"Detected people: {people_count}")

    annotated_image = image_result.plot()
    label = f"Detected people: {people_count}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    thickness = 2
    (text_width, text_height), baseline = cv2.getTextSize(
        label, font, font_scale, thickness
    )
    cv2.rectangle(
        annotated_image,
        (10, 10),
        (20 + text_width, 20 + text_height + baseline),
        (0, 0, 0),
        cv2.FILLED,
    )
    cv2.putText(
        annotated_image,
        label,
        (15, 15 + text_height),
        font,
        font_scale,
        (255, 255, 255),
        thickness,
        cv2.LINE_AA,
    )

    output_path = Path(__file__).with_name("counted_people.jpg")
    if not cv2.imwrite(str(output_path), annotated_image):
        raise OSError(f"Could not save the annotated image to {output_path}")
    print("Saved annotated image:", output_path)

    plt.figure(figsize=(10, 7))
    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()