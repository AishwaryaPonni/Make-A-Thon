from PIL import Image
import PIL

import os
import qrcode
import os.path
from os import path
img=qrcode.make('Room2')

img=img.save('room_2.jpg')
print(path.exists("room_2.jpg"))


