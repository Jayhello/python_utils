# coding:utf-8

import numpy as np
import cv2


def NMS(bboxes, threshold=0.5, model='union'):
    """
    Non max suppression
    :param bboxes: tensor bounding boxes and scores sized [N, 5]
    :param threshold:float overlap threshold
    :param model: str 'union', 'min'
    :return:
        bboxes after nms
        picked indices
    """
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    scores = bboxes[:, 4]

    # all the box areas
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    # descending order scores
    orders = np.argsort(-scores)

    # store the saving indices of the bounding box
    keep_idx = []

    while len(orders) > 0:
        idx = orders[0]
        keep_idx.append(idx)

        # tensor operator, compute all the intersect with the max score area
        xx1 = np.maximum(x1[idx], x1[orders[1:]])
        yy1 = np.maximum(y1[idx], y1[orders[1:]])
        xx2 = np.minimum(x2[idx], x2[orders[1:]])
        yy2 = np.minimum(y2[idx], y2[orders[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        # get all the intersect area, note this is tensor operator
        inter = w * h

        # compute the ratio of overlap, note this is tensor operator
        overlap_ratio = inter / (areas[idx] + areas[orders[1:]] - inter)

        inds = np.where(overlap_ratio <= threshold)[0]
        orders = orders[inds + 1]  # add 1, because the first is the keep index

    return bboxes[keep_idx], keep_idx


def draw_rect_score(img, lst_box):
    # draw rectangle, and score into img
    for box in lst_box:
        p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
        cv2.rectangle(img, p1, p2, (0, 0, 255), 2)
        score = str(box[4])
        cv2.putText(img, score, p1, cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 0, 0), 2)


def compute_iou(box1, box2):
    """
    Compute iou rate of two box.
    :param box1: lst [x1, y1, x2, y2, score]
    :param box2: like box1
    :return: float iou rate
    """
    # compute iou area x1, y1, x2, y2
    xx1 = max(box1[0], box2[0])
    yy1 = max(box1[1], box2[1])
    xx2 = min(box1[2], box2[2])
    yy2 = min(box1[3], box2[3])

    # compute intersect area
    w, h = max(xx2 - xx1 + 1, 0.0), max(yy2 - yy1 + 1, 0.0)
    inter_area = w * h

    area1 = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    area2 = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    return inter_area / float(area1 + area2 - inter_area)


def test_iou_rate():
    """Test iou compute.
    """
    # box group1
    box1 = [146, 173, 240, 263]
    box2 = [160, 152, 251, 245]
    box2 = [174, 196, 266, 282]
    print compute_iou(box1, box2)  # 0.37405

    # box group2
    box1 = [556, 102, 648, 198]
    box2 = [570, 133, 670, 228]
    print compute_iou(box1, box2)  # 0.38613


def test_nms():
    img_path = 'E:/bolg_img/deeplearn/nms/nms_4.jpg'
    lst_box = [[146, 173, 240, 263, 0.98], [160, 152, 251, 245, 0.83],
               [174, 196, 266, 282, 0.75],
               [556, 102, 648, 198, 0.81],
               [570, 133, 670, 228, 0.67]
               ]
    lst_box = np.array(lst_box)

    img = cv2.imread(img_path)
    img_copy = img.copy()
    draw_rect_score(img, lst_box)

    lst_box, _ = NMS(lst_box, 0.2)
    draw_rect_score(img_copy, lst_box)

    cv2.imshow("img_with_rect", img)
    cv2.imshow("nms_img_with_rect", img_copy)

    cv2.waitKey(0)


if __name__ == '__main__':
    test_iou_rate()
    # test_nms()

    arr = np.array([4, 1, 3, 5])
    print arr.size

    pass
