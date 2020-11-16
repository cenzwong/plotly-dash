# https://docs.opencv.org/3.4/de/dc3/classcv_1_1QRCodeDetector.html

import cv2

img = cv2.imread('./QR.png')
QRDetector = cv2.QRCodeDetector()
help(QRDetector)

"""
Help on QRCodeDetector object:

class QRCodeDetector(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  decode(...)
 |      decode(img, points[, straight_qrcode]) -> retval, straight_qrcode
 |      .   @brief Decodes QR code in image once it's found by the detect() method.
 |      .   
 |      .        Returns UTF8-encoded output string or empty string if the code cannot be decoded.
 |      .        @param img grayscale or color (BGR) image containing QR code.
 |      .        @param points Quadrangle vertices found by detect() method (or some other algorithm).
 |      .        @param straight_qrcode The optional output image containing rectified and binarized QR code
 |  
 |  decodeMulti(...)
 |      decodeMulti(img, points[, straight_qrcode]) -> retval, decoded_info, straight_qrcode
 |      .   @brief Decodes QR codes in image once it's found by the detect() method.
 |      .        @param img grayscale or color (BGR) image containing QR codes.
 |      .        @param decoded_info UTF8-encoded output vector of string or empty vector of string if the codes cannot be decoded.
 |      .        @param points vector of Quadrangle vertices found by detect() method (or some other algorithm).
 |      .        @param straight_qrcode The optional output vector of images containing rectified and binarized QR codes
 |  
 |  detect(...)
 |      detect(img[, points]) -> retval, points
 |      .   @brief Detects QR code in image and returns the quadrangle containing the code.
 |      .        @param img grayscale or color (BGR) image containing (or not) QR code.
 |      .        @param points Output vector of vertices of the minimum-area quadrangle containing the code.
 |  
 |  detectAndDecode(...)
 |      detectAndDecode(img[, points[, straight_qrcode]]) -> retval, points, straight_qrcode
 |      .   @brief Both detects and decodes QR code
 |      .   
 |      .        @param img grayscale or color (BGR) image containing QR code.
 |      .        @param points optional output array of vertices of the found QR code quadrangle. Will be empty if not found.
 |      .        @param straight_qrcode The optional output image containing rectified and binarized QR code
 |  
 |  detectAndDecodeMulti(...)
 |      detectAndDecodeMulti(img[, points[, straight_qrcode]]) -> retval, decoded_info, points, straight_qrcode
 |      .   @brief Both detects and decodes QR codes
 |      .       @param img grayscale or color (BGR) image containing QR codes.
 |      .       @param decoded_info UTF8-encoded output vector of string or empty vector of string if the codes cannot be decoded.
 |      .       @param points optional output vector of vertices of the found QR code quadrangles. Will be empty if not found.
 |      .       @param straight_qrcode The optional output vector of images containing rectified and binarized QR codes
 |  
 |  detectMulti(...)
 |      detectMulti(img[, points]) -> retval, points
 |      .   @brief Detects QR codes in image and returns the vector of the quadrangles containing the codes.
 |      .        @param img grayscale or color (BGR) image containing (or not) QR codes.
 |      .        @param points Output vector of vector of vertices of the minimum-area quadrangle containing the codes.
 |  
 |  setEpsX(...)
 |      setEpsX(epsX) -> None
 |      .   @brief sets the epsilon used during the horizontal scan of QR code stop marker detection.
 |      .        @param epsX Epsilon neighborhood, which allows you to determine the horizontal pattern
 |      .        of the scheme 1:1:3:1:1 according to QR code standard.
 |  
 |  setEpsY(...)
 |      setEpsY(epsY) -> None
 |      .   @brief sets the epsilon used during the vertical scan of QR code stop marker detection.
 |      .        @param epsY Epsilon neighborhood, which allows you to determine the vertical pattern
 |      .        of the scheme 1:1:3:1:1 according to QR code standard.


"""

QRDetector.detectAndDecode(img)
"""('HPE', array([[[ 16.,  16.],
         [183.,  16.],
         [183., 183.],
         [ 16., 183.]]], dtype=float32), array([[  0.,   0.,   0.,   0.,   0.,   0.,   0., 255., 255.,   0., 255.,
           0.,   0., 255.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
        [  0., 255., 255., 255., 255., 255.,   0., 255., 255.,   0.,   0.,
           0., 255., 255.,   0., 255., 255., 255., 255., 255.,   0.],
        [  0., 255.,   0.,   0.,   0., 255.,   0., 255.,   0.,   0., 255.,
           0.,   0., 255.,   0., 255.,   0.,   0.,   0., 255.,   0.],
        [  0., 255.,   0.,   0.,   0., 255.,   0., 255., 255.,   0., 255.,
           0., 255., 255.,   0., 255.,   0.,   0.,   0., 255.,   0.],
        [  0., 255.,   0.,   0.,   0., 255.,   0., 255., 255., 255.,   0.,
         255.,   0., 255.,   0., 255.,   0.,   0.,   0., 255.,   0.],
        [  0., 255., 255., 255., 255., 255.,   0., 255., 255., 255., 255.,
         255.,   0., 255.,   0., 255., 255., 255., 255., 255.,   0.],
        [  0.,   0.,   0.,   0.,   0.,   0.,   0., 255.,   0., 255.,   0.,
         255.,   0., 255.,   0.,   0.,   0.,   0.,   0.,   0.,   0.],
        [255., 255., 255., 255., 255., 255., 255., 255.,   0.,   0., 255.,
           0.,   0., 255., 255., 255., 255., 255., 255., 255., 255.],
        [  0.,   0.,   0., 255.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,
           0., 255.,   0.,   0., 255., 255., 255.,   0., 255., 255.],
        [255., 255., 255.,   0., 255.,   0., 255.,   0., 255., 255., 255.,
         255., 255., 255.,   0., 255., 255.,   0., 255.,   0.,   0.],
        [255.,   0., 255.,   0.,   0., 255.,   0., 255.,   0., 255.,   0.,
         255.,   0., 255., 255., 255.,   0.,   0., 255.,   0.,   0.],
        [255., 255., 255., 255.,   0.,   0., 255., 255.,   0., 255., 255.,
         255., 255., 255.,   0., 255., 255.,   0.,   0., 255., 255.],
        [255., 255., 255., 255., 255.,   0.,   0., 255.,   0.,   0.,   0.,
         255.,   0., 255.,   0., 255.,   0., 255.,   0., 255.,   0.],
        [255., 255., 255., 255., 255., 255., 255., 255.,   0.,   0.,   0.,
           0., 255.,   0., 255.,   0., 255.,   0., 255., 255.,   0.],
        [  0.,   0.,   0.,   0.,   0.,   0.,   0., 255.,   0.,   0.,   0.,
           0., 255.,   0.,   0.,   0., 255., 255.,   0., 255., 255.],
        [  0., 255., 255., 255., 255., 255.,   0., 255.,   0., 255.,   0.,
           0.,   0.,   0., 255.,   0.,   0.,   0., 255., 255., 255.],
        [  0., 255.,   0.,   0.,   0., 255.,   0., 255.,   0.,   0., 255.,
           0., 255.,   0.,   0.,   0., 255., 255.,   0., 255.,   0.],
        [  0., 255.,   0.,   0.,   0., 255.,   0., 255., 255., 255.,   0.,
         255., 255., 255.,   0., 255., 255., 255.,   0.,   0., 255.],
        [  0., 255.,   0.,   0.,   0., 255.,   0., 255.,   0.,   0.,   0.,
         255.,   0., 255., 255., 255.,   0., 255., 255., 255.,   0.],
        [  0., 255., 255., 255., 255., 255.,   0., 255.,   0.,   0., 255.,
         255., 255., 255.,   0., 255., 255., 255.,   0.,   0.,   0.],
        [  0.,   0.,   0.,   0.,   0.,   0.,   0., 255.,   0., 255.,   0.,
         255.,   0., 255.,   0., 255.,   0., 255.,   0., 255.,   0.]],
       dtype=float32))"""
