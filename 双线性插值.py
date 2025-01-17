import numpy as np
import cv2

def bilinear_inter(img,out_dim):
    src_h, src_w, channel = img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]
    print("src_h, src_w = ", src_h, src_w)
    print("dst_h, dst_w = ", dst_h, dst_w)
    dst_img = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)
    scale_x, scale_y =  float(src_w) / dst_w, float(src_h) / dst_h

    for i in range(3):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
              #几何中心重合#
              src_x = (dst_x + 0.5) * scale_x - 0.5
              src_y = (dst_y + 0.5) * scale_y - 0.5
              #寻找对应坐标及取整
              src_x0 = int(np.floor(src_x))
              src_x1 = min(src_x0 + 1, src_w - 1)
              src_y0 = int(np.floor(src_y))
              src_y1 = min(src_y0 + 1, src_h - 1)
              #计算插值
              temp0 = (src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
              temp1 = (src_x1 - src_x) * img[src_y1,src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
              dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)

    return dst_img

img = cv2.imread('test.jpg')
print("输出", img)
h1,w1=img.shape[:2]  #取得原图尺寸
dst_h1=int(h1/4)     #原图高缩小4倍
dst_w1=int(w1/4)     #原图宽缩小4倍
dst = bilinear_inter(img,(dst_w1,dst_h1))
cv2.imshow('nearest interp',dst)
cv2.imshow('scr img',img)
cv2.waitKey()

