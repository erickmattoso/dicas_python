# libs
from PIL import Image, ImageDraw, ImageFilter

# imgs
im1 = Image.open('../../img/1.jpg')
im2 = Image.open('../../img/2.jpg')

# image 2
img_w, img_h = im2.size
bg_w, bg_h = im1.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
im1.paste(im2, offset)
im1.save('../../img/img2.png')
