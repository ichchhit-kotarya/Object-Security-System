import cv2

cap = cv2.VideoCapture(1)

tracker = cv2.legacy.TrackerMOSSE_create()
success, img = cap.read()
bbox = cv2.selectROI('Tracking', img, False)
cv2.destroyWindow('Tracking')  # Destroy the ROI selection window
tracker.init(img, bbox)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(fps), (75, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
