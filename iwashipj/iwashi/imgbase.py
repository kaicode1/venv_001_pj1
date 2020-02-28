import numpy as np
from PIL import Image

im_in = Image.open('./sample/xray1.jpg')

im_in.show()

im_np = np.array(im_in)

im_out = Image.fromarray(im_np)

im_out.show()
