
import cv2
import numpy as np

def function(img,out_dim):
    src_h,src_w,c= img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]
    print ("src_h, src_w = ", src_h, src_w)
    print ("dst_h, dst_w = ", dst_h, dst_w)
    dst_img = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)

    for i in range(dst_h):
        for j in range(dst_w):
            x0 = int(np.floor(i * src_h/dst_h ))
            x  = min(x0 + 1,src_h)
            y0 = int(np.floor(j * src_w/dst_w ))
            y = min(y0 + 1, src_w)
            dst_img[i, j] = img[x, y]
    return dst_img

if __name__ == '__main__':
    img = cv2.imread('test.jpg')
    print ("输出", img)
    h1,w1=img.shape[:2]
    dst_h1=int(h1/4)
    dst_w1=int(w1/4)
    dst = function(img,(dst_w1,dst_h1))
    cv2.imshow('nearest interp',dst)
    cv2.imshow('scr img',img)
    cv2.waitKey()

