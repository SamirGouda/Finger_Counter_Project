import cv2
import time
import os
import hand_tracking_module as hand_module
import fingers_module as fm


finger_list = os.listdir('finger_images')
print(finger_list)
overlay_list = []
for img_path in finger_list:
    image = cv2.imread(os.path.join('finger_images', img_path))
    image = cv2.resize(image, (150, 200))
    overlay_list.append(image)

cap = cv2.VideoCapture(0)
# set width and height for webcam
cap.set(3, 640) # set width
cap.set(4, 480) # set height
prev_time = 0
detector = hand_module.HandDetector(detection_confidence=0.7, max_num_hands=1)
fingers = fm.Fingers()

while cap.isOpened():
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)
    # print(lm_list)
    if len(lm_list) != 0:
        count = fingers.count_fingers(lm_list)
        print(count)
        cv2.putText(img, f"fingers:{count}", (490, 225), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        h, w, _ = overlay_list[0].shape
        img[:h, -w:] = overlay_list[count]
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(img, f"fps: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('gesture volume control', img)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

