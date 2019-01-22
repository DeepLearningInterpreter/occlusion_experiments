import numpy as np
import pandas as pd

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

def compute_IoU(box_pred, box):
    [xA1, yA1, xA2, yA2] = box_pred
    [xB1, yB1, xB2, yB2] = box

    xy = pd.DataFrame({'A1': [xA1, yA1], 'A2': [xA2, yA2],
                     'B1': [xB1, yB1], 'B2': [xB2, yB2]})

    xy = np.array(xy)
    #calculating x_overlap
    (A1, A2, B1, B2) = xy[0,:]
    if A1 >= B2 or B1 >= A2:
        x_overlap = 0
    elif A1 <= B1 and B2 <= A2:
        x_overlap = B2 - B1
    elif B1 <= A1 and A2 <= B2:
        x_overlap = A2 - A1
    elif B1 >= A1:
        x_overlap = A2 - B1
    else:
        x_overlap = B2 - A1

    #calculating y_overlap
    (A1, A2, B1, B2) = xy[1,:]
    if A1 >= B2 or B1 >= A2:
        y_overlap = 0
    elif A1 <= B1 and B2 <= A2:
        y_overlap = B2 - B1
    elif B1 <= A1 and A2 <= B2:
        y_overlap = A2 - A1
    elif B1 >= A1:
        y_overlap = A2 - B1
    else:
        y_overlap = B2 - A1

    intersection = x_overlap*y_overlap
    areaA = (xA2-xA1)*(yA2-yA1)
    areaB = (xB2-xB1)*(yB2-yB1)
    union = areaA + areaB - intersection

    IoU = intersection/union

    #print('intersection:', intersection)
    #print('union:', union)
    #print('IoU:', IoU)
    return IoU
