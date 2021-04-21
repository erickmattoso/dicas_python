# libs
from PIL import Image, ImageDraw, ImageFilter

# imgs
im1 = Image.open('../../img/1.jpg')
im2 = Image.open('../../img/2.jpg')

# image 1
img = im1
img_w, img_h = img.size
background = Image.new('RGBA', (1440, 900), (000, 000, 255, 255))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)
background.save('../../img/img1.png')

# image 2
img_w, img_h = im2.size
bg_w, bg_h = im1.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
im3 = im1.copy()
im3.paste(im2, offset)
im3.save('../../img/img2.png')

# image 3
W, H = (300,200)
msg = "hello"
im = Image.new("RGBA",(W,H),"yellow")
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2), msg, fill="black")
im.save('../../img/img3.PNG', quality=95)

# image 4
im3 = im1.copy()
im3.paste(im2)
im3.save('../../img/img4.jpg', quality=95)

# image 5
im3 = im1.copy()
im3.paste(im2,(100, 50))
im3.save('../../img/img5.jpg', quality=95)

# image 6
mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((140, 50, 260, 170), fill=255)
im3 = im1.copy()
im3.paste(im2, (0, 0), mask_im)
im3.save('../../img/img6.jpg', quality=95)

# image 7
mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
im3 = im1.copy()
im3.paste(im2, (0, 0), mask_im_blur)
im3.save('../../img/img7.jpg', quality=95)

# image 8
mask_im = Image.open('../../img/0.png').resize(im2.size).convert('L')
im3 = im1.copy()
im3.paste(im2, (100, 50), mask_im)
im3.save('../../img/img8.jpg', quality=95)