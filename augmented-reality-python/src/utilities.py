# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
import cv2
import numpy as np


# --------------------------
#   Transformation Function
# --------------------------
def convert_tx_rx_into_transformation(tx,rx):
    """
    Converts the transformation and rotation matrix into
    OpenGL transformation matrix.
    :param tx: Translation vector
    :param rx: Rotation vector
    :return: Transformation matrix for OpenGL (4 x 4)
    """
    r_matrix = cv2.Rodrigues(rx)
    transformation_matrix = np.array([[r_matrix[0], r_matrix[3], r_matrix[6], 0.0],
                                      [r_matrix[1], r_matrix[4], r_matrix[7], 0.0],
                                      [r_matrix[2], r_matrix[5], r_matrix[8], 0.0],
                                      [-tx[0], -tx[1], -tx[2], 1.0]])
    print(transformation_matrix)
    return transformation_matrix

if __name__ == '__main__':
    pass