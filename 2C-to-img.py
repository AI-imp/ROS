import numpy as np
import cv2
import labelme
f = open(r'E:\cource\u3exercise\data\CE3_BMYK_PCAML-C-041_SCI_N_20140113194426_20140113194426_0008_A.2C', 'rb')
data = f.read()
byte_array = bytearray(data[len(data)-2352 * 1728 * 3 : ])
numpy_array = np.frombuffer(byte_array,
dtype=np.uint8).reshape((1728, 2352, 3))
numpy_array = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2BGR)
cv2.imwrite("img.jpg",numpy_array)
numpy_array = cv2.resize(numpy_array, (2352 // 2, 1728 // 2))
cv2.imshow('img', numpy_array)
cv2.waitKey()
