# encoding: utf-8
# module cv2.cv2
# from C:\Users\SRC\AppData\Local\Programs\Python\Python37\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as ca # C:\Users\SRC\AppData\Local\Programs\Python\Python37\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2 as __cv2


class dnn_DetectionModel(__cv2.dnn_Model):
    # no doc
    def detect(self, frame, confThreshold=None, nmsThreshold=None): # real signature unknown; restored from __doc__
        """
        detect(frame[, confThreshold[, nmsThreshold]]) -> classIds, confidences, boxes
        .   @brief Given the @p input frame, create input blob, run net and return result detections.
        .             *  @param[in]  frame  The input image.
        .             *  @param[out] classIds Class indexes in result detection.
        .             *  @param[out] confidences A set of corresponding confidences.
        .             *  @param[out] boxes A set of bounding boxes.
        .             *  @param[in] confThreshold A threshold used to filter boxes by confidences.
        .             *  @param[in] nmsThreshold A threshold used in non maximum suppression.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


