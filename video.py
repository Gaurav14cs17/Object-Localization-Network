import cv2, time
from model_utils import ObjectLocalizationNet, remove_initializer_from_input

# Initialize the webcam
cap = cv2.VideoCapture('p1.mp4')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
fps = cap.get(cv2.CAP_PROP_FPS)
save_path = "video.avi"
vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (int(width), int(height)))
FPS = 0

# Initialize object localizer
model_path = "onnx_weight/oln_360x480.onnx"
remove_initializer_from_input(model_path, model_path) # Remove unused nodes
localizer = ObjectLocalizationNet(model_path, threshold=0.75)

cv2.namedWindow("Objects", cv2.WINDOW_NORMAL)	
while cap.isOpened():

	# Read frame from the video
	ret, frame = cap.read()
	t0 = time.time()

	if not ret:	
		break
	
	# Update object localizer
	detections, scores = localizer(frame)

	combined_img = localizer.draw_detections(frame)
	FPS = (FPS + (1. / (time.time() - t0))) / 2
	#result_frame = cv2.putText(combined_img, "FPS=%.2f" % (FPS), (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
	vid_writer.write(combined_img)
	cv2.imshow("Objects", combined_img)

	# Press key q to stop
	if cv2.waitKey(1) & 0xFF  == ord('q'):
		break
