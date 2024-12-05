import mediapipe as mp
import cv2


def blur_faces(frame, ksize :int, draw_bbox :bool=False):

    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        H, W = frame.shape[:2]
        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgbImage)

        if results.detections:
            for detection in results.detections:

                coords = detection.location_data.relative_bounding_box
                x1 = int(coords.xmin * W) 
                y1 = int(coords.ymin * H)
                x2 = x1 + int(coords.width * W)
                y2 = y1 + int(coords.height * H)

                x1 = 0 if x1 < 0 else x1
                y1 = 0 if y1 < 0 else y1
                x2 = W if x2 > W else x2
                y2 = H if y2 > H else y2
                
                frame[y1:y2, x1:x2] = cv2.blur(frame[y1:y2, x1:x2], (ksize,ksize))
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1) if draw_bbox else None

        return frame


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output_frame = blur_faces(frame, 39)

        cv2.imshow('Blurred Face', output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()