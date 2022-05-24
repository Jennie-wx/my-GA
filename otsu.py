import cv2
import numpy as np
import matplotlib.pyplot as plt

GRAY_SCALE = 256


def otsuth(img, threshold):
    image_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


    fg_pix = image_gray > threshold
    bg_pix = image_gray <= threshold

    w0 = float(np.sum(fg_pix)) / image_gray.size
    w1 = float(np.sum(bg_pix)) / image_gray.size

    u0 = 0
    u1 = 0
    if np.sum(fg_pix) != 0:
        u0 = np.sum(image_gray * fg_pix) / np.sum(fg_pix)
    if np.sum(bg_pix) != 0:
        u1 = np.sum(image_gray * bg_pix) / np.sum(bg_pix)

    val = w0 * w1 * (u0 - u1) * (u0 - u1)
    return val


if __name__ == '__main__':
    file_path = 'ship.jpg'
    image = cv2.imread(file_path)
    cv2.imshow('origin_img', image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    image_gray[image_gray > 143] = 255

    cv2.imshow('IM_OTSU', image_gray)
    cv2.waitKey(-1)

    # v = []
    # for i in range(GRAY_SCALE):
    #     print(i)
    #     v.append(otsuth(image, i))
    #
    # max_v = max(v)
    # ind = v.index(max_v)
    #
    # plt.plot(range(GRAY_SCALE), v)
    # y_lim = plt.ylim()
    # plt.plot([ind, ind], y_lim, 'm--')
    # plt.ylim(min(v), max(v) + 100)
    # plt.xlim(0, 255)

    # plt.show()


