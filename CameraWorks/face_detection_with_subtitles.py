import cv2
import mediapipe as mp
import threading
import collections
import textwrap

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

subtitle_text = "Tahia Djzair, Kassaman binazilat al ma7iqat.... wa dima'a azakiyat atahirat.. .. .. .."

coordinates_buffer = collections.deque(maxlen=5)

def update_subtitle_text():
    global subtitle_text
    while True:
        new_text = input("Enter new subtitle: ")
        subtitle_text = new_text

# Draw background of subtitles (black rounded rectangle)
def draw_rounded_rectangle(img, top_left, bottom_right, color, thickness, radius=10):
    x1, y1 = top_left
    x2, y2 = bottom_right

    cv2.rectangle(img, (x1 + radius, y1), (x2 - radius, y2), color, thickness)
    cv2.rectangle(img, (x1, y1 + radius), (x2, y2 - radius), color, thickness)

    cv2.circle(img, (x1 + radius, y1 + radius), radius, color, thickness)
    cv2.circle(img, (x2 - radius, y1 + radius), radius, color, thickness)
    cv2.circle(img, (x1 + radius, y2 - radius), radius, color, thickness)
    cv2.circle(img, (x2 - radius, y2 - radius), radius, color, thickness)

def wrap_text(text, max_width, font, font_scale, thickness):
    """Splits text into lines that fit within max_width."""
    lines = []
    words = text.split()
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + ' ' + word
        text_size = cv2.getTextSize(test_line, font, font_scale, thickness)[0]
        if text_size[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)  

    return lines

input_thread = threading.Thread(target=update_subtitle_text, daemon=True)
input_thread.start()

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                coordinates_buffer.append((x, y, w, h))

                avg_x = int(sum([coord[0] for coord in coordinates_buffer]) / len(coordinates_buffer))
                avg_y = int(sum([coord[1] for coord in coordinates_buffer]) / len(coordinates_buffer))
                avg_w = int(sum([coord[2] for coord in coordinates_buffer]) / len(coordinates_buffer))
                avg_h = int(sum([coord[3] for coord in coordinates_buffer]) / len(coordinates_buffer))

                text_x = avg_x + avg_w // 2
                text_y = avg_y + avg_h + 30  

                font_size = 1.2
                font_thickness = 2
                font = cv2.FONT_HERSHEY_DUPLEX

                max_width = min(400, iw)  

                # this will wrap text
                wrapped_lines = wrap_text(subtitle_text, max_width, font, font_size, font_thickness)

                text_height = cv2.getTextSize('A', font, font_size, font_thickness)[0][1]
                total_height = (text_height + 10) * len(wrapped_lines) 

                max_line_width = max([cv2.getTextSize(line, font, font_size, font_thickness)[0][0] for line in wrapped_lines])

                centered_text_x = text_x - (max_line_width // 2)

                padding = 12
                draw_rounded_rectangle(frame, (centered_text_x - padding, text_y - padding),
                                       (centered_text_x + max_line_width + padding, text_y + total_height + padding), 
                                       (0, 0, 0), -1, radius=15)

                for i, line in enumerate(wrapped_lines):
                    line_y = text_y + (i * (text_height + 10)) + text_height
                    cv2.putText(frame, line, (centered_text_x, line_y),
                                font, font_size, (255, 255, 255), font_thickness, cv2.LINE_AA)

        cv2.imshow('Face Detection with Subtitles', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
