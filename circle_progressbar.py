import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
blank_image = np.zeros((250,250,3), np.uint8)



def draw_half_circle_rounded(image,percentage):
    height, width = image.shape[0:2]
    # Ellipse parameters
    radius = 105
    center = (int(width / 2), int(height/2))
    center2 = (int(width / 2)-70, int(height/2)+15)
    axes = (radius, radius)
    angle = 0
    startAngle = 270
    endAngle = 270+int(360*(percentage/100)+20)
    thickness = 10
    color = (123, 196, 255)
    # http://docs.opencv.org/modules/core/doc/drawing_functions.html#ellipse
    cv2.circle(image, center, radius, (191, 221, 245), 12)
    #cv2.ellipse(image, center, axes, angle, startAngle, endAngle, ,-2)
    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)

    cv2.putText(image, str(format(percentage, '.1f')) +chr(37), center2, 1, 3, (191, 221, 245), 7 , cv2.LINE_AA)
    
    return image

blank_image[:]=(111,123,133)
draw_half_circle_rounded
cv2.imwrite("programs/static/media/result.png",draw_half_circle_rounded(blank_image,33.1))