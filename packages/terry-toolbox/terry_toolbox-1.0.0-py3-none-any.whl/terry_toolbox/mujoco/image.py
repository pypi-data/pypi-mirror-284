import cv2
import numpy as np
import mujoco

def grab_image(viewer, resize_rate=None,interpolation=cv2.INTER_NEAREST):
    """
        Grab the rendered iamge
    """
    img = np.zeros((viewer.viewport.height,viewer.viewport.width,3),dtype=np.uint8)
    mujoco.mjr_render(viewer.viewport,viewer.scn,viewer.ctx)
    mujoco.mjr_readPixels(img, None,viewer.viewport,viewer.ctx)
    img = np.flipud(img) # flip image
    # Resize
    if resize_rate is not None:
        h = int(img.shape[0]*resize_rate)
        w = int(img.shape[1]*resize_rate)
        img = cv2.resize(img,(w,h),interpolation=interpolation)
    return img