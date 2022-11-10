from PIL import Image

import matplotlib.pyplot as plt


image = Image.open('./img/aaa.jpg')

# 图片格式 大小
# print(image.format, image.size, image.mode)

#打印图片
# plt.imshow(image)
# plt.show()

# 调整大小
o = image.resize((128, 128))
# 逆时针旋转45
# FLIP_LEFT_RIGHT 水平左右翻转
# Image.FLIP_TOP_BOTTOM 垂直上下翻转
# Image.ROTATE_90 逆时针90度
# Image.ROTATE_180 逆时针180度
# Image.ROTATE_270 逆时针270度
outfile= o.rotate(45)
plt.imshow(outfile)
plt.show()



# 剪切图片
# box= (100,100,400,500)
#
# region = image.crop(box)
#
# plt.imshow(region)
#
# plt.show()