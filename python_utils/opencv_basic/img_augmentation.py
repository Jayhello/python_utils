# _*_ coding:utf-8 _*_

"""
Deep learning image augmentation
cited from https://scottontechnology.com/flip-image-opencv-python/
"""

import cv2


def img_flip():
    path = "F:/ad_samples/train_samples/ad_text_artifact/base_type/type_10.jpg"
    img = cv2.imread(path)

    horizontal_img = img.copy()
    vertical_img = img.copy()
    both_img = img.copy()

    horizontal_img = cv2.flip(img, 0)
    vertical_img = cv2.flip(img, 1)
    both_img = cv2.flip(img, -1)

    cv2.imshow("original img", img)
    cv2.imshow("horizontal img", horizontal_img)
    cv2.imshow("vertical img", vertical_img)
    cv2.imshow("both flip", both_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img_flip()
    pass
