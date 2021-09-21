# takes videos and outputs frames

import cv2
vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0
while success:
  success,image = vidcap.read()
  count += 1
  if count % 30 != 0:
    continue
  cv2.imwrite("test_frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  # print('Read a new frame: ', success)
